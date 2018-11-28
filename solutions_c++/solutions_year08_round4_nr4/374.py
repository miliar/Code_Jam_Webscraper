#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <string>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define iss istringstream
#define oss ostringstream
#define prv(vec) {for(int zz = 0; zz < vec.size(); ++zz) cout << vec[zz] << " "; cout << endl;}
#define sz(a) ((a).size())
#define len(a) ((a).length())
#define all(c) (c).begin(),(c).end() 
#define forn(i,a,n) for(int i = (int) a; i < (int)n; i++) 

int a[5];
char s[10000],t[10000];

int main()
{
	freopen("d2.in","rt",stdin);
    freopen("d2.out","wt",stdout); 
	int T,n;
	cin >> T;
	forn(x,0,T)
	{
		cin >> n;
		scanf("%s",&s);
		forn(i,0,n) a[i] = i;
		int len = strlen(s);
		int tm = len;
		do
		{
			int ost = 0;
			forn(i,0,len)
			{
				t[i] = s[i - ost + a[ost] ];
				ost++;
				if ( ost == n ) ost = 0;
			}
			int res = 1;
			forn(i,1,len) if ( t[i] != t[i-1] ) res++;
			if ( res < tm ) { tm = res; //forn(i,0,n) cout << a[i]; 
			}
		}while ( next_permutation(a,a+n) );
		cout << "Case #" << x+1 <<": " << tm << endl;
		//printf("Case #%d: %lld\n",t+1,ts);
	}
    return 0;
}