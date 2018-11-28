#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
using namespace std;
 
typedef vector < int > vi;
typedef vector < string > vs;
typedef vector < bool > vb;
#define FOR(i,q,w) for (int i=q;i<w; i++)
#define PB push_back
#define MP make_pair
const int MOD = 1000000007;
const int INF = 2000000000;
typedef long long ll;

int n,m,t;
int A[1000];

int F(int x, int y)
{
		string s1 = "", s2 = "";
		while (x > 0)
		{
				s1 += (x % 2)+'0';
				x /= 2;
		}
		while (y > 0)
		{
				s2 += (y % 2)+'0';
				y /= 2;
		}
		while (s1.size() != s2.size())
		{
				if (s1.size()<s2.size()) s1 += '0';
				if (s2.size()<s1.size()) s2 += '0';				
		}

		int r = 0, p = 1;

		FOR (i,0,s1.size())
		{
				int f = 0;
				if (s2[i]=='0')
				{
						if  (s1[i]=='1') f = 1;						
				}
				else
				{
						if (s1[i]=='0') f = 1;
				}
				r += p*f;
				p = p*2;
		}
		return r;
}

int main()
{

		cin >> t;

		FOR (tt,0,t)
		{
				cin >> n;
				FOR (i,0,n)
						cin >> A[i];

				int res = -1;

				int s = 0, sum = 0;

				FOR (i,0,n)
				{
						s = s^A[i];
						sum += A[i];
				}

				FOR (i,0,n)
				{
						if (A[i] == F(A[i],s))
						{
								if (A[i] != 0 && sum-A[i] != 0) 
										res = max(res,max(A[i],sum-A[i]));
						}
				}

				cout  << "Case #" << tt+1 << ": ";
				if (res==-1)
						cout << "NO" << endl;
				else
						cout << res << endl;
		}

		cin >> n;
		return 0;
} 
 