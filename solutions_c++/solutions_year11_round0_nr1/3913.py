// A.cpp: определ€ет точку входа дл€ консольного приложени€.
//

//#include "stdafx.h"
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
#include <time.h>
#include <sstream>

#define fr(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define fd(i,a,b) for(int i=(int)(a);i>=(int)(b);i--)
#define be(m) (m).begin(),(m).end()
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef double d;

int ri(){int x;scanf("%d",&x);return x;}
d rd(){d x;scanf("%lf",&x);return x;}
ll rll(){ll x;scanf("%lld",&x);return x;}
void wi(int x){printf("%d ",x);}
void wd(d x){printf("%lf ",x);}
void wll(ll x){printf("%lld ",x);}



int main()
{
	//freopen("C:/Users/CleRIC/Desktop/”нивер/acm.timus.ru/input.txt","rt",stdin);
	//freopen("C:/Users/CleRIC/Desktop/”нивер/acm.timus.ru/output.txt","wt",stdout);
	//freopen("input.txt","rt",stdin);
	//freopen("output.txt","wt",stdout);
	int t=ri();
	fr(q,1,t)
	{
		int n=ri();
		vector<int> orange;
		vector<int> blue;
		vector<bool> id(n);
		fr(i,0,n-1)
		{
			string s;
			cin >> s;
			int x=ri();
			if (s=="O")
			{
				orange.pb(x);
				id[i]=true;
			}
			else
			{
				blue.pb(x);
				id[i]=false;
			}
		}
		int time=0;
		int o=0,b=0,x=1,y=1,t=0;
		while(1)
		{
			if (o==orange.size() && b==blue.size())
				break;
			time++;
			bool omg=false;
			if (o<orange.size())
				if (orange[o]==x && id[t])
				{
					o++;
					t++;
					omg=true;
				}
				else
				{
					if (x<orange[o])
						x++;
					else
					if (x>orange[o])
						x--;
				}
			if (b<blue.size())
				if (blue[b]==y && !id[t] && !omg)
				{
					b++;
					t++;
				}
				else
				{
					if (y<blue[b])
						y++;
					else
					if (y>blue[b])
						y--;
				}
		}
		printf("Case #%d: %d\n",q,time);
	}
	return 0;
}

