#include<iostream>
#include<cstdio>
#include<cmath>
#include <fstream>
using namespace std;
ifstream fin("C:\\Users\\Edward\\A-large.in");
ofstream fout("C:\\Users\\Edward\\A-small-attempt1.out");
 
#define cin fin
#define cout fout
int main()
{
	int os , bs , omax , bmax , stb , sto;
	char j;
	int t , n , num;
	int i , d;
	cin>>t;
	num = 0;
	while( t-- )
	{
		cin>>n;
		omax = bmax = 0;
		os = bs = 1;
		++num;
		for( i = 0 ; i < n ; ++i )
		{
			cin>>j>>d;
			if( j == 'O' )
			{
				sto = abs( d - os ) + 1;
				if( sto + omax > bmax + 1 )
				{ omax = sto + omax; }
				else
				{ omax = bmax + 1; }
				os = d;
			}
			else
			{ 
				stb = abs( d - bs ) + 1;
				if( stb + bmax > omax + 1 )
				{ bmax = stb + bmax; }
				else
				{ bmax = omax + 1; }
				bs = d;
			}
		}
		cout<<"Case #"<<num<<": "<<(omax > bmax ? omax : bmax)<<"\n";
	}
	return 0;
}