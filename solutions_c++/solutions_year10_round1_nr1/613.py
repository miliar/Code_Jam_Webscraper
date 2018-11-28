
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
int n,k;
char orgin[50][52];
char rotated[50][52];

void gravity()
{
// 	for(int i=0;i<n;++i)
// 		printf("%s\n",rotated[i]);
// 	printf("\n");
	for(int j=0;j<n;++j){
		int top=n-1;
		while(top>=0&&rotated[top][j]!='.')	--top;
		for(int i=top-1;i>=0;--i){
			if(rotated[i][j]!='.'){
				rotated[top][j]=rotated[i][j];
				rotated[i][j]='.';
				--top;
			}
		}
	}
// 	for(int i=0;i<n;++i)
// 		printf("%s\n",rotated[i]);
}

bool judgeSingle(int row,int col)
{
	//shuiping
	int count=1;
	for(int i=1;i<=col&&rotated[row][col-i]==rotated[row][col];++i)	++count;
	for(int i=1;i+col<n&&rotated[row][col+i]==rotated[row][col];++i)	++count;
	if(count>=k)		return true;
	//shuzhi
	count =1 ;
	for(int i=1;i<=row&&rotated[row-i][col]==rotated[row][col];++i)	++count;
	for(int i=1;i+row<n&&rotated[row+i][col]==rotated[row][col];++i)	++count;
	if(count>=k)		return true;
	//主对角线
	count =1 ;
	for(int i=1;i<=row&&i<=col&&rotated[row-i][col-i]==rotated[row][col];++i)	++count;
	for(int i=1;i+row<n&&i+col<n&&rotated[row+i][col+i]==rotated[row][col];++i)	++count;
	if(count>=k)		return true;
	//副对角线
	count =1 ;
	for(int i=1;i<=row&&i+col<n&&rotated[row-i][col+i]==rotated[row][col];++i)	++count;
	for(int i=1;i+row<n&&i<=col&&rotated[row+i][col-i]==rotated[row][col];++i)	++count;
	if(count>=k)		return true;
	return false;
}

string judgeAll()
{
	bool r=false,b=false;
	for(int i=0;i<n;++i){
		for(int j=0;j<n;++j){
			if(!r&&rotated[i][j] == 'R'&&judgeSingle(i,j))	r=true;
			if(!b&&rotated[i][j]=='B'&&judgeSingle(i,j))	b=true;
			if(r&&b)	return "Both";
		}
	}
	if(r) return "Red";
	if(b)	return "Blue";
	return "Neither";
}

int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;++i){
			scanf("%s",orgin[i]);
			for(int j=0;j<n;++j)
				rotated[j][n-i-1] = orgin[i][j];
		}
		gravity();
		printf("Case #%d: %s\n",t,judgeAll().c_str());
	}
	return 0;
}