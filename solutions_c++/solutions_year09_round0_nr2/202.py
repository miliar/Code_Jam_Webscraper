#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;
char b[102][102];
int a[102][102];
char c;
char paint(int i,int j){
	if (b[i][j]) return b[i][j];
	else{
		int x=i-1,y=j;
		if (a[i][j-1]<a[x][y]) x=i,y=j-1;
		if (a[i][j+1]<a[x][y]) x=i,y=j+1;
		if (a[i+1][j]<a[x][y]) x=i+1,y=j;
		if (a[i][j]<=a[x][y]) 
			b[i][j]=c++;
		else
			b[i][j]=paint(x,y);
		return b[i][j];
	}
}
int main(){
	int N,i,j,n,H,W;
	vector<pair<int, pair<int,int> > >::iterator it;
	for (i=0;i<102;i++){
		a[0][i]=10000;
		a[i][0]=10000;
	}
	scanf("%d\n",&N);
	for (n=1;n<=N;n++){
		scanf("%d%d",&H,&W);
		vector<pair<int, pair<int,int> > >v;
		for (i=1;i<=H;i++)
			for (j=1;j<=W;j++){
				scanf("%d",&a[i][j]);
				b[i][j]=0;
				v.push_back(make_pair(a[i][j],make_pair(i,j)));
			}
		sort(v.begin(),v.end());
		for (i=0;i<=H+1;i++)
			a[i][W+1]=10000;
		for (j=0;j<=W;j++)
			a[H+1][j]=10000;
		c='a';
		for (i=1;i<=H;i++)
			for (j=1;j<=W;j++)
			if (!b[i][j])
				b[i][j]=paint(i,j);
		printf("Case #%d:\n",n);
		for (i=1;i<=H;i++){
			for (j=1;j<=W;j++)
			printf("%c ",b[i][j]);
			printf("\n");
		}
	}
	return 0;
}
