#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
using namespace std;
int num[1200],tim,T,i,j;
char c[120][120];
bool work(char x){
	int i,j;
	for(i=1;i<=4;++i){
		num['X']=num['O']=num['T']=0;
		for(j=1;j<=4;++j)num[c[i][j]]++;
		if(num[x]==4 || num[x]==3 && num['T']==1){
			printf("%c won\n",x);
			return 1;
		}
	}
	for(j=1;j<=4;++j){
		num['X']=num['O']=num['T']=0;
		for(i=1;i<=4;++i)num[c[i][j]]++;
		if(num[x]==4 || num[x]==3 && num['T']==1){
			printf("%c won\n",x);
			return 1;
		}
	}
	num['X']=num['O']=num['T']=0;
	for(i=1;i<=4;++i)num[c[i][i]]++;
	if(num[x]==4 || num[x]==3 && num['T']==1){
		printf("%c won\n",x);
		return 1;
	}
	num['X']=num['O']=num['T']=0;
	for(i=1;i<=4;++i)num[c[i][5-i]]++;
	if(num[x]==4 || num[x]==3 && num['T']==1){
		printf("%c won\n",x);
		return 1;
	}
	return 0;
}
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	for(scanf("%d",&T),tim=1;tim<=T;++tim){
		for(i=1;i<=4;++i)scanf("%s",c[i]+1);
		printf("Case #%d: ",tim);
		if(work('X'))continue;
		if(work('O'))continue;
		for(i=1;i<=4;++i){
			for(j=1;j<=4;++j)if(c[i][j]=='.')break;
			if(j<=4)break;
		}
		if(i==5)printf("Draw\n");
		else printf("Game has not completed\n");
	}
}
		
