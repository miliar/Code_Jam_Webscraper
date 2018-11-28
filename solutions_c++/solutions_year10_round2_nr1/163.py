#include <algorithm>
#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <list>
#include <stack>
#include <set>
#include <map>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define FORE(it,V) for(__typeof( V.begin() ) it = V.begin(); it != V.end(); ++it)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
typedef long long LL;

struct node{
	string katalog;
	vector<node*> next;
	node () {}
	node (string s): katalog(s) {}
};

int global = 0;

node *root;

vector<string> extract(string s) {
	vector<string> path;
	string aktual = "";
	int latacz = 0;
	while(latacz < s.size()) {
		if(s[latacz] == '/') {
			if(aktual != "") path.PB(aktual);
			aktual = "";
			++latacz;
		} else {
			aktual += (char)s[latacz++];
		}
	}
	if(aktual != "") path.PB(aktual);
	return path;
}

void addPath(vector<string> path) {
	node *current = root;
	FORE(it,path) {
		bool found = false;
		FORE(it2,current->next)
			if( (*it2)->katalog == (*it)) {
				current = *it2;
				found = true;
				break;
			}
		if(!found) {
			node *nowy = new node(*it);
			(current->next).PB(nowy);
			current = nowy;
			++global;
		}
	}
}

void testcase(int v) {
	printf("Case #%d: ", v);
	root = new node("");
	int n, m;
	scanf("%d%d", &n, &m);
	vector<string> istn, nieistn;
	char buf[150];
	REP(i,n) {
		scanf("%s", buf);
		string s = buf;
		addPath( extract(s) );
	}
	global = 0;
	REP(i,m) {
		scanf("%s", buf);
		string s = buf;
		addPath( extract(s));
	}
	printf("%d\n", global);
}

int main() {
	int t;
	scanf("%d", &t);
	REP(i,t) testcase(i+1);
	return 0;
}

