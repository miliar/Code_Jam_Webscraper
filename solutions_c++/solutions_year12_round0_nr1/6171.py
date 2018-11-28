#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <set>
using namespace std;

const string c_strInput = "training.txt";

bool CompareChar( char A , char B){

	return A < B ;}


void PrintPair( pair<char, char > char_char )
{
	cout<< (char_char.first)<<" = "<< (char_char.second) << endl;
}

void FillRange( set< char >& range, set<char>& domain )
{
	for( char i = 'a' ; i <= 'z' ; i++ )
	{
		range.insert( i );
		domain.insert( i );
	}
}

void Train( map<char,char>& CharMap )
{

	int len ;//Number of test cases
	string line;
	stringstream parser;
	map<char , char >::iterator it;
	set< char > range;
	set< char > domain;

	vector< string > m_Inputs;
	vector< string > m_Outputs;

	FillRange( range, domain );
	cout<<range.size() << " "<< domain.size()<<endl;
	//Open input file.
	fstream trainData;
	trainData.open( c_strInput.c_str(), fstream::in );

	if( !trainData.is_open() )
		cerr<<"Error, File not open !!"<<endl;

	getline( trainData , line );//Input
	getline( trainData , line );//3
	parser<<line;
	parser>>len;

	cout<<"There are "<<len<<" test cases:"<<endl<<"Inputs:"<<endl<<endl;

	for( int Case = 0 ; Case < len ; Case++ )
	{
		getline( trainData , line );
		m_Inputs.push_back( line );
		cout<<line<<endl;
	}

	getline( trainData , line );//output

	cout<<"Onputs:"<<endl<<endl;

	for( int Case = 0 ; Case < len ; Case++ )
	{
		getline( trainData , line );
		m_Outputs.push_back( line.substr( 9 ,line.length() ) );
		cout<<m_Outputs[ Case ]<<endl;
	}
	trainData.close();

	//Fill in the Dictionary
	for( int Case = 0 ; Case < len ; Case++ )
	{
		for( int i = 0 ; i < m_Inputs[ Case ].length(); i++ )
		{
			char letter = (m_Inputs[ Case ])[ i ] ;
			if( letter !=  ' ' )
			{
				it = CharMap.find( letter );
				if( it == CharMap.end() )
				{
					//cout<<"New Letter "<<letter <<" = "<<m_Outputs[ Case ][ i ]<<endl;
					CharMap[ letter ] = m_Outputs[ Case ][ i ];
					range.erase( letter );
					domain.erase( m_Outputs[ Case ][ i ] );
				}
			}
			else
			{
				if( m_Outputs[ Case ][ i ] != ' ' )
				{
					cerr<<"Error !!1"<<endl;
				}
			}
		
		}
	}
	
	//Insert the values the question itself.
	CharMap[ 'z' ] = 'q';
	range.erase( 'z' );
	domain.erase( 'q' );
	
	if( CharMap.size() < 26 ){
		cout<<"Not all characters are mapped "<<endl;
		cout<<range.size() << " "<< domain.size()<<endl;
		CharMap[ *(range.begin()) ] = *(domain.begin());
	}

	//print the dictionary
	for_each( CharMap.begin() , CharMap.end(), PrintPair );
	//pushing space 
	CharMap[ ' ' ] = ' ';

}

void Readinput( vector<string>& Inputs )
{
	fstream InputData;
	int len;
	string   line;
	InputData.open( "input.txt", fstream::in );
	stringstream parser;

	if( !InputData.is_open() )
		cerr<<"Error, File not open !!"<<endl;

	getline( InputData , line );//3
	parser<<line;
	parser>>len;

	//cout<<"There are "<<len<<" test cases:"<<endl<<"Inputs:"<<endl;

	for( int Case = 0 ; Case < len ; Case++ )
	{
		getline( InputData , line );
		Inputs.push_back( line );
//		cout<<line<<endl;
	}
	
}
void Translate( map<char,char>& Dic ,vector<string>& Inputs, vector< string >& Outputs )
{
//	void trans( string old ){
//		string New = old;
//		for( string::iterator it = New.begin(); it != New.end(); it++ )
//			*it = Dic[ *it ];
//		Output.push_back( New );
//		}
//		
//	for_each( Input.begin(), Input.end(), trans );
	string New;
	for( vector< string >::iterator it = Inputs.begin(); it != Inputs.end(); it++ )
	{
		New = *it;
		for( string::iterator char_it = New.begin(); char_it != New.end(); char_it++ )
		{
			*char_it = Dic[ *char_it ];
		} 
		Outputs.push_back( New );
		cout<<"Pushing: "<<New<<endl; 
	}

}

void WriteOut( vector<string> Outputs ){

	fstream Out;
	Out.open( "Output.txt", fstream::out );
	int i = 1;
	for( vector<string>::iterator it = Outputs.begin(); it != Outputs.end(); it++ )
	{
		Out<<"Case #"<<i++<<":"<<" "<<*it<<endl;
	}
	Out.close();

}
int main()
{

	map<char,char>   CharMap;//our dictionary
	vector< string > Inputs;
	vector< string > Outputs;

	//Train fills the dictionary
	Train( CharMap );
	//read inputs.
	Readinput( Inputs );
	//Translate.
	Translate( CharMap , Inputs, Outputs );
	//Write to file
	WriteOut( Outputs );

	return 0;

}
