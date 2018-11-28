#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

using namespace std;

#define MAX(a,b) ((a>=b)?a:b)
#define MIN(a,b) ((a<=b)?a:b)
#define ABS(a) ((a<0)?-(a):a)
#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define FORD(i,a,b) for (int i=(a);i>(b);--i)
#define VVI vector < vector <int> >
#define VI vector <int>
#define LL long long
#define U unsigned
#define pi 3.14159265358979323846264

bool chk(int n,int k)
{
	bool small[11]; 
	bool sch[11]; 
	bool power[11];
	
	bool tr=true;
	
	FOR(i,0,11) small[i]=false;
	FOR(i,0,11) power[i]=false;
	small[0]=true; 
	power[0]=power[1]=true;
	
	FOR(i,0,k)
	{
		FOR(j,0,11) sch[j]=false;
		FOR(j,1,n+1)
		{
			if (power[j]) sch[j]=true;
		}
        
		FOR(j,0,11) if (sch[j]) small[j]=!small[j];
	    FOR(j,2,11) power[j]=false;
		FOR(j,2,11) if (small[j-1]) power[j]=true; else break;

	}
	
	FOR(j,1,n+1)
		if (!small[j]) tr=false;
	return tr;
}

int main()
{
freopen("a.in","r",stdin);
freopen("a.out","w",stdout);
int t,n,k;
cin >> t;
	FOR(i,1,t+1)
	{
	cin >> n >> k;
	if (chk(n,k))
	cout << "Case #"<< i <<": ON" << endl;
	else 
    cout << "Case #"<< i <<": OFF" << endl;
	}
return 0;
}