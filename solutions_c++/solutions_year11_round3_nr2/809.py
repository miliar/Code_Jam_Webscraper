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
#include <list>  
using namespace std;  

#define PB push_back  
#define MP make_pair  
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v))  
typedef long long ll;  
int max(int ar[],int siz,int exc)
{
	int max = 0;
	int res=0;
	REP(i,siz)
	{
		if (i==exc) continue;
		if(ar[i] > max)
		{
			max = ar[i];
			res = i;
		}
	}
	return res;
}
void run(int casenr) {
	int n,l,c;
	long long T;
	cin>>l;
	scanf("%lld",&T);
	cin>>n>>c;
	int d[c];
	REP(i,c) cin>>d[i];
	int t0 = 0;
	int ans=0;
	REP(i,n) t0+=2*d[i%c];
	if(l == 0) ans = t0;
	else
	{
		int i=0;
		int t1=0;
		while(t1<=T)
		{
			t1 += 2*d[i%c];
			i++;
		}
		i--;
		t1 -= 2*d[i%c];
		if(i>=n) { ans = t0;goto prints;}
		if(l == 1)
		{
			if(n-i>c)
			{
				ans = t0 - d[max(d,c,-1)];
			}
			else
			{
				int nd[c];
				int j = i%c;
				REP(k,j) nd[k]=0;
				nd[j] = d[j] - (T-t1)/2;
				FOR(k,j+1,c) nd[k] = d[k];
				ans = t0 - nd[max(nd,c,-1)];
			}
		}
		else if(l == 2)
		{
			if(n-i>2*c)
			{
				ans = t0 - 2*d[max(d,c,-1)];
			}
			else
			{
				int nd[c];
				int j = i%c;
				REP(k,j) nd[k]=0;
				nd[j] = d[j] - (T-t1)/2;
				FOR(k,j+1,c) nd[k] = d[k];
				if(n-i<=c)
				{
					int tep = max(nd,c,-1);
					ans = t0 - nd[max(nd,c,-1)] - nd[max(nd,c,tep)];
				}
				else
				{
					int tep = max(d,c,-1);
					int m1 = nd[max(nd,c,-1)];
					int m2 = d[max(d,c,tep)];
					int mm = (m1>m2)?m1:m2;
					ans = t0 - d[tep] - mm;
				}
				// ans = t0 - nd[max(nd,c,-1)];
			}
		}
		else cout<<"Cheaters\n";
	}
	prints: cout<<"Case #"<<casenr<<": "<<ans<<endl;
}

int main() {
	int n; cin>>n; FORE(i,1,n) run(i);
	return 0;
}

 
