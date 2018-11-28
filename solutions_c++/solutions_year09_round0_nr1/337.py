/*
 * A.cpp
 *
 *  Created on: 03/09/2009
 *      Author: Hamzawy
 */

#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
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
/*#include <ext/hash_map>
 using namespace __gnu_cxx;*/
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)
#define EPS (1e-9)

int l, d, n, K = 0;
vector<vector<char> > build(string str) {
	vector<vector<char> > re;
	for (int i = 0; i < str.sz;)
		if (str[i] >= 'a' && str[i] <= 'z')
			re.pb(vector<char> (1, str[i])), i++;
		else {
			vector<char> t;
			int j;
			for (j = i + 1; str[j] != ')'; j++)
				t.pb(str[j]);
			re.pb(t);
			i = j + 1;
		}
	return re;
}
set<string> se;
int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
	freopen("A-small.out", "wt", stdout);
#endif
	string str;
	cin >> l >> d >> n;
	for (int i = 0; i < d; i++) {
		cin >> str;
		se.insert(str);
	}
	while (n--) {
		cin >> str;
		vector<vector<char> > v = build(str);
		int cnt=0;
		if (v.sz == l)
			for (set<string>::iterator it = se.begin(); it != se.end(); it++) {
				int i;
				for(i=0;i<v.sz;i++)
				{
					bool f1=0;
					for(int j=0;j<v[i].sz;j++)
						if(v[i][j]==it->operator [](i))
						{
							f1=1;break;
						}
					if(!f1)
						break;
				}
				cnt+=(i==v.sz);
			}
		printf("Case #%d: %d\n", ++K, cnt);
		//system("pause");
	}
	return 0;
}

