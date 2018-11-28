#include <stdio.h>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)

char H[1000];
int T,N,P[1000];

int next(int i, char R){
	while (i<N){
		if (H[i]==R) return P[i];
		i++;
	}
	return -1;
}

void adv(char R, int &pos, int to, int tm){
	if (to==-1) return;
	if (pos < to){
		pos += min(to-pos, tm);
	} else if (pos > to){
		pos -= min(pos-to, tm);
	}
}

int main(){
	scanf("%d",&T);
	REP(tc,T){
		scanf("%d",&N);
		REP(i,N) scanf("%s %d",H+i,&P[i]);
		int Bp=1, Op=1, res=0;
		REP(i,N){
			int tO = next(i,'O');
			int tB = next(i,'B');
			if (H[i]=='B'){
				if (P[i]!=Bp){
					int need = abs(tB-Bp);
					adv('O',Op,tO,need);
					adv('B',Bp,tB,need);
					res += need;
				}
				assert(P[i]==Bp);
				res++;
				adv('O',Op,tO,1);
			} else {
				if (P[i]!=Op){
					int need = abs(tO-Op);
					adv('O',Op,tO,need);
					adv('B',Bp,tB,need);
					res += need;
				}
				assert(P[i]==Op);
				res++;
				adv('B',Bp,tB,1);
			}
		}
		printf("Case #%d: %d\n",tc+1,res);
		fflush(stdout);
	}
}
