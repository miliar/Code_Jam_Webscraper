#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

const int LSIZE = 15;
const int DSIZE = 5000;
const int NSIZE = 500;

string Dbuff[ DSIZE ];
string Nbuff[ NSIZE ];
int NCount[NSIZE];

bool isMatch( string D , string N , int i , bool flg=true)
{
	if( D.empty() || N.empty() ){
		//if( flg ) NCount[i]++;
		return flg;
	}
	string tmp;
	if( *N.begin() == '(' ){
		do{
			tmp+= *N.begin();
			N.erase( N.begin() , N.begin()+1 );
		}while( *N.begin() != ')' );
		N.erase( N.begin() , N.begin()+1 );
	}
	else{
		tmp += *N.begin();
		N.erase( N.begin() , N.begin()+1 );
	}
	if( find( tmp.begin() , tmp.end() , *D.begin()) == tmp.end() ){
		//cout << D << " " << N <<endl;
		flg = false;
	}
	D.erase( D.begin() , D.begin()+1 );

	return isMatch( D , N , i ,flg);
}

int main()
{
	
	int l , d , n;
	cin >> l >> d >> n;

	for(int i=0 ; i<d ; i++ )
		cin >> Dbuff[ i ];
	for(int i=0 ; i<n ; i++ )
		cin >> Nbuff[ i ];


	for( int i=0 ; i<d ; i++ )
	{
		for( int j=0 ; j<n ; j++ )
		{
			if( isMatch( Dbuff[i] , Nbuff[j] , j ) ){
				NCount[j]++;
			}
		}
	}

	for( int i=0 ; i<n ; i++ )
	{
		cout << "Case #" << i+1 <<": "<< NCount[i] <<endl;
	}

	return 0;
}
