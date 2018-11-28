#include <cstdio>

int T;
int N, S, p;
int t[100];
int best, nsupri;
int sup[100], nsup[100];

int main()
{
	scanf("%d", &T);

	for(int test=1; test<=T; test++) {
		scanf("%d%d%d", &N, &S, &p);
		for(int i=0; i<N; i++) scanf("%d", &t[i]);
		best=nsupri=0;
		for(int i=0; i<N; i++) {
			if(t[i]%3==0) {
				if(t[i]>=3) sup[i]=2+(t[i]-3)/3;
				else sup[i]=-1;
				nsup[i]=t[i]/3;
			}
			else if(t[i]%3==1) {
				if(t[i]>=4) sup[i]=2+(t[i]-4)/3;
				else sup[i]=-1;
				nsup[i]=1+(t[i]-1)/3;
			}
			else {
				sup[i]=2+(t[i]-2)/3;
				nsup[i]=1+(t[i]-2)/3;
			}
			if(nsup[i]>=p) best++;
			else if(sup[i]>=p && nsupri<S) {best++; nsupri++;}
		}
		printf("Case #%d: %d\n", test, best);
	}

	return 0;
}
