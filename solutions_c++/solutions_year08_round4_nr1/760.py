


#include<iostream>
using namespace std;

const int maxn=20000;
const int inf=9999999;
int d[maxn][2];
int g[maxn],cc[maxn];
int m,v;
#define min(x,y) x<y?x:y
void ini(){
	int i,j,k;
	scanf("%d%d",&m,&v);
	memset(d,-1,sizeof(d));
	for(i=1;i<=(m-1)/2;i++)scanf("%d%d",&g[i],&cc[i]);
	for(i=(m-1)/2+1;i<=m;i++){
		scanf("%d",&k);if(k==0){ d[i][0]=0;d[i][1]=inf;}
		else { d[i][1]=0;d[i][0]=inf;}
	}
}

bool solve(){
	int i,j,k;	
	
		for(i=(m-1)/2;i>=1;i--){
			int c=i*2;d[i][0]=d[i][1]=inf;
			if(g[i]==1){
				d[i][0]=min(d[i][0],d[c+1][0]+d[c][0]);d[i][0]=min(d[i][0],d[c+1][1]+d[c][0]);
				d[i][0]=min(d[i][0],d[c+1][0]+d[c][1]);d[i][1]=min(d[i][1],d[c+1][1]+d[c][1]);
			}
			else {
				d[i][0]=min(d[i][0],d[c+1][0]+d[c][0]);d[i][1]=min(d[i][1],d[c+1][1]+d[c][0]);
				d[i][1]=min(d[i][1],d[c+1][0]+d[c][1]);d[i][1]=min(d[i][1],d[c+1][1]+d[c][1]);
			}

			if(cc[i]==0)continue;

			if(g[i]==1){
			d[i][0]=min(d[i][0],d[c+1][0]+d[c][0]+1);d[i][1]=min(d[i][1],d[c+1][1]+d[c][0]+1);
			d[i][1]=min(d[i][1],d[c+1][0]+d[c][1]+1);d[i][1]=min(d[i][1],d[c+1][1]+d[c][1]+1);
			}
			else {
			d[i][0]=min(d[i][0],d[c+1][0]+d[c][0]+1);d[i][0]=min(d[i][0],d[c+1][1]+d[c][0]+1);
			d[i][0]=min(d[i][0],d[c+1][0]+d[c][1]+1);d[i][1]=min(d[i][1],d[c+1][1]+d[c][1]+1);
			}
			
		}

		if(d[1][v]<inf){
			printf("%d\n",d[1][v]);return true;
		}
		else return false;
}

	

int main(){
	int i,t,ca,j;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for(ca=1;ca<=t;ca++){		 
		ini();
		printf("Case #%d: ",ca);
		if(solve()==false)printf("IMPOSSIBLE\n");
	}

	return 0;
}


