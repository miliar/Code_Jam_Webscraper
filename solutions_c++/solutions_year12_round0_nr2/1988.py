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
int N,S,P;
int t[200];
bool isSurprise(int a, int b, int c)
{
	int maxDiff = 0;
	maxDiff = max( maxDiff, c-b);
	maxDiff = max( maxDiff, c-a);
	maxDiff = max( maxDiff, b-a);
	if( maxDiff == 2 ) return true;
	return false;
}
bool Check(int a[],int x, int next )
{
	int rest = x - P;
	a[0] = P;
	a[1] = next;
	a[2] = rest - a[1];
	if( a[0] < 0 || a[1] < 0 || a[2] < 0) return false;

	sort(a,a+3);
	if( (a[2] - a[0]) > 2 ) return false;
	
	if( isSurprise(a[0], a[1], a[2] ) && S <= 0 ) return false;
	return true;
	
}
bool checkCanMax(int x)
{
	if( (x/3) >= P) return true;
	int a[4];
	
	if ( Check( a, x, P-1) == true ) 
	{
		if( isSurprise(a[0], a[1], a[2] ) == false ) return true;
		else
		{
			if ( Check( a, x, P-2) == true ) 
			{
				if( isSurprise(a[0], a[1], a[2] ) ) S--;
				return true;
			}
			S--; 
			return true;
		}
	}
	if ( Check( a, x, P-2) == true ) {
		if( isSurprise(a[0], a[1], a[2] ) ) S--;
		return true;
	}
	//if( isSurprise(a[0], a[1], a[2] ) ) S--;
	return false;
}
void process()
{
	int cnt = 0;
	FOR(i , N)
	{
		cin >> t[i];
	}
	sort(t, t+N,greater<int>());
	FOR(i,N)
	{
		if( checkCanMax(t[i] ))  cnt++;
	}
	cout << "Case #" << (++caseno) << ": " << cnt << endl;
}
int main()
{
	freopen("input.txt","r", stdin);
	freopen("outputB.txt", "w", stdout);
	cin >> cases;
	while( cases-- )
	{
		cin >> N >> S >> P;
		process();
	}
}