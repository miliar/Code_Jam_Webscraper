#include<fstream>
#include<string>
using namespace std;

bool Search ( char , string );

bool checkEquiv ( string , string  );
int main()
{
	int T, C,D , N ;
	char element;
	string list ;
	string *baseOppos , *baseEquiv;
	ifstream in;   ofstream out;
	in.open( "in.txt" );
	out.open ( "out.txt" );
	in>>T;
	for ( int k=0 ; k < T ; k++ )
	{
		in>>C;
		baseEquiv = new string[C];
		for ( int j=0 ; j < C ;j++ )
			in>>baseEquiv[j];
		in>>D;
		baseOppos = new string[D];
		for ( int j=0 ; j < D ;j++ )
			in>>baseOppos[j];
		in>>N;
		if ( N != 0 )
		{
			for ( int i=0 ; i < N ; i++ )
			{
				in>>element;
				list.insert ( list.end() , element );
				if ( list.length()>1)
					for ( int j=0 ; j < C ;j++ ) 
						if ( checkEquiv ( baseEquiv[j] , list ) )
							{
								list.erase( list.end()-1 );
								list.erase( list.end()-1 );
								list.insert ( list.end() , 1 , baseEquiv[j][2] );
								break;
							}	
				for ( int j=0 ; j < D ; j++ ) 
					if ( Search( baseOppos[j][0] , list ) && Search( baseOppos[j][1] , list ) )
					{ list.clear(); break;}
			}
		}
		out <<"Case #"<<k+1<<": [";
		if ( list.length() != 0 )
			{
				out<<list[0];
				for ( int i=1 ; i < list.length() ; i++ )
					out<<", "<<list[i];
			}
		out<<"]\n";
		list.clear();
	}
	in.close();
	out.close();
	return 0;
}

bool Search ( char c , string list  )
{
	for ( int i=0 ; i < list.length() ; i++ )
		if ( c == list[i] )
			return true;
	return false;
}

bool checkEquiv ( string baseEquiv , string list )
{
	return (( list[list.length()-1] ==baseEquiv[0]) && (list[list.length()-2]==baseEquiv[1]))|| ((list[list.length()-1] == baseEquiv[1]) && (list[list.length()-2] == baseEquiv[0]) );
}