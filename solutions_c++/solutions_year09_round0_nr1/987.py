#include <stdio.h>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <sstream>
#include <cstring>
#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define forv(i,v) for (int i = 0; i < v.size(); i++)
#define fors(i,s) for (int i = 0; i < s.length(); i++)
#define rep(i,f,t) for (int i = (int)(f); i < (int)(t); i++)
#define per(i,f,t) for (int i = f; i > t; i--)
#define fe(it,container) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define all(a) a.begin(),a.end()
#define mp make_pair
#define pb push_back
#define sz size()
#define ft first
#define sd second
#define VI vector< int >
#define VS vector< string >
#define PII pair< int,int >
#define PIS pair< int, string >
#define VPIS vector< PIS >
#define VPII vector< PII >
#define sqr(a) ((a)*(a))
#define cube(a) ((a)*(a)*(a))
#define pname "domino"
#define mod 1000000007LL
#define pi 3.1415926535
#define have(u,v) (u&(1<<v))
#define maxn 50000
#define inf (1<<20)
#define ll long long
using namespace std;
string a[5002];
int l,d,n;
int b[15][26];
int solve() {
	memset(b,0,sizeof(b));
	string u;
	cin >> u;
	
	int i = 0, j = 0;
	while (i < u.sz) {
		if (u[i]=='(') {
			i++;
			while (u[i] != ')') {
				b[j][u[i]-'a']=1;
				i++;
			}
			i++;
		} else {
			b[j][u[i]-'a']=1;
			i++;
		}
		j++;
	}

	int ans=0;
	forn(i,d) {
		int f=1;
		forn(j,l)if (!b[j][a[i][j]-'a']) {
			f=0;
			break;
		}
		ans+=f;
	}

	return ans;
}

int main() {
#ifndef ONLINE_JUDGE
   freopen("input.txt", "rt", stdin);
   freopen("output.txt", "wt", stdout);
#endif	
	cin >> l >> d >> n;
	forn(i,d) {
		cin >> a[i];
	}

	forn(i,n) {
		printf("Case #%d: %d\n",i+1,solve());
	}
	return 0;
}	

