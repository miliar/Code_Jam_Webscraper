#include<cstdio>
#include<cstring>
#include<iostream>
#define maxn (1001)
#define L 2000
#define inf 0x3fffffffffffLL
using namespace std;
long long w[maxn][maxn],lx[maxn],ly[maxn],n;
long long fx[maxn],fy[maxn],sy[maxn],slack[maxn],slackx[maxn];
void fix(long e){
	long tmp;
	while(e!=-1){
		sy[e]=fy[e];
		e=fx[fy[e]];
	}
}
long find(long s){
	long u,v,found;
	long long min;
	memset(fx,0,sizeof(fx));
	memset(fy,0,sizeof(fy));
	fx[s]=-1;
	for(u=1;u<=n;u++){
		slack[u]=lx[s]+ly[u]-w[s][u];
		slackx[u]=s;
	}
	while(1){
		found=0;
		for(u=1;u<=n;u++)
			if(fy[u]==0&&slack[u]==0){
				found=1;
				if(sy[u]==0){
					fy[u]=slackx[u];
					return u;
				}else{
					fy[u]=slackx[u];
					fx[sy[u]]=u;
					for(v=1;v<=n;v++)
						if(fy[v]==0&&lx[sy[u]]+ly[v]-w[sy[u]][v]<slack[v]){
							slack[v]=lx[sy[u]]+ly[v]-w[sy[u]][v];
							slackx[v]=sy[u];
						}
				}
			}
		if(!found){
			min=inf;
			for(u=1;u<=n;u++)
				if(fy[u]==0&&slack[u]<min)
					min=slack[u];
			for(u=1;u<=n;u++){
				if(fx[u])
					lx[u]-=min;
				if(fy[u])
					ly[u]+=min;
				slack[u]-=min;
			}
		}
	}
}

bool bt[maxn];

int a[1000],b[1000];
bool dfs(long k){
	if (bt[k]) return false;
	else bt[k]=true;
	for (long i=1;i<=n;++i)
	    if (w[k][i]>-inf && (ly[i]==0 || dfs(ly[i]))){
			ly[i]=k;
			return true;
		}
	return false;
}
void init(){
	memset(sy,0,sizeof(sy));
	memset(lx,0,sizeof(lx));
	memset(ly,0,sizeof(ly));
	long i,j;
	scanf("%d",&n);
	for (i=1;i<=n;++i)
		scanf("%d",&a[i]);
	for (i=1;i<=n;++i)
	    scanf("%d",&b[i]);
	for(i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
			w[i][j]=-(long long)a[i]*b[j];
	memset(ly,0,sizeof(ly));
	for (i=1;i<=n;++i)
	    for (j=1;j<=n;++j)
            lx[i]>?=w[i][j];
}


void KM(){
	for(int i=1;i<=n;i++)
		fix(find(i));
}
int I=0;

void out(){
	long i,j;
	long long s=0;
	for(i=1;i<=n;i++)
		s+=w[sy[i]][i];
	cout << "Case #" << ++I << ": "<< -s << endl;
}
int main(){
	long T;
	scanf("%d\n",&T);
	while (T--){
		init();
		KM();
		out();
	}
	return 0;
}
