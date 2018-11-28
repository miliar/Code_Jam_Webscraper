#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;
typedef long long LL;


int ntc,n,m,res,old;
struct cc { set<LL> S; cc() { S.clear(); } };
map<LL, cc*> M;
cc * root, * act;
char buff[1007]; 

void analyse() {
	LL hash=0;
	act=root;
	for(int i=1; ; ++i) {
		if(buff[i]=='/' || buff[i]==0) {
			act->S.insert(hash);
			if(M[hash]==NULL) { ++res; M[hash]=new cc; }
			act=M[hash];	
			if(buff[i]==0) break;
		} else {
			hash*=26LL;
			hash+=(LL)buff[i];
		}
	}
}

void undo(cc * x) {
	for(set<LL>::iterator it = (x->S).begin(); it!= (x->S).end(); ++it) { undo(M[*it]); M[*it]=NULL; }
	delete(x);
}


int main() {
	scanf("%d", &ntc);
	for(int i=1; i<=ntc; ++i) {
		printf("Case #%d: ", i);
		scanf("%d%d", &n,&m);
		root = new cc;
		while(n--) {
			scanf(" %s", buff);
			analyse();
		}
		old=res;
		while(m--) {
			scanf(" %s", buff);
			analyse();
		}
		printf("%d\n", res-old);
		res=old=0;
		undo(root);		
	}
}










