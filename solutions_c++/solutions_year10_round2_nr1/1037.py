/*
Author : OmarEl-Mohandes
PROG   : A
LANG   : C++
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
#include <map>
#include <complex>
#include <valarray>
#include <memory.h>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define REP(i,k,m) for(int i=k;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define oo ((int)1e9)

int main()
{
	freopen("A.in" , "rt" , stdin);
	freopen("A.out" , "wt" , stdout);
	int N , M , t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cin >> N >> M;
		set<vector<string> >e , w;
		string t ;
		for (int j = 0; j < N; ++j) {
			cin >> t;
			string tmp = "";
			vs S;
			for (int k = 0; k < t.size(); ++k) {
				if(t[k] == '/' || k == t.size()-1)
				{
					if(k == t.size()-1)tmp += t[k];
					if(tmp != ""){
						S.pb(tmp);
						e.insert(S);
					}
					tmp = "";
				}
				else
					tmp += t[k];
			}

		}
		for (int j = 0; j < M; ++j) {
			cin >> t;
						string tmp = "";
						vs S;
						for (int k = 0; k < t.size(); ++k) {
							if(t[k] == '/' || k == t.size()-1)
							{
								if(k == t.size()-1)tmp += t[k];
								if(tmp != ""){
									S.pb(tmp);
								}
								tmp = "";
							}
							else
								tmp += t[k];
						}
						w.insert(S);
		}
		int res = 0;
		for(set<vector<string> > :: iterator it = w.begin() ; it != w.end() ; it ++)
		{
			vector<string>s = (*it);
			bool f = 1;
			vector<string>tt;
			for (int k = 0; k < s.size(); ++k) {
				tt.pb(s[k]);
				if(e.find(tt) != e.end())continue;
				if(f)
				{
					res += s.size()-k , f = 0;
				}
				e.insert(tt);
			}
		}
		cout << "Case #" << i+1 << ": " << res << endl;
	}
	return 0;
}
