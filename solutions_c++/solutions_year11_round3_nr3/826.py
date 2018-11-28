#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
using namespace std;

#define GI ({int t ;scanf("%d",&t);t;})
#define FORZ(i,n) for(typeof(n)i=0;i<n;i++)
#define all(x) (x).begin(), (x).end()
#define PB push_back
#define sz size()
#define FF first
#define SS second
#define pr(x) cout<<#x<<" : "<<x<<endl<<flush; 
typedef vector<int> VI;
typedef long long LL;
typedef unsigned long long uLL;
typedef pair<int,int> pII;
typedef pair<string,int> pSI;
typedef map<int,int> mII;
typedef map<string,int> mSI;
typedef vector<string> VS;

int main ()
{
	int T = GI;
	
	FORZ (t, T) {
		int n, l, h;
		cin >> n >> l >> h;
		
		int note[n];
		FORZ (i, n)
			cin >> note[i];
		
		int freq = -1;	
		for (int f = l ; f <= h ; f ++)
		{
			bool can = true;
			FORZ (i, n) {
				if (f % note[i] != 0 && note[i] % f != 0)
					can = false;
			}
			if (can)
			{
				freq = f;
				break;
			}
		}
		
		if (freq == -1)
			printf ("Case #%d: NO\n", t + 1);	
		else	
			printf ("Case #%d: %d\n", t + 1, freq);		
	}
	
	
	
	return 0;
}


