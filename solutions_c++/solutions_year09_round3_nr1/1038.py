// task1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cstdio>
#include <utility>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>

#pragma warning(disable:4996)

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define REP(i,n) FOR(i,0,n)
#define REPD(i,n) FORD(i,0,n)
#define VAR(v,w) __typeof(w) v=(w)
#define FORE(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define PB push_back
#define ALL(c) (c).begin(),(c).end()
#define RALL(C) (C).rbegin(), (C).rend()
#define SIZE(c) ((int)(c).size())
#define MP make_pair
#define FT first
#define SD second

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VII;
typedef vector<double> VD;
typedef vector<LD> VLD;
typedef vector<LL> VLL;
typedef vector<bool> VB;
typedef istringstream ISS;
typedef ostringstream OSS;

#define FILE_AS_IN 1

#ifdef FILE_AS_IN
#define OPEN fp = fopen( "A-small-attempt1.in" , "r" ); if ( fp == NULL ) { printf("no input\n"); return -1 ; } ;
#define SC(i) fscanf( fp , "%d", &i)
FILE *fp ;
#else
#define OPEN
#define SC(i) scanf( "%d", &i)
#endif

// END OF MACRO TEMPLATES

int T ;
int N ;

int data[30] ;
int dataShadow[30] ;
int len(0);

int cnt(0) ;

void getVal() {
	len = 0; 
	while(!feof(fp)) {
		char c = fgetc(fp);
		if(c == -1) return ;
		if(c == 13) continue;
		if(c == 10) return ;

		if( c > 47 && c < 58 ) c = c - 48 ;
		if( c > 96 && c < 123 ) c = c - 87 ;

		data[len++] = c ;
	}
}

int tabelka[30] ;
int ileZnakow()
{
	REP(i,30) tabelka[i] = 0;

	REP(i,len) tabelka [ data[i] ] ++ ;

	int suma(0);
	REP(i,30 ) suma += tabelka[i] > 0 ? 1 : 0 ;
	return suma ;
}

long long toVal()
{
	long long result(0);
	int mult(1);
	REP( i,len ) {
		result += data[len-i-1] * mult ;
		mult *= 10 ;
	}
	return result ;
}

map< int , int > mConv ;

int main(int argc, char* argv[])
{
	OPEN;				
	SC(T);				//Scan num of cases
	char c = fgetc(fp);	//skip one

	REP(t,T) {


		getVal();

		//Process data here

		mConv.clear();

		mConv[ data[0] ] = 1 ;
		REP( i , len - 1 ) if ( data[i+1] != data[0] ) { mConv[ data[i+1] ] = 0 ; break ; }
		

		//Present result here

		printf("Case #%d: ",t+1);
		//printf("sc %d\n" , ileZnakow() );

		int n = 2 ;
		REP( i , len )
			if ( mConv.find( data[i] ) == mConv.end() )
				mConv[ data[i] ] = n ++  ;

		int mult = 1 ;

		//for ( map<int,int>::iterator it = mConv.begin() ; it != mConv.end() ; it ++ )
		//	printf( "%x %d," , (*it).first , (*it).second );

		int base( mConv.size() == 1 ? 2 : mConv.size() );
		LL result(0);
		REP( i , len ) {
			result += mConv[ data[len - i-1] ] * mult ;
			mult *= base ;
		}

		printf("%d\n",result);
	}
	//system("pause");
	return 0;
}

