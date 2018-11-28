// Headers {{{
#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,j,k) for(int i=(j); i<=(k); ++i)
#define FORD(i,j,k) for(int i=(j); i>=(k); --i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ST first
#define ND second
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define SQR(a) ((a)*(a))
#define debug(x) cerr << #x << " = " << x << '\n'
template<typename Q> inline int size(Q a) { return a.size(); }
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<pair<int,int> > VPII;
typedef unsigned long long ULL;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
const int INF=1000000000;
// }}}

char buf[100];
string read() {
	gets(buf);
	return buf;
}

double s2d(string s) {
	double res;
	sscanf(s.c_str(),"%lf",&res);
	return res;
}

string desc;

struct Node {
	string feature;
	double w;
	Node *left,*right;
};

char descr[1000];

Node *root;

int poz;

void deluj(Node *nod) {
	if(nod->left!=NULL) {
		deluj(nod->left);
		deluj(nod->right);
	}
	delete nod;
}

void build(Node *r) {
//	printf("build\n");
	while(desc[poz]!='(') ++poz;
	string wei;
	++poz;
	while(desc[poz]==' ') ++poz;
	while(desc[poz]=='.' || isdigit(desc[poz])) {
		wei+=desc[poz];
		++poz;
	}
	r->w=s2d(wei);
	while(desc[poz]==' ') ++poz;
	if(desc[poz]==')') {
		r->left=r->right=NULL;
		return;
	}
	while(desc[poz]!=' ') {
		r->feature+=desc[poz];
		++poz;
	}
	r->left=new Node;
	r->right=new Node;
	build(r->left);
	build(r->right);
	while(desc[poz]!=')') ++poz;
	++poz;
}

int main() {
	int ntc;
	scanf("%d\n",&ntc);
	FOR(tc,1,ntc) {
		printf("Case #%d:\n",tc);
		int lines;
		scanf("%d\n",&lines);
		desc="";
		REP(i,lines) {
			string s=read();
			if(i) desc+=' ';
			desc+=s;
		}
		poz=0;
		root=new Node;
		build(root);
		int n;
		scanf("%d\n",&n);
		REP(i,n) {
			gets(descr);
			VS v;
			int j=0;
			while(descr[j]!=' ') ++j;
			while(isdigit(descr[j])) ++j;
			while(descr[j]==' ') ++j;
			for(;;) {
				string cur;
				while(descr[j]!=' ' && descr[j] && descr[j]!='\n') {
					cur+=descr[j];
					++j;
				}
//				printf("dodaje %s\n",cur.c_str());
				v.push_back(cur);
				if(!descr[j] || descr[j]=='\n') break;
				while(descr[j]==' ') ++j;
			}
		//	printf("j=%d\n",j);
			double res=1.0;
			Node *poz=root;
			while(true) {
//				printf("%s\n",poz->feature.c_str());
				res*=poz->w;
				if(poz->left==NULL) break;
				if(find(ALL(v),poz->feature)!=v.end()) poz=poz->left;
				else poz=poz->right;
			}
			printf("%0.8lf\n",res);
		}
		deluj(root);
	}
	return 0;
}
