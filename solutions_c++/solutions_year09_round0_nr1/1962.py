#include <fstream>
#include <vector>
#include <string>
#include <list>
#include <algorithm>

class RemovePrediction
{
	const std::list<char>& rem_;
	unsigned indextoCheck_;
public:
	RemovePrediction( const std::list<char>& rem, unsigned indextoCheck ):
	rem_(rem), indextoCheck_(indextoCheck){
	}
	bool operator()( const std::string* strToCheck ){
		char cSearched = (*strToCheck)[indextoCheck_];
		return std::find(rem_.begin(), rem_.end(), cSearched ) == rem_.end();
	}
};
void SolveTask( const char* inputFileName, const char* outputFileName )
{
	std::ifstream inFile( inputFileName );
	std::ofstream oFile( outputFileName );

	unsigned L(0);
	unsigned D(0);
	unsigned N(0);
	inFile >> L;
	inFile >> D;
	inFile >> N;
	std::list< std::string > inputData;
	// dictionary filling
	for ( unsigned i = 0; i < D; i++ )
	{
		std::string bufString;
		inFile >> bufString;
		inputData.push_back(bufString);
	}
	inputData.sort();
	for ( unsigned i = 0; i < N; i++ )
	{
		std::string testingString;
		inFile >> testingString;
		typedef std::list< const std::string* > TStringList;
		typedef std::list<char> TCharVec;
		TStringList bufList;
		TCharVec searchedChars;
		unsigned curPosition = 0;
		
		for( std::list<std::string>::const_iterator j = inputData.begin(); j != inputData.end(); j++ )
		{
			bufList.push_back(&(*j));
		}
		for( unsigned j = 0; j < L; j++ )
		{
			if( bufList.empty() )
				break;
			searchedChars.clear();
			if( testingString[curPosition]=='(' )
			{
				curPosition++;
				while( testingString[curPosition] != ')')
				{
					searchedChars.push_back(testingString[curPosition]);
					curPosition++;
				}
				searchedChars.sort();
			}
			else
			{
				searchedChars.push_back(testingString[curPosition]);
			}
			curPosition++;
			RemovePrediction rPred(searchedChars, j);
			bufList.remove_if( rPred );
		}
		oFile << "Case #" << (i+1) << ": " << bufList.size() << std::endl;
	}
}

void main()
{
	SolveTask( "d:/1.txt", "d:/2.txt");
}