#include <stdio.h>

#define INP freopen("c.in","rt",stdin)
#define OUP freopen("c.out","wt",stdout)
#define FOR(i,a,b) for(i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,1,n)
#define N 1000
#define max(a,b) (a>b) ? a : b

int T;
int r,k,n;
int g[N+5];
int go[N+5];
long long gg[N+5];

void process(){
	int i,offset=1;

	long long ans=0;
	long long tmp;

	REP(i,n*2){
		go[i] = -1;
	}

	REP(i,r){

		if (offset>n){
			offset -= n;
		}

		int l_,r_,m_,foffset;
		long long fnd;

		l_ = offset;
		r_ = offset+n-1;
		tmp = -1;



		//if (go[l_] < 




		//printf("%d",offset);
		while(l_<=r_){
			m_ = (l_+r_)/2;
			fnd = gg[m_] - gg[offset-1];
			if (fnd > k){
				r_ = m_-1;
			}
			else if (fnd < k){
				l_ = m_+1;
				if (tmp < fnd){
					tmp = fnd;
					foffset = m_+1;
				}
			}
			else if (fnd == k){
				if (tmp < fnd){
					tmp = fnd;
					foffset = m_+1;
				}
				break;
			}
		}
		offset = foffset;
		//printf(" %d\n",fnd);
		ans += tmp;
	}
	printf("Case #%d: %lld\n",T,ans);
}

void input(){
	int i;
	scanf("%d %d %d",&r,&k,&n);
	REP(i,n){
		scanf("%d",&g[i]);
	}
	REP(i,n){
		g[i+n] = g[i];
	}
	REP(i,2*n){
		gg[i] = g[i];
	}
	gg[0] = 0;
	REP(i,2*n){
		gg[i+1] += gg[i];
	}
}

int main(){
	int t;
	INP;
	OUP;
	scanf("%d",&t);
	REP(T,t){
		input();
		process();
	}
	return 0;
}
