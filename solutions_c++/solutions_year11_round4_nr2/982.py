#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <queue>
#include <vector>
#include <stack>
#include <algorithm>
#include <sstream>
using namespace std;

const double eps=1e-10;

int r,c,d,ans;
int board[505][505];
char map[505][505];

void solve() {
	for (int i=0;i<r;i++)
		for (int j=0;j<c;j++)
			board[i][j]=d+(map[i][j]-'0');
	for (ans=min(r,c);ans>=2;ans--) {
		for (int i=0;i<r-ans+1;i++)
			for (int j=0;j<c-ans+1;j++) {
				double x=0,y=0,z=(ans+1)*1.0/2;
				for (int ii=0;ii<ans;ii++)
					for (int jj=0;jj<ans;jj++) {
						x+=board[i+ii][j+jj]*(jj-z+1);
						y+=board[i+ii][j+jj]*(ii-z+1);
					}
				x-=board[i][j]*(1-z);
				y-=board[i][j]*(1-z);
				x-=board[i][j+ans-1]*(ans-z);
				y-=board[i][j+ans-1]*(1-z);
				x-=board[i+ans-1][j]*(1-z);
				y-=board[i+ans-1][j]*(ans-z);
				x-=board[i+ans-1][j+ans-1]*(ans-z);
				y-=board[i+ans-1][j+ans-1]*(ans-z);
				x/=(ans*ans-4);
				y/=(ans*ans-4);
//				cout<<ans<<" "<<x<<" "<<y<<endl;
				if (fabs(x)<eps&&fabs(y)<eps)
					return;
			}
	}
}

int main() {
	int T,kase=0;
	cin>>T;
	while (T--) {
		cin>>r>>c>>d;
		for (int i=0;i<r;i++)
			scanf("%s",map[i]);
		solve();
		if (ans>=3)
			printf("Case #%d: %d\n",++kase,ans);
		else
			printf("Case #%d: IMPOSSIBLE\n",++kase);
	}
	return 0;
}

