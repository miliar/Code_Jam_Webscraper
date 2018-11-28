#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

int cnt;
map<string,int> s2i;
map<int,string> i2s;

int str2int(const string& s) {
	if (s2i.count(s)) return s2i[s];
	s2i[s]=cnt;
	i2s[cnt]=s;
	return cnt++;
}
int N;

const int MAX=400;
typedef pair<int,int> pii;
vector<pii> v[MAX];
const int INF=1<<29;


void insert(vector<pii>& cur, int k) {
	cur.insert(cur.end(),v[k].begin(), v[k].end());
}

const int GOAL=10000;

int go(int s0, int s1=-1, int s2=-1) {
	//printf("TRYING %d %d %d\n", s0, s1, s2);
	vector<pii> cur;
	insert(cur,s0);
	if (s1!=-1) insert(cur,s1);
	if (s2!=-1) insert(cur,s2);
	sort(cur.begin(),cur.end());

	//printf("SIZE: %d\n", cur.size());

	int at = 1;
	int maxv = -INF;
	int ans = 0;
	for (int i=0;i<cur.size();++i) {
		int st = cur[i].first;
		int end = -cur[i].second;
		//printf("I: %d, AT: %d, ST: %d, END: %d\n", i, at, st, end);
		if (end<=at) continue;
		if (st>at) {
			if (maxv+1<st) return INF;
			++ans;
			at = maxv;
			maxv = -INF;
		}
		if (end>at) maxv=max(maxv,end);
		if (at>=GOAL) return ans;
	}
	if (at>=GOAL) return ans;
	if (maxv>=GOAL) return ans+1;
	return INF;
}

int main() {
	int NCASES;
	cin >> NCASES;
	for (int z=1;z<=NCASES;++z) {
		cnt=0;
		s2i.clear();
		i2s.clear();

		cin >> N;
		for (int i=0;i<N;++i) v[i].clear();

		for (int i=0;i<N;++i) {
			string s;
			int a,b;
			cin >> s >> a >> b;
			int u = str2int(s);
			v[u].push_back(make_pair(a,-b));
			//cout << "PUSHING " << u << " " << a << " and " << -b << endl;
		}
		for (int i=0;i<cnt;++i) sort(v[i].begin(),v[i].end());
		
		int minv=INF;

		for (int i=0;i<cnt;++i)
			minv = min(minv, go(i));

		for (int i=0;i<cnt;++i)
			for (int j=i+1;j<cnt;++j)
				minv = min(minv, go(i,j));

		for (int i=0;i<cnt;++i) {
			for (int j=i+1;j<cnt;++j) {
				for (int k=j+1;k<cnt;++k) {
					minv = min(minv, go(i,j,k));
				}
			}
		}
		printf("Case #%d: ",z);
		if (minv>=INF) printf("IMPOSSIBLE\n");
		else printf("%d\n", minv);
	}
}
