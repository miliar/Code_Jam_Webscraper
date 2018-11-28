#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>
#include <set>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)
#define FOR(i,a,b) for (int i=a,_n=b; i<=_n; i++)
#define FORE(i,a) for (__typeof(a.begin()) i=a.begin(); i!=a.end(); i++)

char L[30], D[10010][30], AD[10010][30];
int nTC,nD,nQ,DL[10010];

int calc(int chosen){
	vector<int> cand;
	REP(i,nD) if (DL[i]==DL[chosen]) cand.push_back(i);
	int ret = 0;
	for (char *g=L; cand.size() && *g; g++){
		int ada = false, ch = *g - 'a';
		REP(i,cand.size()){
			int idx = cand[i];
			if (D[idx][ch]){ ada = true; break; }
		}
		if (ada){
			int loss = (!D[chosen][ch])? 1 : 0;
			for (int i=0; i<cand.size(); i++){
				int idx = cand[i], prune = 0;
				for (int j=0; j<DL[chosen] && !prune; j++){
					if (AD[chosen][j]==*g){
						if (AD[idx][j]!=*g) prune = 1;
					} else {
						if (AD[idx][j]==*g) prune = 1;
					}
				}
				if (prune){
					cand[i] = cand.back();
					cand.pop_back();
					i--;
				}
			}
//			fprintf(stderr,"char = %c, cands = %d, dic=%s, tipu = %d\n",*g,cand.size(),AD[cand[0]],loss);
			ret += loss;
		}
	}
	return ret;
}

void solve(){
	int best=-1, bestd=-1;
	REP(i,nD){
		int loss = calc(i);
//		fprintf(stderr,"DIC = %s, los = %d\n",AD[i],loss);
		if (loss > best){
			best = loss;
			bestd = i;
		}
	}
//	fprintf(stderr,"%d %d\n",best,bestd);
	printf(" %s",AD[bestd]);
}

int main(){
	scanf("%d",&nTC);
	FOR(TC,1,nTC){
		scanf("%d %d",&nD,&nQ);
		memset(D,0,sizeof(D));
		REP(i,nD){
			scanf("%s",AD[i]);
			DL[i] = strlen(AD[i]);
			REP(j,DL[i]) D[i][AD[i][j]-'a']++;
		}

		printf("Case #%d:",TC);
		REP(i,nQ){
			scanf("%s",L);
			solve();
		}
		puts("");
		fflush(stdout);
	}
}
