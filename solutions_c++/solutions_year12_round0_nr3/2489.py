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

int T;
int a,b;
int V[8]; int tam = 0, m = 0;
int s[8], t[8];
int comp (int A[8], int B[8], int k){
	fd(i,k-1,0) if (A[i]!=B[i]) return A[i] < B[i]? -1 : 1;
	return 0;
}

int main()
{
	ios_base::sync_with_stdio (0);
	cin >> T;
	f(caso,0,T){
		cout << "Case #" << caso+1 << ": ";
		cin >> a >> b;
		int B[8];
		int bb = b;
		m = 0; for (; b; b/=10) B[m++] = b%10;
			
		int res = 0;
		f(x,a,bb+1){
			tam = m = 0;
			int N = x;
			for (; N; N/=10) s[m++] = N%10;
			f(i,1,m)if (s[i-1]){
				int sz = 0;
				f(j,i,m) t[sz++] = s[j];
				f(j,0,i) t[sz++] = s[j];
//				f(j,0,m) cout << t[j]; cout << endl;		
//				f(j,0,m) cout << s[j]; cout << endl << endl;
				if (comp (s, t, m)<0 && comp (t, B, m)<=0){
					int num = 0;
					fd(i,m-1,0) num = 10*num + t[i];
					V[tam++] = num;
				}
			}
			sort (V, V+tam);
			int add = unique (V, V+tam) - V;
			res += add;
//			if (add) cout << x << " " << add << endl;
		}
		cout << res << endl;
	}
}

