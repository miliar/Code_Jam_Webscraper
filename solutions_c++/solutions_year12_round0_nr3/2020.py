/*
  Problem No : 
  Author     : Debashis Maitra
  Complexity :
  Date       :
*/

#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <ctype.h>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <sstream>

using namespace std;

#define CLR(x) memset((x),0,sizeof(x))
#define pb push_back
#define sz size()
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORALL(i,x) for(int i=0;i<x.size();i++)
#define FORALLR(i,x) for(int i=x.size()-1;i>=0;i--)
#define SWAP(x,y) (x)+=(y);y=(x)-(y);x=(x)-(y);
#define lint long long
#define MAX 1000
#define INF 1<<30

typedef vector<int> vi;
typedef vector<string> vs;

int cases,caseno;
int a,b;
//int used[1001][1001];
map< pair<int,int>, bool > used;

int getDigitNo( int n)
{
	if( !n) return 1;
	return log10( n*1.0 ) + 1;
}
int rotateNumber(int n, int part)
{
	int ret;
	int x =  pow( 10.0, part);
	ret =  (n % x) * ((int)pow( 10.0,(getDigitNo(n) - part ))) + (n/x);
	return ret;

}
bool checkUsed(int a,int b)
{
	if(a>b)swap(a,b);
	pair<int,int> pr = make_pair(a,b);
	if( used.find(pr) != used.end() )return true;
	used[pr] = true;
	return false;
}
int getCount(int x)
{
	int cnt = 0;
	int dig = getDigitNo( x );
	for( int i = 1; i < dig; i++ )
	{
		int newNum = rotateNumber( x, i);		
		if( newNum == x ) continue;
		if( newNum > b || newNum < a) continue;
		if( checkUsed(newNum,x) )continue;
		
		cnt++;
	}
	return cnt;
}
void process()
{
	cin >> a >> b;
	used.clear();
	//used[a] = used[b] = 1;
	int res = 0;
	for(int i = a; i <= b; i++ )
	{
		res += getCount( i );

	}
	cout <<"Case #"<< (++caseno)<< ": "<< res << endl;
}
int main()
{
	//cout << rotateNumber( 1234, 2 ) << endl;
	//return 0;
	freopen("input.txt","r",stdin);
	freopen("outputC.txt","w",stdout);
	cin >> cases;
	while( cases-- )
	{
		process();
	}
}