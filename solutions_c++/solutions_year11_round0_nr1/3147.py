#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <stack>

using namespace std;

#define pb push_back
#define mp make_pair
#define fir first
#define fi first
#define sec second
typedef long long int64;
typedef long double ld;

const int inf=2000000000;
const ld eps=1e-07;

int n;
vector < pair<int,int> > a[3];

int main(){
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	int t;
	scanf("%d",&t);
	for (int z=0;z<t;++z){
		a[0].clear();
		a[1].clear();

		scanf("%d",&n);
		for (int i=0;i<n;++i){
			char c;
			int x;
			scanf(" %c %d ",&c,&x);
			if (c=='O')
				a[0].pb(mp(x,i));
			else a[1].pb(mp(x,i));
		}
		int i1=0;
		int i2=0;
		int tek1=1;
		int tek2=1;
		int ans=0;
		while (i1<a[0].size() || i2<a[1].size()){
			++ans;
			if (i1==a[0].size()){
				if (a[1][i2].first==tek2)
						++i2;
				else if (tek2<a[1][i2].first)
						++tek2;
				else if (tek2>a[1][i2].first)
						--tek2;
			}
			else 
				if (i2==a[1].size()){
					if (a[0][i1].first==tek1)
							++i1;
					else if (tek1<a[0][i1].first)
							++tek1;
					else if (tek1>a[0][i1].first)
							--tek1;
				}
				else 
					if (a[0][i1].second>a[1][i2].second){
						if (tek1<a[0][i1].first)
							++tek1;
						else if (tek1>a[0][i1].first)
								--tek1;

						if (a[1][i2].first==tek2)
							++i2;
						else if (tek2<a[1][i2].first)
								++tek2;
						else if (tek2>a[1][i2].first)
								--tek2;
					}
					else {
						if (tek2<a[1][i2].first)
							++tek2;
						else if (tek2>a[1][i2].first)
								--tek2;

						if (a[0][i1].first==tek1)
							++i1;
						else if (tek1<a[0][i1].first)
								++tek1;
						else if (tek1>a[0][i1].first)
								--tek1;
					}
		}
		printf("Case #%d: %d\n",z+1,ans);
	}
	return 0;
}