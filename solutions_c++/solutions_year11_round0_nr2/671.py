#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
#include<stack>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)
#define MAX 105

vector<string> com, op;

void combine(string &r) {
	if(r.size() < 2) return;
	int n,i;
	n = r.size();
	rep(i, com.size()) {
		if(com[i][0] == r[n-1] && com[i][1] == r[n-2]) {
			r = r.substr(0, n-2) + com[i][2];
			combine(r);
			break;
		}
		else if(com[i][0] == r[n-2] && com[i][1] == r[n-1]) {
			r = r.substr(0, n-2) + com[i][2];
			combine(r);
			break;
		}
	}
}

void oppose(string &r) {
	int n,i,j,k;
	n = r.size();
	rep(i,n) for(j=i+1;j<n;j++) {
		rep(k,op.size()) {
			if(op[k][0] == r[i] && op[k][1] == r[j]) { r=""; return; }
			if(op[k][0] == r[j] && op[k][1] == r[i]) { r=""; return; }
		}
	}
}

int main() {
	int T,kase=1;
	int C,D,i,n;
	char s[1000];
	string seq,res;
	//stack<char> S;
	scanf(" %d",&T);
	while(T--) {
		printf("Case #%d: [",kase++);
		com.clear(); op.clear();
		scanf(" %d",&C);
		rep(i,C) {
			scanf(" %s", s);
			com.push_back(s);
		}

		scanf(" %d",&D);
		rep(i,D) {
			scanf(" %s", s);
			op.push_back(s);
		}

		scanf(" %d %s",&n, s);
		seq = s;
		res = "";
		//while(!S.empty()) S.pop();
		rep(i,n) {
			res += seq[i];
			combine(res);
			oppose(res);
		}
		rep(i,res.size()) {
			if(i > 0) printf(", ");
			printf("%c",res[i]);
		}printf("]\n");

	}
	return 0;
}