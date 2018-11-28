#include<iostream>
#include<vector>
#include<map>
#include<fstream>
#include<string>
#include<math.h>
#include<queue>
#include<stack>
#include<sstream>
#include<algorithm>
#include<set>
#include<stdio.h>
#include<stdlib.h>

#define vint vector <int>
#define vstring vector <string>
#define np(a) next_permutation(a.begin(),a.end())
#define ff(i,n) for (i=0; i<n; i++)
#define pb(a,b) a.push_back(b)
#define mkp make_pair
#define all(a) a.begin() , a.end()

/*

sort(a.begin(),a.end(),f) for vint a;
sort(a,a+n) for int a[n] where a[0] is smallest;

reverse(a.begin(),a.end()) for vint a;
reverse(a,a+n) for int a[n];

pair <int , string> a;

multiset<int> mymultiset (myints,myints+5);

*/

using namespace std;
typedef __int64 ll;
stringstream ss;

int n , m;
int mp[22][22] , x[22] , y[22];

bool ok(int p) {
	int i , j , e , w , tx , ty , k , t;
	for (i=1; i<=n-p+1; i++)
		for (j=1; j<=m-p+1; j++) {
			memset(x,0,sizeof(x));
			memset(y,0,sizeof(y));
			for (k=1; k<=p; k++) 
				for (e=1; e<=p; e++) {
					x[k]+=mp[i+k-1][j+e-1];
					y[e]+=mp[i+k-1][j+e-1];
				}
			x[1]-=(mp[i][j]+mp[i][j+p-1]);
			x[p]-=(mp[i+p-1][j]+mp[i+p-1][j+p-1]);
			y[1]-=(mp[i][j]+mp[i+p-1][j]);
			y[p]-=(mp[i][j+p-1]+mp[i+p-1][j+p-1]);
			t=0;
			for (k=1; k<=p/2; k++) t+=(x[k]*(k-(p/2+1))+x[p+1-k]*(p/2+1-k));
			if (t==0) {
				for (k=1; k<=p/2; k++) t+=(y[k]*(k-(p/2+1))+y[p+1-k]*(p/2+1-k));
				if (t==0) return true;
			}
		}
	return false;
}

int main() {
	freopen("in.txt" , "r" , stdin);
	freopen("b.txt" , "w" , stdout);
	int i , j , k , tt , ttt , dd , st;
	cin >> tt;
	string s;
	for (ttt=1; ttt<=tt; ttt++) {
		cin >> n >> m >> dd;
		for (i=1; i<=n; i++) {
			cin >> s;
			for (j=1; j<=m; j++) mp[i][j]=s[j-1]-'0';
		}
		st=n;
		if (n>m) st=m;
		for (k=st; k>=3; k--) 
			if (ok(k)) break;
		if (k>=3) printf("Case #%d: %d\n" , ttt , k);
		else printf("Case #%d: IMPOSSIBLE\n" , ttt);
	}
	return 0;
}