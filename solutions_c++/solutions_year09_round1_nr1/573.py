#include <stdio.h>
#include <string.h>
#include <set>
#define maxn 50000

using namespace std;

bool f[11][maxn];

int r[11][11][11];

int nextone(int u,int b){
	int ret=0;
	int tmp;
	while (u){
		tmp=u%b;
		u/=b;
		ret=ret+tmp*tmp;
	}
	return ret;
}

int check(int u,int b){
	int r;
	set<int> S;
	S.clear();
	while (1){
		if (S.find(u)!=S.end()) break;
		S.insert(u);
		u=nextone(u,b);
//		fprintf(stderr,"[%d,%d]\n",u,b);
	}
//	fprintf(stderr,"%d %d\n",u,b);
	return u==1;
}

int main(){
	int i,j,k,t,b;
	int cas;
	char s[1000];
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	for (b=2;b<11;b++){
		for (i=1;i<maxn;i++)
			f[b][i]=check(i,b);
		fprintf(stderr,"%d\n",b);
	}
	for (i=2;i<=10;i++) for (j=i+1;j<=10;j++){
		for (t=2;t<maxn;t++){
			if (f[i][t] && f[j][t]){
				r[0][i][j]=t;
//				printf("%d %d => %d\n",i,j,t);
				break;
			}
		}
//		if (t==maxn) printf("Error %d %d\n",i,j);
		for (k=j+1;k<=10;k++){
			for (t=2;t<maxn;t++){
				if (f[i][t] && f[j][t] && f[k][t]){
					r[i][j][k]=t;
//					printf("%d %d %d => %d\n",i,j,k,t);
					break;
				}
			}
//			if (t==maxn) printf("Error %d %d %d\n",i,j,k);
		}
	}
	scanf("%d",&t);
	cas = 1;
	getchar();
	while (t--){
		gets(s);
		b=sscanf(s,"%d %d %d",&i,&j,&k);
		if (b==2) printf("Case #%d: %d\n",cas++,r[0][i][j]);
		else printf("Case #%d: %d\n",cas++,r[i][j][k]);
	}
	return 0;
}
