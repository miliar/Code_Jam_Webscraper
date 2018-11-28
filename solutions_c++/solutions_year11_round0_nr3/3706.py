// C.cpp: определ€ет точку входа дл€ консольного приложени€.
//

#include "stdafx.h"
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
	freopen("C:/Users/CleRIC/Desktop/”нивер/acm.timus.ru/input.txt","rt",stdin);
	freopen("C:/Users/CleRIC/Desktop/”нивер/acm.timus.ru/output.txt","wt",stdout);
	//freopen("input.txt","rt",stdin);
	//freopen("output.txt","wt",stdout);
	int t=ri();
	fr(q,1,t)
	{
		int n=ri();
		vector<int> mas(n);
		fr(i,0,n-1)
			mas[i]=ri();
		sort(mas.rbegin(),mas.rend());
		int x=mas[0];
		fr(i,1,n-1)
			x=x^mas[i];
		printf("Case #%d: ",q);
		if (x)
			printf("NO");
		else
		{
			ll sum=0;
			fr(i,0,n-2)
				sum+=mas[i];
			printf("%lld",sum);
		}
		printf("\n");
	}
	return 0;
}
