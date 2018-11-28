// A.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <ctime>
#include <cstdio>
#include <memory>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <utility>
#include <iterator>
#include <bitset>
#include <sstream>
#include <numeric>

#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
#define LL long long
#define ULL unsigned LL
#define VI vector<int>
#define X first
#define Y second
#define sz(_v) ((int)_v.size())
#define all(_v) (_v).begin(),(_v).end()
#define FOR(i,a,b) for (int i(a); i<=(b); ++i)
#define rep(i,a) FOR(i,1,a)
#define rept(i,a) FOR(i,0,(int)(a)-1)
#define x1 X1
#define y1 Y1
#define sqr(a) ((a)*(a))
#define INF 2000000000
#define PI 3.141592653589
#define eps 0.00000001
#define MOD 1000000007
#define PRIME 1000003

using namespace std;
int f(int n, int t,int p,int &s)
{
	if (t<p) return 0;
	if (t/n>=p) return 1;
	else
	{
		int temp=(t-p)/(n-1);
		if (temp+1==p) return 1;
		else 
			if (s!=0)
				if (temp+2==p)
				{
					s--;
					return 1;
				}
				else return 0;
			else return 0;
	}
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int tests;
	cin>>tests;
	rep(test,tests)
	{
		int n,s,p,counter=0;
		cin>>n>>s>>p;
		rept(i,n)
		{
			int temp;
			cin>>temp;
			counter+=f(3,temp,p,s);
			
		}
		printf("Case #%d: %d\n",test,counter);

	}
	return 0;
}

