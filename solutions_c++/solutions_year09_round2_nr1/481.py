#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

const char* INPUT_FILE_NAME  = "A-large.in";
const char* OUTPUT_FILE_NAME = "A-large.out";
//const char* INPUT_FILE_NAME  = "A-small-attempt0.in";
//const char* OUTPUT_FILE_NAME = "A-small-attempt0.out";
//const char* INPUT_FILE_NAME  = "A-small.in";
//const char* OUTPUT_FILE_NAME = "A-small.out";

class TreeData
{
public:
	TreeData( double _prob, string _feature, TreeData* _trueData, TreeData* _falseData ) : prob( _prob )
													   , feature( _feature )
													   , trueData( _trueData )
													   , falseData( _falseData ) {}
	~TreeData()
	{
		delete trueData;
		delete falseData;
	}
	double prob;
	string feature;
	TreeData* trueData;
	TreeData* falseData;
};

TreeData* GetNode( const vector<string>& tokens, int startIndex, int& endIndex )
{
	if( tokens[ startIndex + 2 ].compare( ")" ) == 0 )
	{
		endIndex = startIndex + 2;
		return new TreeData( atof( tokens[ startIndex + 1 ].c_str() ), "", NULL, NULL );
	}
	else
	{
		TreeData* trueData = GetNode( tokens, startIndex + 3, endIndex );
		TreeData* falseData = GetNode( tokens, endIndex + 1, endIndex );
		++endIndex;
		return new TreeData( atof( tokens[ startIndex + 1 ].c_str() ), 
						 tokens[ startIndex + 2 ], trueData, falseData );
	}
}

TreeData* ParseTree( const vector<string>& tokens )
{
	int endIndex;
	return GetNode( tokens, 0, endIndex );
}

double GetProbValue( const set<string>& features, TreeData* rootNode )
{
	double prob = 1.0;

	TreeData* currentNode = rootNode;

	while( 1 )
	{
		prob *= currentNode->prob;

		if( currentNode->trueData == NULL )
			break;

		if( features.find( currentNode->feature ) != features.end() )
		{
			currentNode = currentNode->trueData;
		}
		else
			currentNode = currentNode->falseData;
	}

	return prob;
}

void GetTokens( fstream& inputFileStream, vector<string>& tokens, int L )
{
	char buffer[8192];

	for( int i = 0 ; i < L; ++i )
	{
		inputFileStream.getline(buffer, 8192);
		string line( buffer );

		int size = line.size();

		int tokenStartPos = -1;
		for( int j = 0 ; j < size ; ++j )
		{
			if( buffer[ j ] == '(' )
			{
				if( tokenStartPos != -1 )
				{
					tokens.push_back( line.substr( tokenStartPos, j - tokenStartPos ) );
					tokenStartPos = -1;
				}
				tokens.push_back( "(" );
			}
			else if( buffer [ j ] == ')' )
			{
				if( tokenStartPos != -1 )
				{
					tokens.push_back( line.substr( tokenStartPos, j - tokenStartPos ) );
					tokenStartPos = -1;
				}
				tokens.push_back( ")" );
			}
			else if( buffer[ j ] == ' ' || buffer[ j ] == '\n' )
			{
				if( tokenStartPos != -1 )
				{
					tokens.push_back( line.substr( tokenStartPos, j - tokenStartPos ) );
					tokenStartPos = -1;
				}
			}
			else
			{
				if( tokenStartPos == -1 )
					tokenStartPos = j;
			}
		}
		if( tokenStartPos != -1 )
		{
			tokens.push_back( line.substr( tokenStartPos, size - tokenStartPos ) );
			tokenStartPos = -1;
		}
	}
}

int main()
{
	int N;
	string strOutput;
	string strInput;

	fstream inputFileStream(INPUT_FILE_NAME, ios_base::in);
	fstream outputFileStream(OUTPUT_FILE_NAME, ios_base::out|ios_base::trunc);
	outputFileStream.setf(ios_base::floatfield, ios_base::fixed);
	outputFileStream.precision(7);
	cout.setf(ios_base::floatfield, ios_base::fixed);
	cout.precision(7);

	inputFileStream >> N;
	char buffer[8192];
	inputFileStream.getline(buffer, 8192);

	for( int i = 0; i < N; ++i )
	{
		int L;
		inputFileStream >> L;
		inputFileStream.getline(buffer, 8192);

		vector<string> tokens;
		GetTokens( inputFileStream, tokens, L );

		TreeData* root = ParseTree( tokens );

		int A;
		inputFileStream >> A;
		inputFileStream.getline(buffer, 8192);

		outputFileStream << "Case #" << i+1 << ": " << endl;
		cout << "Case #" << i+1 << ": " << endl;

		for( int k = 0 ; k < A ; ++k )
		{

			string temp;
			inputFileStream >> temp;
			int F;
			inputFileStream >> F;
			set<string> features;
			for( int j = 0; j < F; ++j )
			{
				string feature;
				inputFileStream >> feature;
				features.insert( feature );
			}

			double probValue = GetProbValue( features, root );
			outputFileStream << probValue << endl;
			cout << probValue << endl;
		}

		delete root;
	}

	inputFileStream.close();
	outputFileStream.flush();
	outputFileStream.close();

	return 0;
}
