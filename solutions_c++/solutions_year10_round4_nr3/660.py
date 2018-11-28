#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <algorithm>
#include <memory.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,k,n) for(int i=(k); i<=(n); i++)
#define DFOR(i,k,n) for(int i=(k); i>=(n); i--)
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a, 0, sizeof(a))

#define LL long long
#define VI  vector<int>
#define PAR pair<int ,int>
#define o_O 1000000000 
void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}

int R;

int sol()
{
	set< PAR > S1;
	set< PAR > S2;
	set< PAR > S3;
	int X1, Y1, X2, Y2;
	FOR(a,1,R)
	{
		cin >> X1 >> Y1 >> X2 >> Y2;
		FOR(b,X1,X2)
			FOR(c,Y1,Y2)
				S1.insert(make_pair(b,c));
	}

	int ans=0;
	while(SZ(S1))
	{
		/*FOR(a,1,10)
		{
			FOR(b,1,10) cout << (S1.find(make_pair(a,b))!=S1.end()?1:0);
			cout << "\n";
		}*/
		//cerr << SZ(S1) << "\n";
		S2.clear();
		S3.clear();
		set< PAR >::iterator it;
		for (it=S1.begin(); it!=S1.end(); it++)
			if (S1.find(make_pair(it->first-1, it->second+1))!=S1.end() &&
				S1.find(make_pair(it->first, it->second+1))==S1.end())
				S2.insert(make_pair(it->first, it->second+1));
		for (it=S1.begin(); it!=S1.end(); it++)
			if (S1.find(make_pair(it->first-1, it->second))==S1.end() &&
				S1.find(make_pair(it->first, it->second-1))==S1.end())
					S3.insert(make_pair(it->first, it->second));
		for (it=S3.begin(); it!=S3.end(); it++)
			S1.erase(*it);
		for (it=S2.begin(); it!=S2.end(); it++)
			S1.insert(*it);
		ans++;
	}
	return ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	FOR(z,1,t)
	{
		cerr << z << "\n";
		cin >> R;
		cout << "Case #" << z << ": " << sol() << "\n";
	}
	return 0;
}