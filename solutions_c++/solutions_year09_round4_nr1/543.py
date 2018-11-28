#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <queue>
#include <time.h>

using namespace std;

#define RP(a,h) for(int (a)=0; (a)<(h); (a)++)
#define FR(a,l,h) for(int (a)=(l); (a)<=(h); (a)++)
#define INF 2000000000
#define sz size()
#define pb push_back
#define sv(v) sort((v).begin(), (v).end())
#define ABS(x) (((x)>0)?(x):(-(x)))


#define IMAX 30000000

int a[100][100];

int main()
{   
	int t, n;

	string s;
	    
	cin >> t;
	
    RP(test, t)
    {
		cin >> n;
		memset(a, 0, sizeof(a));
		vector<int> v(n, 0);

		RP(i, n)
		{
			 cin >> s;
			 RP(j, n) { a[i][j] = s[j] - '0'; if (a[i][j] == 1) v[i] = j; }
		}
				
		int res = 0;
		RP(i, n)
		{
//			RP(ii, n) { cout << v[ii] << " "; } cout << endl;
			if (v[i] > i)
			{				
//				cout << i << " " << v[i] << endl;
				FR(j, i+1, n-1) 
				{
					if (v[j] <= i)
					{
//						cout << j << " " << v[j] << endl;
						for(int k=j; k>i; k--)
						{
							int tmp = v[k];
							v[k] = v[k-1];
							v[k-1] = tmp;
							res++;
						}
						break;
					}
				}
			}
		}
		
		cout << "Case #" << test+1 << ": " << res << endl;
	}
    
    return 0;
}
