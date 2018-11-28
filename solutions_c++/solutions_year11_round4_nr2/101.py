#include <iostream>
#include <string>
#include <cstring>
#include <string.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <math.h>

using namespace std;

char s[510][510];
double sumx[510][510];
double sumy[510][510];
double x[510][510];
double y[510][510];
double m[510][510];
double summ[510][510];

void solve(int tst){
	int n,mm,d;
	scanf("%d%d%d\n",&n,&mm,&d);
	for (int i=0; i<n; i++){
		for (int j=0; j<mm; j++){
			scanf("%c",&s[i][j]);
			x[i][j]=(i+0.5)*(d+(double)(s[i][j]-'0'));
			y[i][j]=(j+0.5)*(d+(double)(s[i][j]-'0'));
			m[i][j]=d+(double)(s[i][j]-'0');
		}
		scanf("\n");
	}

	sumx[0][0]=x[0][0], sumy[0][0]=y[0][0];
	summ[0][0]=m[0][0];
	for (int i=1; i<mm; i++)
		sumx[0][i]=sumx[0][i-1]+x[0][i],
		sumy[0][i]=sumy[0][i-1]+y[0][i],
		summ[0][i]=summ[0][i-1]+m[0][i];

	for (int i=1; i<n; i++)
		sumx[i][0]=sumx[i-1][0]+x[i][0],
		sumy[i][0]=sumy[i-1][0]+y[i][0],
		summ[i][0]=summ[i-1][0]+m[i][0];

	for (int i=1; i<n; i++)
		for (int j=1; j<mm; j++){
			sumx[i][j]=x[i][j]+sumx[i-1][j]+sumx[i][j-1]-sumx[i-1][j-1];
			sumy[i][j]=y[i][j]+sumy[i-1][j]+sumy[i][j-1]-sumy[i-1][j-1];
			summ[i][j]=m[i][j]+summ[i-1][j]+summ[i][j-1]-summ[i-1][j-1];
		}

	int res=2;
	int xx=0;
	int yy=0;
	for (int i=0; i<n; i++)
		for (int j=0; j<mm; j++)
			for (int k=res+1; i+k-1<n&&j+k-1<mm; k++){
				double sx=sumx[i+k-1][j+k-1]-sumx[i-1][j+k-1]-sumx[i+k-1][j-1]+sumx[i-1][j-1];
				double sy=sumy[i+k-1][j+k-1]-sumy[i-1][j+k-1]-sumy[i+k-1][j-1]+sumy[i-1][j-1];
				double sm=summ[i+k-1][j+k-1]-summ[i-1][j+k-1]-summ[i+k-1][j-1]+summ[i-1][j-1];
				sx-=x[i][j]+x[i+k-1][j]+x[i+k-1][j+k-1]+x[i][j+k-1];
				sy-=y[i][j]+y[i+k-1][j]+y[i+k-1][j+k-1]+y[i][j+k-1];
				sm-=m[i][j]+m[i+k-1][j]+m[i+k-1][j+k-1]+m[i][j+k-1];

				double cx=sx/sm;
				double cy=sy/sm;
				if (fabs(cx-((2*i+k)/2.0))<1e-9&&
					fabs(cy-((2*j+k)/2.0))<1e-9){
						res=k;
						xx=i;
						yy=j;
				}
			}
			//cout<<xx<<" "<<yy<<endl;

	/*double curx=0, cury=0,curm=0;
	for (int i=xx; i<xx+res; i++)
		for (int j=yy; j<yy+res; j++){
			curx+=x[i][j], cury+=y[i][j], curm+=m[i][j];
		}
	curx-=x[xx][yy]+x[xx+res-1][yy]+x[xx+res-1][yy+res-1]+x[xx][yy+res-1];
	cury-=y[xx][yy]+y[xx+res-1][yy]+y[xx+res-1][yy+res-1]+y[xx][yy+res-1];
	curm-=m[xx][yy]+m[xx+res-1][yy]+m[xx+res-1][yy+res-1]+m[xx][yy+res-1];

	printf("%.10lf %.10lf\n",curx/curm,cury/curm);
	printf("%.10lf %.10lf\n",(xx+xx+res)/2.0,(yy+yy+res)/2.0);*/
	if (res!=2)	printf("Case #%d: %d\n",tst,res); else
		printf("Case #%d: IMPOSSIBLE\n",tst);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d\n",&tests);

	for (int tt=1; tt<=tests; tt++){
		solve(tt);
	}

	return 0;
}