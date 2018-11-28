#include <iostream>
#include <cstdlib>
#include <cstdio>
#define maxlong 1000000000

using namespace std;

int ii,T,i,n,j,k,ans;
int f[12][1024][14];
int Minval[12][1024];
int a[1024];
int val[12][1024];
FILE *fin=freopen("B.in","r",stdin);
FILE *fout=freopen("B.out","w",stdout);

//SMALL 
/*
int dfs(int l,int r,int al){
	int Max=-1;
	for(int i=l;i<=r;i++)
		Max=max(Max,M[i]);
	if(al>=Max)
		return 0;
	ans++;
	if(l+1==r)
		return 0;
	int mid=l+r>>1;
	dfs(l,mid,al+1);
	dfs(mid+1,r,al+1);
}

int main(){
	cin >> T;
	for(int c=1;c<=T;c++){
		cin >> P ;
		N=1<<P;
		for(int i=0;i<N;i++){
			cin >> M[i];
			M[i]=P-M[i];
		}
		
		int tmp;
		for(int i=N/2;i>=1;i/=2)
			for(int j=0;j<i;j++)
				cin >> tmp;
		
		ans=0;
		dfs(0,N-1,0);
		fprintf(fout,"Case #%d: %d\n",c,ans);
	}
}
*/

// LARGE
int main() {
	cin >> T ;
	for (ii=1;ii<=T;++ii) {
		cin >> n;
		memset(f,0,sizeof(f));
		for (i=0;i<=(1 << n)-1;++i) 
			cin >> Minval[n][i] ;
		for (i=n-1;i>=0;--i)
			for (j=0;j<=(1 << i)-1;++j)
				cin >> val[i][j];
		for (i=n-1;i>=0;--i)
			for (j=0;j<=(1 << i)-1;++j) 
				Minval[i][j]=min(Minval[i+1][j*2],Minval[i+1][j*2+1]);
		for (i=1;i<(1 << n);++i)
			for (k=Minval[n][i]+1;k<=n+1;++k)
				f[n][i][k]=maxlong;
		for (i=n-1;i>=0;--i)
			for (j=0;j<=(1 << i)-1;++j) {
				for (k=0;k<Minval[i][j];++k)
					f[i][j][k]=min(f[i+1][j*2][k+1]+f[i+1][j*2+1][k+1]
								,f[i+1][j*2][k]+f[i+1][j*2+1][k]+val[i][j]);
				f[i][j][k]=f[i+1][j*2][k]+f[i+1][j*2+1][k]+val[i][j];
				for (k=Minval[i][j]+1;k<=n+1;++k) 
					f[i][j][k]=maxlong;
			}
		ans=min(f[0][0][1],f[0][0][0]);
		fprintf(fout,"Case #%d: %d\n",ii,ans);
	}
	
	return 0;
}
