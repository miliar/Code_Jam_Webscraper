//SkyHawk, CMC MSU

#include <stdio.h>
#include <iostream>
#include <list>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <set>

using namespace std;

#define FOR(i,n) for(int i = 0;i < n;++i)
#define PII pair<int,int>
#define EPS 1e-9

int dyn[10010];
int may[10010];
int d[10010];
int l[10010];

int main(int argc, char** argv)
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin >> t;
	FOR(count,t)
	{
		int n;
		cin >> n;
		memset(dyn,0,sizeof(dyn));
		memset(may,0,sizeof(may));
		FOR(i,n)
			cin >> d[i] >> l[i];
		cin >> d[n];
		l[n] = 0;
		++n;
			if(l[0]>=d[0])
			{
				may[0] = 1;
				dyn[0] = max(dyn[0],d[0]);
			}
		FOR(i,n)
			if(may[i])
				for(int j = i+1;j<n;++j)
					if(d[j]<=d[i]+dyn[i])
					{
						may[j] = 1;
						dyn[j] = max(dyn[j],min(d[j]-d[i],l[j]));
						//cerr << j << " " << dyn[j] << endl;
						
					}
		if(may[n-1])
			cout << "Case #" << count+1 << ": " << "YES" << endl;
		else
			cout << "Case #" << count+1 << ": " << "NO" << endl;
	}
	return 0;
}
