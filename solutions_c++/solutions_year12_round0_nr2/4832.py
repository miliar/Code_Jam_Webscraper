#pragma comment(linker, "/STACK:256000000")

#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <ctime>
#include <math.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;


template<class T>
double sqrt(T x)
{
	return sqrt((double) x);
}

template<class T>
T sqr (T x)
{
	return x*x;
}


#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define X first
#define Y second
#define pb push_back
#define mp make_pair
//#define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)



const double PI = acos(-1.0);
const int INF = 1000000000;
const int MOD = 1000000007;

struct dr
{	//a / b;
	
	int a,b;
	dr(int _a, int _b)
	{
		a = _a;
		b = _b;
	}
	bool operator<(const dr& c)
	{
		return (a * c.b < b * c.a);
	}
	bool operator<=(const dr& c)
	{
		return (a * c.b <= b * c.a);
	}
};


//#define ONLINE_JUDGE

int main()
{
	double TIME_START = clock();
#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif

	int T;
	cin >> T;

	bool su[35]={0,};
	int mas[35]={0,};
	int mans[35]={0,};

	for (int x = 0 ; x <= 30 ; x++)
	{
		bool sup = 0;
		int cma =-1;
		int no_sup = -1;
		for (int a = 0 ; a <= x ; a++)
			for(int b = 0 ; b + a <= x ; b++)
			{
				int c = x - a - b;
				int ma = max(max(a,b),c);
				int mi = min(min(a,b),c);
				if ( ma - mi > 2 ) continue;
				if ( ma - mi == 2 ) sup = 1;
				if ( cma < ma && ma - mi == 2 ) cma = ma;
				if ( ma - mi != 2 && no_sup < ma ) no_sup = ma;
			}
			su[x] = sup;
			mas[x] = cma;
			mans[x] = no_sup;
	}


	for (int test = 1 ; test <= T ; test++)
	{
		int n,s,p;
		cin >> n >> s >> p;
		vector<int> t(n);
		for (int y = 0 ; y < n ; y++) cin>>t[y];

		sort(t.begin(), t.end());

		int ans = 0;

		for (int y = 0 ; y < n ; y++)
		{
			int v = t[y];

			if ( mans[v] >= p ) ans++;
			else
			if ( s )
			{				
				if ( su[v] == 1 && mans[v] < p && mas[v] >= p) 
				{
					s--;
					ans++;
				}
			} 
				
		}

		printf("Case #%d: %d\n", test,ans);
	}



	
	eprintf("\n\n%.15lf\n\n",(double)(clock() - TIME_START)/CLOCKS_PER_SEC);
	return 0;
}
