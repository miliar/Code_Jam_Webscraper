#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <algorithm>
#include <iostream>
#include <assert.h>
#ifdef DM1_MACHINE	
	#include "template.cpp"
#endif

using namespace std;

#define SET(v,i) memset(v,i,sizeof(v));
#define FOR(i,n,k) for(int i=n;i<k;++i)
#define RI(i) scanf("%d",&i);
#define RS(i) scanf("%s",i);
#define RF(i) scanf("%lf",&i);
#define RL(i) scanf("%lld",&i);

const int INF=0x3F3F3F3F;
const int MAXN=100001;
typedef long long int i64;
typedef pair<int,int> pii;
typedef pair<string,int> psi;

char mat[5][5];

bool win(pii pos,char who){
	bool valid=true;
	if(pos.first == 3-pos.second){
		FOR(i,0,4){
			if(mat[i][3-i]!=who && mat[i][3-i]!='T') { valid=false; break; }
		}
		if(valid) return true;
	}
	if(pos.first == pos.second){
		FOR(i,0,4){
			if(mat[i][i]!=who && mat[i][i]!='T') { valid=false; break; }
		}
		if(valid) return true;
	}
	valid=true;
	FOR(i,0,4){
		if(mat[pos.first][i]!=who && mat[pos.first][i]!='T') { valid=false; break; }
	}
	if(valid) return true;
	valid=true;
	FOR(i,0,4){
		if(mat[i][pos.second]!=who && mat[i][pos.second]!='T') { valid=false; break; }
	}
	if(valid) return true;
	return false;
}

inline void solve(int test){
	int t;
	RI(t);
	FOR(ic,1,t+1){
		vector<pii> O,X;
		bool canDraw=true;
		FOR(i,0,4){
			RS(mat[i]);
			FOR(j,0,4){
				if(mat[i][j]=='O')
					O.push_back(make_pair(i,j));
				else if(mat[i][j]=='X')
					X.push_back(make_pair(i,j));
				else if(mat[i][j]=='.')
					canDraw=false;
			}
		}
		printf("Case #%d: ",ic);
		bool W=false;
		FOR(i,0,(int)O.size()){
			if(win(O[i],'O')){
				printf("O won\n");
				W=true;
			}
			if(W) break;
		}
		if(W) continue;
		FOR(i,0,(int)X.size()){
			if(win(X[i],'X')){
				printf("X won\n");
				W=true;
			}
			if(W) break;
		}
		if(W) continue;
		if(canDraw){
			printf("Draw\n");
		}
		else printf("Game has not completed\n");
	}
}
int main(){
	freopen("FILE.in","r",stdin);
	freopen("FILE.out","w",stdout);
	solve(0);
	return 0;
}

////////////////////////////////////////////
/////////////Code by David Moran////////////
/////////////////////////////P=NP///////////

