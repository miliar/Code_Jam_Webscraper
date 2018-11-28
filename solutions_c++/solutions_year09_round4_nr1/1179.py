// cheburashka, bear-mouse, team template

#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <stack>
#include <cmath>
#include <queue>
#include <set>
#include <cstring>
using namespace std;

#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long ll;
typedef vector < string > vs;
typedef vector <int> vi;

ifstream inp("A.in");
ofstream out("A.out");

//string split given string a and delimiters
vs strsp(string a, string delim=" ")
{
  vs ret;
  string cr = "";
  for(int i = 0; i < a.size(); i++)
  {
    if(delim.find(a[i])==string::npos) cr += a[i];
    else { if(cr.size()) ret.push_back(cr); cr = ""; }
  }
  if(cr.size()) ret.push_back(cr);
  return ret;
}

int N;
set<vs> vst;
int ql, qr;
vector<vs > que;
vi que_d;

int is_ok(vs &a) {
	for (int i = 0; i < N; i++) {
		for (int j = i + 1; j < N; j++) {
			if (a[i][j] == '1') return false;
		}
	}
	return true;
}

int solve(vs start) {
	ql = 0;
	qr = 0;
	que.clear();
	que.pb(start);
	que_d.clear();
	que_d.pb(0);
	qr = 1;

	int res = 0;
	if (is_ok(start)) {
		return 0;
	}

	while (ql < qr) {
		vs cur = que[ql];
		int cur_d = que_d[ql++];

		for (int i = 0; i < N - 1; i++) {
			swap(cur[i], cur[i + 1]);
			if (vst.find(cur) == vst.end()) {
				if (is_ok(cur)) {
					return cur_d +1;
				}
				vst.insert(cur);
				que.pb(cur);
				que_d.pb(cur_d + 1);
				qr++;
			}
			swap(cur[i], cur[i + 1]);
		}
	}
	// should not happen
	return -1;
}

int main()
{
	int NT;
	inp >> NT;

	for (int nt = 1; nt <= NT; nt++) {
		vst.clear();
		inp >> N;
		vs start(N);
		for (int i = 0; i < N; i++) {			
			inp >> start[i];
		}

		int ans = solve(start);

		out << "Case #" << nt << ": " << ans << endl;
	}

	inp.close();
	out.close();
	return 0;
}
