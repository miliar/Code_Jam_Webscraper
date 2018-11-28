#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <string>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cctype>
#define f(i,x,y) for (int i = x; i <y; i++)
#define fd(i,x,y) for (int i = x; i >=y; i--)
#define FOR(it,A) for (typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define clr(A,x) memset (A, x, sizeof A)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define oo (1<<30)
#define eps (1e-9)
#define vint vector<int>
#define pb push_back
#define pii pair<int,int>
#define fst first
#define snd second
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define debug(x) cout << #x << " = " << x << endl
#define adebug(x,n) cout << #x << "[]"<<endl; f(i,0,n)cout<<x[i]<<char(i+1==n? 10 : 32)
#define mdebug(x,m,n) cout << #x << "[]"<<endl; f(j,0,m)f(i,0,n)cout<<x[j][i]<<char(i+1==n? 10 : 32)
#define MAX 10005
typedef long long ll;
using namespace std;

int T,n;
int d[MAX], len[MAX], D;
int g[MAX];
int caso;

int main(){
	cin >> T;
	while (T--){
		cin >> n;
		f(i,1,n+1) scanf ("%d%d", d+i, len+i);
		scanf ("%d", &D);
		d[0] = 0; len[0] = d[1];
		n = n+2;
		d[n-1] = D;
		g[n-1] = 0;
		fd(j,n-2,0){
			g[j] = oo;
			for (int k = j+1; k<n && d[k] <= d[j] + len[j]; k++){
				if (d[k]-d[j]>=g[k]) g[j] = d[k]-d[j], k = n;
			}
		}
		printf ("Case #%d: %s", ++caso, g[0]==oo? "NO" : "YES");
		putchar(10);
	}
}

