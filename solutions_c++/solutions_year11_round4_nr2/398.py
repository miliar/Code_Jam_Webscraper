#include <iostream>

using namespace std;

int x[600][600],y[600][600],z[600][600],w[600][600],tot[600][600],h[600][600];


int getx(int a,int b,int c,int d) {
	return x[a][b]-x[a][d]-x[c][b]+x[c][d];
}
int gety(int a,int b,int c,int d) {
	return y[a][b]-y[a][d]-y[c][b]+y[c][d];
}
int gettot(int a,int b,int c,int d) {
	return tot[a][b]-tot[a][d]-tot[c][b]+tot[c][d];
}
int main()
{
	int t;
	cin >> t;
	int ca=0;
	while (++ca<=t) {
		int r,c,d;
		cin >> r >> c >> d;
		for (int i=1;i<=r;i++) {
			for (int j=1;j<=c;j++) {
				char c;
				cin >> c;
				int a=c-'0';
				tot[i][j]=a;
				h[i][j]=a;
				x[i][j]=a*i;
				y[i][j]=a*j;
				z[i][j]=a*i;
				w[i][j]=a*j;
			}
		}
		for (int i=1;i<=r;i++) {
			for (int j=1;j<=c;j++) {
				x[i][j]+=x[i-1][j]+x[i][j-1]-x[i-1][j-1];
				y[i][j]+=y[i-1][j]+y[i][j-1]-y[i-1][j-1];
				tot[i][j]+=tot[i-1][j]+tot[i][j-1]-tot[i-1][j-1];
			}
		}
		int ans=2;
		for (int i=1;i<=r;i++) {
			for (int j=1;j<=c;j++) {
				for (int k=ans+1;k<=i;k++) {
					int li=i-k;
					int lj=j-k;
					if (li<0||lj<0) break;
					int sumx=getx(i,j,li,lj);
					int sumy=gety(i,j,li,lj);
					sumx-=z[i][j]+z[li+1][j]+z[i][lj+1]+z[li+1][lj+1];
					sumy-=w[i][j]+w[li+1][j]+w[i][lj+1]+w[li+1][lj+1];
					int num=gettot(i,j,li,lj);
					num-=h[i][j]+h[li+1][j]+h[i][lj+1]+h[li+1][lj+1];
					int cx=num*(i+li+1)/2;
					int cy=num*(j+lj+1)/2;
					if (sumx==cx&&sumy==cy) ans=k;
				}
			}
		}
		if (ans>2) printf("Case #%d: %d\n",ca,ans);
		else printf("Case #%d: IMPOSSIBLE\n",ca);
	}
}