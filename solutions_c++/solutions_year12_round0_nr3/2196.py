#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <utility>
#include <math.h>
#include <cstdlib>
#include <memory.h>
#include <queue>

#define pb push_back
#define i64 long long
#define mp make_pair
#define pii pair <int,int>
#define vi vector <int>
#define vii vector <pii>
#define f first
#define s second
#define foran(i,a,b) for (int i=a;i<(int)b;i++)
#define forn(i,n) for (int i=0;i<(int)n;i++)
#define ford(i,n) for (int i=(int)n-1;i>=0;i--)

const double eps = 1e-9;
const int int_inf = 2000000000;
const i64 i64_inf = 1000000000000000000LL;
const double pi = acos(-1.0);
 
using namespace std;
int tests;
int A[7];
int B[7];
int C[7];
int sz;

int solve(int a,int b)
{
	int aa = a, bb = b;
	int ans = 0;
	int sz = 0;
	while (a != 0) A[sz] = a % 10, sz++,a /= 10;
	reverse(A,A+sz);
	sz = 0;
	while (b != 0) B[sz] = b % 10, sz++, b /= 10;
	reverse(B,B+sz);
	
	for (int i=aa; i<=bb; i++)
	{
		
		int c = i; sz = 0;
		while (c != 0) C[sz] = c % 10, sz++, c /= 10;
		reverse(C,C+sz);
		vector <int> r;
		for (int j=1; j<sz; j++)
		{
			if (C[j] == 0) continue;
			bool oka = 0; bool okb = 0; bool okc = 0;
			int jj = j;
			int it = 0;
			int cc = 0;
			while (it < sz)
			{
				if (!oka) 
                    { if (C[jj%sz] > A[it]) oka = 1; else if (C[jj%sz] < A[it]) break; }
				if (!okb) 
                    { if (C[jj%sz] < B[it]) okb = 1; else if (C[jj%sz] > B[it]) break; }
				if (!okc) 
                    { if (C[jj%sz] > C[it]) okc = 1; else if (C[jj%sz] < C[it]) break; }
				it++; jj++;
			    cc = cc * 10 + C[jj%sz];
			}
			forn(jjj,r.size()) if (r[jjj] == cc) { okc = 0; break; }
			if (sz == it && okc) { ans++; r.pb(cc); }
		}
		
	}
	
	return ans;
}

int main() {
//  freopen("input.txt","r",stdin);
//  freopen("output.txt","w",stdout);
  cin >> tests;
  for (int test=1; test<=tests; test++)
  {
	int a,b; scanf("%d%d",&a,&b);
	printf("Case #%d: %d\n",test,solve(a,b));
  }
  
  return 0;
}