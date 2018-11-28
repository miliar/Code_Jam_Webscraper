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
		int n = GI;
		VI seq(n);
		
		FORZ (i, n)
			seq[i] = GI;

		int maxn = 1 << n, ans = 0;
			
		FORZ (bit, maxn) {
		
			int nb = bit;
			string s;
			
			while (nb) {
				if (nb & 1) 
					s += '1';
				else
					s += '0';
				nb >>= 1;							
			}
			while (s.sz < n)
				s += '0';

			reverse(all(s));
							
			int a = 0, b = 0, sean = 0, pat = 0;
			
			FORZ (i, s.sz) {
				if (s[i] == '1') {
					a ^= seq[i]; 
					sean += seq[i];
				}
				else {
					b ^= seq[i]; 
					pat += seq[i]; 
				}	
			}
			
			//printf ("%s %d %d %d %d\n", s.c_str(), a, b , sean, pat);
			
			if (a > 0 && b > 0 && a == b)
				ans = max (ans, max(sean, pat));
		}
		
		if (ans == 0)
			printf ("Case #%d: NO\n", t + 1);
		else
			printf ("Case #%d: %d\n", t + 1, ans);			
	}
	
	return 0;
}



















