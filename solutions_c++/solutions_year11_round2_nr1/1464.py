#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

char table[101][101];
int win[101],loss[101];
double WP[101],OWP[101],OOWP[101];

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T,t,N,i,j;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d",&N);
		memset(table,0,sizeof(table));
		memset(win,0,sizeof(win));
		memset(loss,0,sizeof(loss));
		for(i=1;i<=N;i++){
			for(j=1;j<=N;j++){
				while(scanf("%c",&table[i][j]) && table[i][j]=='\n');
				if(table[i][j]=='1')win[i]++;
				else if(table[i][j]=='0')loss[i]++;
			}
		}
		for(i=1;i<=N;i++)WP[i]=win[i]*1.0/(win[i]+loss[i]);
		for(i=1;i<=N;i++){
			OWP[i]=0;
			for(j=1;j<=N;j++){
				if(table[i][j]=='1')OWP[i]+=win[j]*1.0/(win[j]+loss[j]-1);
				else if(table[i][j]=='0')OWP[i]+=(win[j]-1)*1.0/(win[j]+loss[j]-1);
			}
			OWP[i]/=(win[i]+loss[i]);
		}
		for(i=1;i<=N;i++){
			OOWP[i]=0;
			for(j=1;j<=N;j++){
				if(table[i][j]!='.')OOWP[i]+=OWP[j];
			}
			OOWP[i]/=(win[i]+loss[i]);
		}
		printf("Case #%d:\n",t);
		for(i=1;i<=N;i++)printf("%.7llf\n",0.25*WP[i]+0.50*OWP[i]+0.25*OOWP[i]);
	}
	
	return 0;
}
