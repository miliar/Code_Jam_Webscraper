#include<cstdio>
#include<algorithm>
using namespace std;
int ZZZ,N,a[10005],b[10005],c[10005],d[10005];
int ds[10005],cnt=0;

int find(int k){
	if (ds[k]!=k) return ds[k] = find(ds[k]);
	return k;
}

bool ok(int i,int j){
//	printf("hi %d %d\n",i,j);
	if (c[i]+1<a[j] || c[j]+1<a[i]) return false;
//	printf("hi %d %d\n",i,j);
	if (d[i]+1<b[j] || d[j]+1<b[i]) return false;
//	printf("hi %d %d\n",i,j);
	if (c[i]+1==a[j] && d[i]+1==b[j]) return false;
//	printf("hi %d %d\n",i,j);
	if (c[j]+1==a[i] && d[j]+1==b[i]) return false;
	
//	printf("hi %d %d\n",i,j);
	return true;
}

int main(){
	int w[105][105];
	
	scanf("%d",&ZZZ);
	for (int z=1;z<=ZZZ;++z){
	//	memset(w,0,sizeof(w));
			
		scanf("%d",&N);
		for (int i=1;i<=N;++i){
			scanf("%d%d%d%d",&a[i],&b[i],&c[i],&d[i]);
			ds[i] = i;
			
		//	for (int x=a[i];x<=c[i];++x) for (int y=b[i];y<=d[i];++y) w[x][y] = i;
		}
	/*	if (z!=99) continue;
		
		for (int i=1;i<=100;++i) {for (int j=1;j<=100;++j){
		//	printf("%c",'a'+w[i][j]);
			if (w[i][j]) printf("x");
			else printf(".");
		}
		puts("");}
		*/
		for (int i=1;i<=N;++i){
			for (int j=i+1;j<=N;++j){
				if (ok(i,j)){
					ds[find(j)] = find(i);
				}
			}
		}
		
	//	for (int i=1;i<=N;++i) printf("%d %d %d %d %d %d\n",i,ds[i],a[i],b[i],c[i],d[i]);
		for (int i=1;i<=N;++i) find(i);
		int ans=0;
		for (int i=1;i<=N;++i){
			if (ds[i]==i){
				int mxx=0,mxy=0,mn=(1<<30);
				for (int j=1;j<=N;++j){
					if (ds[j]==i){
						if (c[j]>mxx) mxx=c[j];
						if (d[j]>mxy) mxy=d[j];
						if (a[j]+b[j]<mn) mn = a[j]+b[j];
					}
				}
				if (mxx+mxy-mn+1 > ans) ans = mxx+mxy-mn+1;
			//	printf("%d %d\n",i,mxx+mxy-mn+1);
			}
		}
		
		printf("Case #%d: %d\n",z,ans);
		cnt += ans;
	}
//	printf("%d\n",cnt);
	return 0;
}
