#include <stdio.h>
#include <string.h>

#define MAX 160

inline int width(int k,int i) {
	return i<k ? i+1 : 2*k-i-1;
}

inline int place(int k,int i,int j) {
	return i<k ? k-i-1+j*2 : i-k+1+j*2;
}

int a[MAX*2][MAX*2];
int b[MAX*2][MAX*2];
int c[MAX*2][MAX*2];

void print(int n,int z[][MAX*2]) {
	for(int i=0;i<2*n-1;++i) {
		for(int j=0;j<2*n-1;++j) {
			if(z[i][j]>=0)
				printf("%d",z[i][j]);
			else if(z[i][j]==-1)
				printf(" ");
			else printf("?");
		}
		printf("\n");
	}
}

inline bool check_hor(int n) {
	for(int i=0;i<2*n-1;++i) {
		for(int j=0;j<width(n,i)/2;++j) {
			int k=place(n,i,j);
			int h=place(n,i,width(n,i)-1-j);
			if(c[i][k]>=0 && c[i][h]>=0 && c[i][k]!=c[i][h])
				return false;
			if(c[i][k]<0) c[i][k]=c[i][h];
			if(c[i][h]<0) c[i][h]=c[i][k];
		}
	}
	return true;
}

inline bool check_ver(int n) {
	for(int i=0;i<n-1;++i) {
		for(int j=0;j<width(n,i);++j) {
			int k=place(n,i,j);
			int h=2*n-2-i;
			if(c[i][k]>=0 && c[h][k]>=0 && c[i][k]!=c[h][k])
				return false;
			if(c[i][k]<0) c[h][k]=c[i][k];
			if(c[h][k]<0) c[i][k]=c[h][k];
		}
	}
	return true;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int n;
		scanf("%d",&n);
		memset(a,0xFF,sizeof(a));
		for(int i=0;i<2*n-1;++i)
			for(int j=0;j<width(n,i);++j)
				scanf("%d",&a[i][place(n,i,j)]);
		printf("Case #%d: ",test);
		int ans;
		for(ans=n;ans<=3*n;++ans) {
			memset(b,0xFF,sizeof(b));
			for(int i=0;i<2*ans-1;++i)
				for(int j=0;j<width(ans,i);++j)
					b[i][place(ans,i,j)]=-2;
			for(int i=0;i<2*ans-1;++i)
				for(int jj=0;jj<width(ans,i);++jj) {
					int j=place(ans,i,jj)-n+1;
					if(j>=0) {
						bool ok=true;
						memcpy(c,b,sizeof(b));
						for(int k=0;k<2*n-1;++k)
							for(int h=0;h<width(n,k);++h) {
								int ni=k+i;
								int nj=j+place(n,k,h);
								if(ni>=2*ans-1 || nj>place(ans,ni,width(ans,ni)-1) || c[ni][nj]!=-2) {
									ok=false;
									goto zzz;
								}
								c[ni][nj]=a[k][place(n,k,h)];
							}
zzz:;				if(ok) {
//							print(ans,c);
							if(check_hor(ans) && check_ver(ans))
								goto found;
						}
					}
				}
		}
		printf("BUG\n");
found:
		printf("%d\n",ans*ans-n*n);
	}
	return 0;
}
