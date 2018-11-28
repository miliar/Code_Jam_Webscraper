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
#include <queue>
#include <time.h>
#include <stdio.h>

using namespace std;

#define RP(a,h) for(int (a)=0; (a)<(h); (a)++)
#define FR(a,l,h) for((a)=(l); (a)<=(h); (a)++)
#define INF 2000000000
#define sz size()
#define pb push_back
#define sv(v) sort((v).begin(), (v).end())
#define ABS(x) (((x)>0)?(x):(-(x)))

int n;
string s;
string s1 = "welcome to code jam";
int lookup[502][27];
int a[502][20];

int cal(int p1, int p2)
{
	//cout << p1 << " " << s1[p2] << " " << lookup[p1][s1[p2]-'a'] << endl;
	if (p1 >= s.sz) return 0;
	if (p2 >= s1.sz) return 1;
	int& res = a[p1][p2];
	
	if (res != -1) return res;
	
	res = 0;
	int pos = lookup[p1][s1[p2]-'a'];
	while(pos < s.sz && pos != -1)
	{
		if (p2 == s1.sz - 1) res++;
		else res+=cal(pos+1, p2+1);
		if (pos == s.sz-1) break;
		else pos = lookup[pos+1][s1[p2]-'a'];		
	}
	res %= 10000;
	return res;
}

int main()
{
	cin >> n;
	getline(cin, s);
	RP(i, s1.sz) if (s1[i] == ' ') s1[i] = 'z'+1;
	RP(test, n)
	{
		getline(cin, s);
		
		memset(lookup, -1, sizeof(lookup));
		RP(i, s.sz)
		{
			if (s[i] == ' ') s[i] = 'z'+1;
			int t = i;
			while(t >= 0 && lookup[t][s[i]-'a'] == -1) { lookup[t][s[i]-'a'] = i; t--; }
		}
		
		memset(a, -1, sizeof(a));
		printf("Case #%d: %04d\n", test+1, cal(0, 0));
	}
}
