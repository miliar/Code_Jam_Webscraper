#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <iostream>

using namespace std;
int A, B;


int getLen(int n)
{
	if(n < 10) return 1;
	if(n < 100) return 2;
	if(n < 1000) return 3;
	if(n < 10000) return 4;
	if(n < 100000) return 5;
	if(n < 1000000) return 6;
	return 1;
}

int get10pow(int n)
{
	if(n == 0) return 1;
	if(n == 1) return 10;
	if(n == 2) return 100;
	if(n == 3) return 1000;
	if(n == 4) return 10000;
	if(n == 5) return 100000;
	if(n == 6) return 1000000;
	return 1;
}


int getCount( int n )
{
	int len = getLen(n);
	int ans = 0;
	set<int> visited;
	for( int i = 1; i< len; i++ ) {
		int bt = get10pow(i);
		int m = (n % bt) * get10pow(len-i) + n / bt;
		if( n < m && m <=B && visited.count(m) == 0 ){
			visited.insert(m);
			ans++;
		}
	}
	
	return ans;
}


int solv()
{
	int ans = 0;
	for (int n=A; n<B; n++) {
		ans += getCount(n);
	}
	
	return ans;
}


int main()
{
	FILE *fin = fopen( "../../input.txt", "rt" );
	FILE *fout = fopen( "../../out.txt", "wt" );
	//FILE *fout = stdout;
	
	int tc = 0;
	fscanf( fin, "%d\n", &tc );
	
	for( int i=1; i<=tc; i++ )
	{
		fscanf( fin, "%d %d\n", &A, &B );
		fprintf( fout, "Case #%d: %d\n", i, solv() );
	}
	
    return 0;
}