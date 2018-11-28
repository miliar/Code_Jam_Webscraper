// task2.cpp : Defines the entry point for the console application.
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

#include <boost/foreach.hpp>

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
#define OPEN fp = fopen( "B-small-attempt2.in" , "r" );
#define SC(i) fscanf( fp , "%d", &i)
FILE *fp ;
#else
#define OPEN
#define SC(i) scanf( "%d", &i)
#endif



// END OF MACRO TEMPLATES

int T ;
int N ;

int data[10] ;
int dataShadow[10] ;
int len(0);

int cnt(0) ;

void getVal() {
	len = 0; 
	while(!feof(fp)) {
		char c = fgetc(fp);
		if(c == -1) return ;
		if(c == 13) continue;
		if(c == 10) return ;
		data[len++] = c - 48 ;
	}
}

int toVal()
{
	int result(0);
	int mult(1);
	REP( i,len ) {
		result += data[len-i-1] * mult ;
		mult *= 10 ;
	}
	return result ;
}
void change( int a , int b ) 
{
	int x = data[a] ;
	data[a] = data[b] ;
	data[b] = x ;
}

int main(int argc, char* argv[])
{
	OPEN;				
	SC(T);				//Scan num of cases
	char c = fgetc(fp);	//skip one

	REP(t,T) {

		int result(0);

		REP( i,10 ) { data[i] = 0 ; dataShadow[i] = 0 ; } ;


		getVal();

		REP( i , len ) dataShadow[i] = data[i] ;

		//Process data here

		int org = toVal() ;
		next_permutation(data,data+len);
		int res = toVal() ;

		if ( res <= org ) { 	
			REP( i,len ) data[i] = dataShadow[i];
								
			len ++ ; 

			while( res <= org ) 
			{
				next_permutation(data,data+len);
				res = toVal() ;
			}			
		} ;
		
		//Present result here

		printf("Case #%d: ",t+1);

		REP( i , len )
			printf("%d",data[i]);

		printf("\n");
	}
	//system("pause");
	return 0;
}

