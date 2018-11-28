#include <cstdio>
#include <ctime>
#include <cstring>
#include <assert.h>
#include <iostream>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
bool mat[2][101][101];
void trans()
{
	for(int i=0;i<=100;++i)
		for(int j=0;j<=100;++j){
			if(mat[0][i][j]){
				bool alive = false;
				if(i>0 && mat[0][i-1][j])	alive = true;
				if(j>0 && mat[0][i][j-1])	alive = true;
				if(i==0 && j==0)	alive = false;
				mat[1][i][j] = alive;
			}
			else{
				bool alive = true;
				if(i>0 && !mat[0][i-1][j])	alive = false;
				if(j>0 && !mat[0][i][j-1])	alive = false;
				if(i==0 && j==0)	alive = false;
				mat[1][i][j] = alive;
			}
		}
		for(int i=0;i<=100;++i)
			for(int j=0;j<=100;++j)
				mat[0][i][j] = mat[1][i][j];
}
bool check()
{
	for(int i=0;i<=100;++i)
		for(int j = 0;j<=100;++j)
			if(mat[0][i][j])	return false;
	return true;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int C;
	cin>>C;
	int x1,y1,x2,y2;
	for(int c=1;c<=C;++c){
		int r;
		cin>>r;
		memset(mat,0,sizeof mat);
		while(r--){
			cin>>x1>>y1>>x2>>y2;
			for(int i=x1;i<=x2;++i)
				for(int j=y1;j<=y2;++j)
					mat[0][i][j] = 1;
		}
		int res;
		for(res = 0;!check();++res){
			trans();
		}
		cout<<res<<endl;
	}
	return 0;
}