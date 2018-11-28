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

int res(int A,int B)
{
	int ans=0;
	fr(i,A,B)
	{
		int temp=i;
		vector<int> st;
		while(temp)
			st.push_back(temp%10),temp/=10;
		set<int> hm;
		fr(j,0,(int)st.size()-2)
		{
			if (st[j]==0)
				continue;
			int L=0,R=0;
			fd(k,j,0)
				L*=10,L+=st[k];
			fd(k,st.size()-1,j+1)
				R*=10,R+=st[k];
			fr(k,1,(int)st.size()-j-1)
				L*=10;
			L+=R;
			if (L>i && L<=B && hm.find(L)==hm.end())
				ans++,hm.insert(L);
		}
	}
	return ans;
}

void solve()
{
	int test=ri();
	fr(testing,1,test)
	{
		int a=ri(),b=ri();
		printf("Case #%d: ",testing);
		cout << res(a,b) << endl;
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

	//#ifndef ONLINE_JUDGE
	//	printf("\n\ntime-%.3lf",clock()*1e-3);
	//#endif

	return 0;
}