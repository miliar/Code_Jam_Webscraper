/*
 Author: Mohamed Naguib
 Language: C++
 */
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>

using namespace std;

#define pb push_back
#define all(v)              v.begin(),v.end()
#define sz              size()
#define rep(i,m)        for(int i=0;i<m;i++)
#define REP(i,k,m)      for(int i=k;i<m;i++)
#define mem(a,b)        memset(a,b,sizeof(a))
#define mp              make_pair

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;

#define OO ((int)1e9)
#define MAX 100000

int main() {
    freopen ("B-large.out","w",stdout);
    freopen ("B-large.in","r",stdin);
	int t;
	cin >> t;
	int n, S, P;
	int l = 1;
	while (t--) {
		cin >> n >> S >> P;
		vi v(n);
		rep(i,n)
			cin >> v[i];
		int res = 0;
		rep(i,v.sz) {
			if(v[i]==0&&P!=0)
							continue;
			if(v[i]==0&&P==0){
				res++;continue;
			}
			int a = v[i] / 3;
			int b = v[i] % 3;
			if (b == 1) {
				if (a + b >= P)
					res++;
			}
			if (b == 0) {
				if (a >= P) {
					res++;
					continue;
				}
				if (a + 1 >= P && S)
					res++, S--;
			}
			if (b == 2) {
				if (a + 1 >= P) {
					res++;
					continue;
				} else if (a + 2 >= P && S) {
					res++, S--;
				}
			}


		}
		cout << "Case #" << l << ": " << res << endl;
		l++;

	}
}

