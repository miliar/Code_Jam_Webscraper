#include<stdio.h>
char c[10001][4],d[10001][3],n[10001],s[10001];
char m[256][256],nn[256][256],cc;
int used[256];
main(){
	int i,j,k;
	int T,TT;
	int C,D,N,p;
	scanf("%d",&T);
	for(TT=1;TT<=T;TT++){
		scanf("%d",&C);
		for(i=0;i<256;i++){
			for(j=0;j<256;j++){
				m[i][j]=0;
				nn[i][j]=0;
			}
		}
		for(i=0;i<C;i++){
			scanf("%s",c[i]);
			m[c[i][0]][c[i][1]]=m[c[i][1]][c[i][0]]=c[i][2];
		}
		scanf("%d",&D);
		for(i=0;i<D;i++){
			scanf("%s",d[i]);
			nn[d[i][0]][d[i][1]]=nn[d[i][1]][d[i][0]]=1;
		}
		scanf("%d",&N);
		scanf("%s",n);
		p=0;
		for(i=0;i<N;i++){
			s[p++]=n[i];
			used[n[i]]++;
			while(p>1&&m[s[p-2]][s[p-1]]){
				used[s[p-2]]--;
				used[s[p-1]]--;
				s[p-2]=m[s[p-2]][s[p-1]];
				used[s[p-2]]++;
				p--;
			}
			for(cc='A';cc<='Z';cc++){
				if(nn[cc][s[p-1]]&&used[cc]){
					for(j=0;j<p;j++){
						used[s[j]]--;
					}
					p=0;
					break;
				}
			}

		}
		for(j=0;j<p;j++){
			used[s[j]]--;
		}
		s[p]=0;
		printf("Case #%d: [",TT);
		for(i=0;i<p;i++){
			if(i){
				putchar(',');
				putchar(' ');
			}
			putchar(s[i]);
		}
		puts("]");
	}
}
