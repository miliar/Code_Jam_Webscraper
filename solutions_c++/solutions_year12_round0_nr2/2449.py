#include <iomanip>
#include <numeric>
#include <functional>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <cctype>
#include <sstream>
#include <map>
#include <set>
#include <cstdio>
#include <queue>
#define f(i,x,y) for(int i=x;i<y;i++)
#define fd(i,y,x) for(int i=y;i>=x;i--)
#define FOR(it,A) for( typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define impr(A) for( typeof A.begin() chen = A.begin(); chen !=A.end(); chen++ ) cout<<*chen<<" "; cout<<endl
#define ll long long
#define vint vector<int>
#define clr(A,x) memset(A,x,sizeof(A))
#define CLR(v) f(i,0,n) v[i].clear()
#define oo (1<<30)
#define ones(x) __builtin_popcount(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define pb push_back
#define eps (1e-9)
#define cua(x) (x)*(x)
using namespace std;

int T,n,s,p;
int t[105];
int lo[31], hi[31];
bool orden (int i, int j){ return lo[i] > lo[j]; }

int main()
{
	clr (hi, -1);
	f(k,0,31){
		lo[k] = (k+2) / 3;
		int pri = floor (k-2)/3, ter = pri+2;
		if (pri>=0 && ter<=10) hi[k] = ter;
	}

	cin >> T;
	f(caso,0,T){
		printf ("Case #%d: ", caso+1);
		cin >> n >> s >> p;
		f(i,0,n) cin >> t[i];
		int aumentables = 0;
		int arr[n];
		vint v;
		f(i,0,n) arr[i] = lo[t[i]];
		f(i,0,n) if (2<=t[i] && t[i]<=28 && t[i]%3!=1 && arr[i]==p-1) v.pb (i);
		sort (all(v), orden);
		s = min (s,(int) v.size());
		f(j,0,s) arr[v[j]]++;
		int res = 0;
		f(i,0,n) if (arr[i] >= p) res++;
		cout << res << endl;
	}
}

