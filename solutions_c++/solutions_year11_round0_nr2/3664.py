#include <iostream>
#include <cstring>
#include <string.h>
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
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define SZ(v) (int)v.size()

#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;

const int oo = (int) 1e9;
const double PI = 3.141592653589793;
const double eps = 1e-11;



#define _small_
//#define _large_
int main() {

#ifdef _small_
	freopen("B-small.in", "rt", stdin);
#endif
#ifdef _large_
	freopen("B-large.in", "rt", stdin);
#endif
	freopen("B.out", "wt", stdout);

	//-----------------------
	//map<pair<char,char>,char > comb;
	char comb[300][300];
	//map<char,char> rev;
	char rev[300];
	int T,C,D,N;
	cin >> T;
	string str ;
	vector<char> st;
	for (int tt = 1; tt <= T; ++tt) {
		st.clear();
//		rev.clear();
//		comb.clear();
		memset(rev, 0, sizeof rev);
		memset(comb, 0, sizeof comb);

		cin >> C;
		for (int i = 0; i < C; ++i) {
			cin >> str;
			comb[str[0]][str[1]] = str[2];
			comb[str[1]][str[0]] = str[2];
		}
		cin >> D;
		for (int i = 0; i < D; ++i) {
			cin >> str;
			rev[str[0]] = str[1];
			rev[str[1]] = str[0];
		}
		cin >> N >> str;
		st.push_back(str[0]);
		for (int i = 1; i < N; ++i) {
			char tmp ;
			if(tmp = comb[st.back()][str[i]])
			{
				st.pop_back();
				st.push_back(tmp);
				continue;
			}
			if(find(st.begin(),st.end(),rev[str[i]]) != st.end())
			{
				st.clear();
				continue;
			}
			st.push_back(str[i]);
		}

		printf ("Case #%d: [",tt);

		for (int i = 0; i < SZ(st); ++i) {
			cout<<st[i];
			if(i != SZ(st)-1)
				cout<<", ";
		}
		cout<<"]\n";
	}

	return 0;
}
