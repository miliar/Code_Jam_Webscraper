#include <cmath>
using namespace std;
#include <iostream>
#include <string>
#include <cstdio>
#include <map>

//By chyx111
#define DBG(a) cerr << #a << ": " << (a) << endl
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)

char strtmp[110000];
int np;

map<pair<int,string>, int> son;

void build(char *s, int root){
	if( ! *s ) return;
	for(int i = 0; ;++i){
		if( s[i] == '/' ){
			s[i] = 0;

			if( son.count( make_pair(root,s)) == 0){
				son[make_pair(root, s)] = np++;
			}

			build(s+i+1, son[make_pair(root,s) ] );
			return;
		}else if( s[i] == 0){
			if( son.count( make_pair(root,s)) == 0){
				son[make_pair(root, s)] = np++;
			}
			return;
		}
	}
}

int cnt;
void update(char *s, int root){
	if( ! *s ) return;
	for(int i = 0; ;++i){
		if( s[i] == '/'){
			s[i] = 0;

			if( son.count( make_pair(root,s)) == 0){
//				DBG(s);
				cnt++;
				son[make_pair(root, s)] = np++;
			}

			update(s+i+1, son[make_pair(root,s)]);
			return;
		}else if( s[i] == 0){
			if( son.count( make_pair(root,s)) == 0){
//				DBG(s);
				cnt++;
				son[make_pair(root, s)] = np++;
			}
			return;
		}
	}
}

int main() {
	int ca;cin>>ca;
	np = 0;
	Rep(ica,ca){
		int n,m; scanf("%d%d", &n,&m);
		np = 1;
		son.clear();
		Rep(i,n){
			scanf("%s", strtmp);
			build(strtmp+1, 0);
		}
		cnt=0;
		Rep(i,m){
			scanf("%s", strtmp);
			update(strtmp+1, 0);
		}
		DBG(np);

		printf("Case #%d: %d\n", ica+1, cnt);
	}
	return 0;
}

