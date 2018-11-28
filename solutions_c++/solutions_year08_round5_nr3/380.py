#include <stdio.h>
#include <string.h>

int test(int m,int i){
	return (m&(1<<i));
}

int max(int a,int b){
	if(a>b) return a;
	return b;
}

int main(){
	freopen("C-small-attempt2.in","r",stdin);
	freopen("c.txt","w",stdout);
	const int size=12;
	int C,T,M,N,f[2][1<<size],i,j,k,v,p,r,c;
	char s[size];
	scanf("%d",&C);
	for(T=1; T<=C; T++){
		scanf("%d%d",&M,&N);
		memset(f,-1,sizeof(f));
		f[0][0]=r=0;
		for(i=p=0; i<M; i++){
			scanf("%s",s);
			for(j=0; j<(1<<N); j++){
				int &u=f[1-p][j];
				for(v=c=0; v<N; v++){
//					if(i==0&&j==1&&v==1){
//						printf("v=%d %d %c\n",v,test(j,v),s[v]);
//					}
					if(!test(j,v)) continue;
					c++;
					if(s[v]=='x') break;
					if(v>0&&test(j,v-1)) break;
				}
//				if(i==0&&j==1){
//					printf("v=%d\n",v);
//				}
				if(v<N){
					u=-1;
					continue;
				}
				u=0;
				for(k=0; k<(1<<N); k++){
					int &x=f[p][k];
					if(x<0) continue;
					for(v=0; v<N; v++){
						if(!test(j,v)) continue;
						if(v>0&&test(k,v-1)) break;
						if(v+1<N&&test(k,v+1)) break;
					}
					if(v>=N){
//						if(i==0&&j==0) printf("k=%d %d %d %d\n",k,u,v,c);
						u=max(u,x+c);
					}
				}
				//if(u>r) printf("i=%d j=%d %d\n",i,j,u);
				if(u>r) r=u;
			}
			p=1-p;
		}
		printf("Case #%d: %d\n",T,r);
	}
	return 0;
}
