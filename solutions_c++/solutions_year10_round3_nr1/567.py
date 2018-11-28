#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <map>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <numeric>

#define all(x) x.begin() , x.end()
#define pb(x) push_back(x)
#define sz(x) ((int) x.size())
#define INF 0x7fffffff
#define LL long long
#define LD long double
#define VI vector<int>
#define VS vector<string>

using namespace std;


int n;
struct node
{
	int a,b;
}B[1001];

bool func(node a,node b)
{
	return a.a < b.a;
}

int main()
{
	int Te;
	cin >> Te;
	for(int te=0 ; te<Te  ; te++)
	{
		cout << "Case #"<<te+1 << ": ";
		int res =0 ;
		cin >> n;
		for(int i=0 ; i<n ; i++)
			cin >> B[i].a >> B[i].b;


		sort(B,B+n,func);

		
		for(int i=1 ; i<n ; i++)
			for(int j=0 ; j<i ; j++)
				if(B[j].b > B[i].b)
						res++;

		cout << res << endl;
	}
}
