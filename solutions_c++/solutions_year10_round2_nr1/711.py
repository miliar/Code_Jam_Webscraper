using namespace std;

#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <cmath>
#include <queue>
#define FOR(i,a,n) for(int i=a; i<n; i++)
#define REP(i,n) FOR(i,0,n)
#define MAX 1000
#define GI ({int _; scanf("%d", &_);_;})
#define INF (LL)1e18
#define sz size()
#define pb push_back
#define mkp make_pair
#define eps 1e-15
#define DINF 1e100
typedef long long LL;
typedef vector<int> VI;

class node {
public:
	string name;
	node *c[210];
	int cnt;
	node(string s) { name=s; cnt=0;}
};
node *root;
int ans;
node *create(node *cur, string val) {
//cout << "inserting " << val << " looking at " << cur->name <<endl;
	REP(i,cur->cnt) {
		node * next = cur->c[i];
	//	cout <<"found " << next->name << endl;
		if(next->name.compare(val) == 0) {
			return next;
		}
	}
	node * next = new node(val);
	cur->c[cur->cnt] = next;
	cur->cnt = cur->cnt + 1;
	ans++;
	return next;

}
int main() {
	LL kases = GI+1;	
	FOR(kase, 1, kases) {
		int n = GI, m = GI;
		root = new node("/");
		REP(j,n) {
			string s;
			cin >> s;
			s += "/";
			node *cur = root;
			string word;
			for(int i = 1; i < s.sz; ++i) {
				if(s[i] == '/' && word.sz) {
					cur = create(cur, word);
					word = "";
				}
				else word += s[i];
			}

		}

		ans=0;
		REP(j,m) {
			string s;
			cin >> s;
			s += "/";
			node *cur = root;
			string word;
			for(int i = 1; i < s.sz; ++i) {
				if(s[i] == '/' && word.sz) {
					cur = create(cur, word);
					word = "";
				}
				else word += s[i];
			}

		}
		printf("Case #%d: %d\n", kase, ans);
	}
}
