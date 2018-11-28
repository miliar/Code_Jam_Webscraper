#include<cstdio>
#include<vector>
#include<list>
#include<queue>
#include<stack>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>
using namespace std;
#define REP(i,n) for(int i=0;i<(n); ++i)
int opp[256][256];
int comb[256][256];
char let[101];
vector<char> elli;
void print_list(){
	printf("[");
	REP(i,(int)elli.size()-1)
		printf("%c, ", elli[i]);
	if(!elli.empty()) printf("%c", *elli.rbegin());
	printf("]");
}
int main(){
	char tmp;
	int z, res, C, D, N; scanf("%d", &z); REP(jj,z) {
		REP(i,256) REP(j,256) opp[i][j] = 0;
		REP(i,256) REP(j,256) comb[i][j] = 0;
		scanf("%d", &C);
		while(C--){
			scanf("%s", let);
			comb[(unsigned char)let[0]][(unsigned char)let[1]] = comb[(unsigned char)let[1]][(unsigned char)let[0]] = 1 + (unsigned char)let[2];
		}
		scanf("%d", &D);
		while(D--){
			scanf("%s", let);
			opp[(unsigned char)let[0]][(unsigned char)let[1]] = opp[(unsigned char)let[1]][(unsigned char)let[0]] = 1;
		}
		scanf("%d%s", &N, let);
		REP(i,N){
			if(!elli.empty()){
				tmp = *elli.rbegin();
				if(comb[(unsigned char)tmp][(unsigned char)let[i]]){
					elli.pop_back();
					let[i] = comb[(unsigned char)tmp][(unsigned char)let[i]] - 1;
				} else {
					REP(j,elli.size())
						if(opp[(unsigned char)elli[j]][(unsigned char)let[i]]){
							elli.clear();
							goto rep1end;
						}
				}
			}
			elli.push_back(let[i]);
			rep1end:;
		}
		printf("Case #%d: ", jj+1);
		print_list();
		printf("\n");
		elli.clear();
	}
	return 0;
}

