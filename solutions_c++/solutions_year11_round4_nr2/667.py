#include<stdio.h>
#include<queue>
#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<algorithm>
#include<math.h>

using namespace std;

#define eps 1e-6
void gcj()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("1.out","w",stdout);
	return ;
}
int n,m;
char map[510][510];
int d;

bool ok(int ans){
	for(int i = 0; i + ans <= n; i ++){
		for(int j = 0 ; j + ans <= m; j ++){
			//
			double x = i + (ans-1) / 2.0;
			double y = j + (ans-1) / 2.0;
			double tmpx = 0, tmpy = 0;
			for(int ii = i; ii < i + ans; ii ++){
					for(int jj = j; jj < j + ans; jj ++){
					if(ii == i && jj == j) continue;
					if(ii == i && jj == j + ans -1) continue;
					if( ii == i + ans -1 && jj == j) continue;
					if(ii == i + ans -1 && jj == j + ans -1 ) continue;
					tmpx += (x - ii)*(d + map[ii][jj]);
					tmpy += (y - jj)*(d + map[ii][jj]);
				}
			}
			if(fabs(tmpx) < eps && fabs(tmpy) < eps)
				return  true;
		}
	}
	return false;
}

int main()
{
	int T;
	int cas = 0;
	gcj();
	scanf("%d",&T);
	while(T--){
		cas ++;
		scanf("%d%d%d",&n,&m,&d);
		for(int i = 0 ; i < n; i ++){
			scanf("%s",&map[i]);
			for(int j = 0 ; j < m; j ++)
				map[i][j] -= '0';
		}
		int ans = min(n,m);
		for(ans; ans >= 3; ans --){
			if(ok(ans)) break;
		}
		printf("Case #%d: ",cas);
		if(ans == 2)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",ans);
	}
	return 0;
}