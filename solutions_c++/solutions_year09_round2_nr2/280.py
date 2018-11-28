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
#define pi 3.1415926535
#define have(u,v) (u&(1<<v))
#define maxn 50000
#define inf (1<<20)
#define ll long long
#define maxnm 105
using namespace std;

void solve() {
	string u;
	cin >> u;
	if (next_permutation(all(u))) {
		cout<< u << endl;
		return;
	}
	sort(all(u));
	u = "0" + u;
	int i = 0;
	while (i < u.sz && u[i] == '0')i++;
	swap(u[i],u[0]);
	cout<< u << endl;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	forn(i,t) {
		printf("Case #%d: ",i+1);
		solve();
	}
	return 0;
}	

