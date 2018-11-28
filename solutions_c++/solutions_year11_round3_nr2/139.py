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

long long vals[1000001];

int main()
{
	int Te;
	cin >> Te;
	for(int te=0 ; te<Te  ; te++)
	{
		cout << "Case #"<<te+1 << ": ";
		long long L,t,N,C;
		long long a[1001];
		long long res = 0;

		cin >> L >> t >> N >> C;
		
		for(int i=0 ; i<C ; i++) cin >> a[i];
		for(int i=0 ; i<N ; i++) vals[i] = a[i%C];

		int k=0;
		res = 0;
		for( ; res + vals[k]*2 <= t && k < N; k++)
			res += vals[k]*2;
		
		if(k < N)
		{
			long long remtime = t - res;
			res += remtime;

			vals[k] -= remtime/2;
			sort(vals+k, vals+N);
			reverse(vals+k, vals+N);

			for( ; k<N ; k++)
			{
				//cout << vals[k] << endl;
				if(L) 
				{
					res += vals[k];
					L--;
				}
				else res += vals[k]*2;
			}
		}
		cout << res << endl;
	}
}
