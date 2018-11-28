#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <stdlib.h>
#include <sstream>
#include <assert.h>

#include <time.h>
#pragma comment(linker, "/STACK:20000000")

#define fr(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define fd(i,a,b) for(int i=(int)(a);i>=(int)(b);i--)
#define mp make_pair
#define pb push_back
#define ll long long

using namespace std;

int ri(){int x;scanf("%d",&x);return x;}
ll rll(){ll x;scanf("%lld",&x);return x;}

string change="yhesocvxduiglbkrztnwjpfmaq";

void solve()
{
	int test=ri();
	map<char,char> st;
	fr(i,0,25)
		st[i+'a']=change[i];
	getchar();
	fr(testing,1,test)
	{
		string s;
		getline(cin,s);
		printf("Case #%d: ",testing);
		fr(i,0,s.length()-1)
			cout << (s[i]==' ' ? s[i] : st[s[i]]);
		cout << endl;
	}
}

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("C:/Users/CleRIC/Desktop/Универ/acm.timus.ru/input.txt","rt",stdin);
		freopen("C:/Users/CleRIC/Desktop/Универ/acm.timus.ru/output.txt","wt",stdout);
	#else
		//freopen("input.in","rt",stdin);
		//freopen("output.out","wt",stdout);
	#endif

	solve();

	///#ifndef ONLINE_JUDGE
	//	printf("\n\ntime-%.3lf",clock()*1e-3);
	//#endif

	return 0;
}