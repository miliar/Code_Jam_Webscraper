#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;



int main()
{
    freopen("a.in","rt",stdin);
    freopen("a.out","wt",stdout);
    
	long long ttt,www = 1;
	cin >> ttt;
	long long n,k,b,t;
	while(ttt--)
	{
		double x[10000];
		double v[10000];
		cin >> n >> k >> b >> t;
		for(int i = 0; i < n; i++)
			cin >> x[i];
		for(int i = 0; i < n; i++)
			cin >> v[i];
		long long res = 0,swaps = 0;
		for(int i = n - 1; i >= 0; i--)
		{
			if( ((double)b - x[i])/v[i] <= t)
			{
				double t1 = ((double)b - x[i])/v[i];
				res++;
				for(int j = i + 1; j < n; j++)
				{
					double ts = ((double)b - x[j])/v[j];
					if(t1 < ts && ts > t)
						swaps++;
				}
				if(res >= k) break;
			}
		}
		if(res >= k)
		cout << "Case #"<< www <<": " << swaps << endl;
		else
		cout << "Case #"<< www <<": IMPOSSIBLE\n";
		www++;
	}


     return 0;
}
