#include <iostream>
#include <string>
#include <fstream>
using namespace std;



bool QuestionOne( int N , int K )
{
	int iMax = 1;

	for ( int i = 1 ; i < N ; i++ )
	{
		iMax = ( iMax << 1 ) + 1;
	}


	if ( ( K & iMax ) == iMax )
	{
		return true;
	}
	else
	{
		return false;
	}
}



int main( )
{
	string sFileName = "A-large.in";
    ifstream ifile( sFileName.c_str() );
    ofstream ofile( "One.txt" );
	string sline;

	getline( ifile , sline );
	
	int iLineNum= 0;
	
	for ( size_t i = 0 ; i < sline.length() ; i ++ )
	{
		iLineNum *= 10;
		iLineNum += sline[i] - '0';
	}

	for ( int i = 0 ; i < iLineNum ; i ++ )
	{
		getline( ifile , sline );

		string sN = sline.substr( 0 , sline.find(" ") ) ;
		string sK = sline.substr( sline.find(" ") + 1 ,  sline.length() - sline.find(" ") - 1 );

		int iN = 0 ;
		for ( size_t j = 0 ; j < sN.length() ; j ++ )
		{
			iN *= 10;
			iN += sN[j] - '0';

		}

		int iK =0 ;

		for ( size_t j = 0 ; j < sK.length() ; j ++ )
		{
			iK *= 10;
			iK += sK[j] - '0';
		}
       
		ofile << "Case #";
		char cTmp[10];
		itoa( i + 1 , cTmp , 10 );
		ofile << string(cTmp) << ":";

		if ( QuestionOne(  iN , iK ) )
		{
		    ofile << " ON" << endl;	 
		}
		else
		{
            ofile << " OFF" << endl;
		}


	}

    ofile.close();
	ifile.close();

	//cout << "Hello world!" << endl;
}