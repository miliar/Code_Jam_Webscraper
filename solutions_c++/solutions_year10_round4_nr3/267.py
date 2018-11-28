#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
using namespace std;

const int maxn = 100+10;
int r;
bool mat[maxn][maxn];

int main(){
	int tc,tt;
	cin>>tc;
	for(tt=1;tt<=tc;tt++){
		printf("Case #%d: ",tt);
		cin>>r;
		memset(mat,0,sizeof(mat));
		int i,j;
		int x1,x2,y1,y2;
		int cnt = 0;
		for(i=0;i<r;i++){
			cin>>y1>>x1>>y2>>x2;
			for(;x1<=x2;x1++){
				int ty;
				for(ty = y1;ty<=y2;ty++)
					if(!mat[x1][ty])
						mat[x1][ty]=true,cnt++;
			}
		}
		/*for(i=1;i<=6;i++){
				for(j=1;j<=6;j++)
					cout<<mat[i][j]<<' ';
				cout<<endl;
			}
			cout<<endl;*/
		int ans = 0;
		while(cnt>0){
			cnt = 0;
			for(i=100;i>=1;i--)
				for(j=100;j>=1;j--){
					if(mat[i][j] && (i==1||j==1||!mat[i][j-1]&&!mat[i-1][j]))
						mat[i][j] = false;
					else
					if(!mat[i][j] && (i>1 && j>1 && mat[i][j-1] && mat[i-1][j]))
					{
						mat[i][j] = true;
					}
					if(mat[i][j])cnt++;
				}
/*			for(i=1;i<=5;i++){
				for(j=1;j<=5;j++)
					cout<<mat[i][j]<<' ';
				cout<<endl;
			}
			cout<<endl;*/
			ans++;
		}
		cout<<ans<<endl;
	}

	return 0;
}
