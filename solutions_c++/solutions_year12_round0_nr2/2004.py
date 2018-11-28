#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <deque>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <sstream>

#define For(i,a,n) for(int i =a ; i < n ; ++i )
#define all(x) (x).begin(),(x).end()
#define n(x) (int)(x).size()
#define pb(x) push_back(x)

using namespace std;
typedef pair<int,int> pii;
const int maxn = 110;
int t;
int n;
int s;
int p;
int su[maxn];
int cnb;
int hv;

int main()
{
	ios::sync_with_stdio(false);
	cin >> t;
	For(it,0,t)
	{
		cin >> n >> s >> p ;
		int ans = 0;
		cnb =0;
		hv = 0;
		For(i,0,n)
		{
			cin >> su[i];
			if((su[i]+2)/3 >= p)
			{
//				cerr << su[i] << endl;
				if(su[i] > 1 && su[i] < 29)
					cnb ++;
				else
					ans ++;
				continue;
			}
			if( su[i]%3 == 1)
				continue;
			if( su[i]%3 == 2)
				if(su[i]/3+2 >= p)
				{
					hv++;
					continue;
				}
			if( su[i]%3 == 0 && su[i] > 0)
				if(su[i]/3+1 >= p)
				{
					hv++;
					continue;
				}
				
		}
		cout << "Case #"<<it+1 << ": " <<ans+cnb+min(s,hv) << endl; 
//		cerr << ans << " " << cnb << " " << s << " " << hv << endl;
	}
	return 0;
}
