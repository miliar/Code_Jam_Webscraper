#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
const int MAXN=110;
struct point{
	int a[110];
}mm[MAXN];
int operator<(point x,point y){
	return x.a[0]>y.a[0];
}

int cs,cn=1;
int uy[MAXN],n,m;
int mp[MAXN][MAXN],lk[MAXN];


int can(int x,int y){
	int i;
	for(i=0;i<m;i++) if(mm[x].a[i]<=mm[y].a[i]) return 0;
	return 1;
}

int fd(int a){
	int i,j,k;
	for(i=0;i<n;i++){
		if(!uy[i]&&mp[a][i]){
			k=lk[i];lk[i]=a;uy[i]=1;
			if(k==-1||fd(k)) return 1;
			lk[i]=k;
		}
	}
	return 0;
}


int main(){
	freopen("C-large.in","r",stdin);
	freopen("c.txt","w",stdout);
	int i,j,k,t;
	scanf("%d",&cs);
	while(cs--){
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++){
			for(j=0;j<m;j++) scanf("%d",&mm[i].a[j]);
		}
		sort(mm,mm+n);
		memset(mp,0,sizeof(mp));
		for(i=0;i<n;i++){
			for(j=i+1;j<n;j++){
				if(can(i,j)) mp[i][j]=1;
			}
		}
		memset(lk,-1,sizeof(lk));
		int pp = 0;
		for(i=0;i<n;i++){
			memset(uy,0,sizeof(uy));
			pp += fd(i);
		}
		printf("Case #%d: %d\n",cn++,n-pp);
	}
	return 0;
}
