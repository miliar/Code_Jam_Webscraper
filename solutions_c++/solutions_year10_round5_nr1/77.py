#include <stdio.h>

int a[1500005];
int p[1000000], np=0;
int al[1000000], m=0;
int ala[1000000], alb[1000000];
int fx, fy;
typedef long long LL;
LL prime;
LL inv(LL x, LL y, LL pp, LL qq, LL rr, LL ss){
	if(y==0) return (pp%prime+prime)%prime;
	return inv(y, (x%y), rr, ss, pp-rr*(x/y), qq-ss*(x/y));
}

void setfx(int x){
	if(fx==-1) fx = x;
	if(x!=-1 && fx!=x) fx = -2;
}
void setfy(int y){
	if(fy==-1) fy = y;
	if(y!=-1 && fy!=y) fy = -2;
}

int main(void)
{
	int i, j;
	p[np++] = 2;
	for(i=3;i<=1000005;i+=2)
		if(a[i]==0){
			p[np++] = i;
			if(i<1000)
				for(j=i*i;j<=1000005;j+=i)
					a[j]=1;
		}
	int T, cs;
	scanf("%d",&T);
	int b[15];
	for(cs=1;cs<=T;cs++){
		int D, K;
		scanf("%d%d",&D,&K);
		m=0;
		int DD=1;
		while(D>0) DD*=10, D--;
		for(i=0;i<K;i++)
			scanf("%d",&b[i]);
		for(i=0;i<np && p[i]<=DD;i++){
			//fprintf(stderr, "p[i]=%d\n", p[i]);
			for(j=0;j<K;j++)
				if(b[j]>=p[i])
					break;
			if(j<K) continue;

			fx=-1, fy=-1;
			prime = (long long)p[i];
			for(j=0;j<K-1;j++){
				if(b[j]==0){
					setfy(b[j+1]);
				}
			}

			for(j=1;j<K-1;j++){
				int u = b[j-1]-b[j];
				if(u<0) u+=p[i];
				int v = b[j]-b[j+1];
				if(v<0) v+=p[i];
				//printf("p[i]=%d, u=%d, v=%d\n",p[i], u, v);
				if(v==0 && u!=0){ setfx(0); setfy(b[j]); continue;}
				if(v!=0 && u==0){ fx=-2; fy=-2; break;}
				setfx(((int)(  ((long long) v)*inv((long long)u, (long long)p[i], 1LL, 0LL, 0LL, 1LL) )%p[i]));
				if(fx>=0){
					fy = b[j] - (int)(((long long) fx * (long long) b[j-1]) %p[i]);
					fy %= p[i];
					while(fy<0) fy+=p[i];

				}else
					fy=-2;
			}
			//printf("p=%d, fx=%d, fy=%d\n",p[i],  fx, fy);
			if(fx==-2 || fy==-2){
				continue;
			}else{
				
				if(fy==-1 && fx!=-1) fprintf(stderr,"HERE");
				if(K>1){
					ala[m] = (fx==-1?0:fx);
					alb[m] = (fy==-1?b[1]:fy);
					al[m++] = p[i];
					if(fx==-1){
						ala[m] = (fx==-1?1:fx);
						alb[m] = (fy==-1?(b[1]-b[0]+p[i])%p[i]:fy);
						al[m++] = p[i];
					}
				}else{
					ala[m] = (fx==-1?0:fx);
					alb[m] = (fy==-1?b[0]:fy);
					al[m++] = p[i];
					ala[m] = (fx==-1?1:fx);
					alb[m] = (fy==-1?0:fy);
					al[m++] = p[i];
					ala[m] = (fx==-1?0:fx);
					alb[m] = (fy==-1?1:fy);
					al[m++] = p[i];
				}
				
				
				//TODO here
			}
		}
		if(m==0){
			printf("Case #%d: Impossible.\n", cs);
			fprintf(stderr,"Case #%d: Impossible.\n", cs);
		}else{
			int fx= (((long long)ala[0]) * ((LL) b[K-1]) + ((LL)alb[0])) % al[0];
			for(i=1;i<K;i++)
				if(b[i-1]==b[i]){
					fx = b[i];
					break;
				}
			if(i==K)
			for(i=1;i<m;i++){
				fy = (((long long)ala[i]) * ((LL) b[K-1]) + ((LL)alb[i])) % al[i];
				if(fy != fx)
					break;
			}else
				i=m;
			
			if(i==m){
				printf("Case #%d: %d\n", cs, fx);
				fprintf(stderr,"Case #%d: %d\n", cs, fx);
			}else{
				printf("Case #%d: I don't know.\n", cs);
				fprintf(stderr,"Case #%d: I don't know.\n", cs);
			}
		}
		
	}
	return 0;
}
