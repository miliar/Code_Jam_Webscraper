#include<stdio.h>
#include<string.h>
#include<algorithm>
char s[10001][11];
char t0[27],t[101][27];
struct S {
	int ND;
	int sr;
	bool operator<(S x) const {
		return sr>x.sr||sr==x.sr&&ND<x.ND;
	}
} se[10001];
bool maybe[1001];
char now[1001];
int hvlt[10001][27];
int lns[10001];
char declist[11];
int dc;
bool chk(int y,char *now,char ts){
	char *ans=s[y];
	while(*now){
		/*if(*now==10&&*ans==change){
			now++;
			ans++;
		} else if(*now==*ans){
			now++;
			ans++;
		}*/
		if(*now!=10&&*now!=*ans){
			return 0;
		}
		for(int i=0;i<dc;i++){
			if(*ans==declist[i]){
				return 0;
			}
		}
		if(*ans==ts&&*now==10){
			return 0;
		}
		now++;
		ans++;
	}
	return 1;
}
main(){
	int i,j,k,x,y;
	int T,TN;
	int N,M;
	int wait;
	char test;
	scanf("%d",&T);
	for(TN=1;TN<=T;TN++){
		scanf("%d%d",&N,&M);
		for(i=0;i<26;i++){
			maybe[i]=0;
		}
		for(i=0;i<N;i++){
			scanf("%s",s[i]);
			for(j=0;j<26;j++){
				hvlt[i][j]=0;
			}
			for(j=0;s[i][j];j++){
				maybe[s[i][j]-'a']=1;
				hvlt[i][s[i][j]-'a']++;
			}
			lns[i]=strlen(s[i]);
		}
		for(i=0;i<M;i++){
			scanf("%s",t0);
			k=0;
			for(j=0;t0[j];j++){
				if(maybe[t0[j]-'a']){
					t[i][k++]=t0[j];
				}
			}
			t[i][k]=0;
			//puts(t[i]);
		}
		printf("Case #%d:",TN);
		for(i=0;i<M;i++){
			for(j=0;j<N;j++){ //if gauss j
				k=0;
				
				
				
				
				wait=lns[j];
				
				for(x=0;x<wait;x++){
					now[x]=10;
				}
				now[wait]=0;
				dc=0;
				for(x=0;t[i][x];x++){
					test=t[i][x];
					if(wait==0)break;
					for(y=0;y<N;y++){
						if(lns[j]==lns[y]&&chk(y,now,test)&&hvlt[y][test-'a'])break;
					}
					if(y>=N)continue;
					if(hvlt[j][test-'a']==0){
						k++;
						declist[dc++]=test;
					} else {
						wait-=hvlt[j][test-'a'];
						for(y=0;s[j][y];y++){
							if(s[j][y]==test){
								now[y]=test;
							}
						}
					}
				}
				
				
				se[j]=(S){j,k};
				//printf(" %d",k);
			}
			std::sort(se,se+N);
			printf(" %s",s[se[0].ND]);
		}
			
		puts("");
	}
		
}


