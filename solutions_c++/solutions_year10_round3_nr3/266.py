#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <set>
using namespace std;
unsigned long long hash[512][512][513];
char map[512][512];
char str[300];
char chk[512][512];
struct point{
	int x,y;
	point(int xx=0,int yy=0){
		x=xx;y=yy;
	}
};
bool operator<(const point& a,const point& b){
	if(a.x!=b.x)
		return a.x<b.x;
	return a.y<b.y;
}
int res[513];
unsigned long long pattern[513][2];
void build_pattern(int m,int n)
{
	int mymin=m;
	if(mymin>n)
		mymin=n;
	int i,j,k;
	pattern[1][0]=0;
	pattern[1][1]=1;
	for(k=2;k<=mymin;k++){
		pattern[k][0]=pattern[k-1][0]+(pattern[k-1][1]<<16)+(pattern[k-1][1]<<32)+(pattern[k-1][0]<<48);
		pattern[k][1]=pattern[k-1][1]+(pattern[k-1][0]<<16)+(pattern[k-1][0]<<32)+(pattern[k-1][1]<<48);
	}
}
void init(int m,int n)
{
	for(int i=0;i<m;i++){
		gets(str);
		int j=0;
		char* p=str;
		while(*p){
			int num=0;
			if(*p>='0' && *p<='9')
				num=*p-'0';
			else
				num=*p-'A'+10;
			for(int k=3;k>=0;k--){
				if((1<<k)&num)
					map[i][j]=1;
				else
					map[i][j]=0;
				j++;
			}
			p++;
		}
	}
}
void build_hash(int m,int n)
{
	int i,j,k;
	for(k=1;k<=m && k<=n;k++)
	{
		for(i=0;i<m;i++){
			if(m-i<k)
				break;
			for(j=0;j<n;j++)
			{
				if(k==1){
					hash[i][j][k]=map[i][j];
				}else{
					if(n-j<k)
						break;
					hash[i][j][k]=hash[i][j][k-1]+(hash[i][j+1][k-1]<<16)+(hash[i+1][j][k-1]<<32)+(hash[i+1][j+1][k-1]<<48);
				}
			}
		}
	}
}
bool pipei(int m,int n,int x,int y,int k,int start)
{
	for(int i=x;i<x+k;i++)
		for(int j=y;j<y+k;j++){
			int dis=i-x+j-y;
			dis&=1;
			if(chk[i][j]==1 || dis^start!=map[i][j])
				return false;
		}
	return true;
}
void sets(int x,int y,int k){
	for(int i=x;i<x+k;i++)
		for(int j=y;j<y+k;j++)
			chk[i][j]=1;
}
void solve(int m,int n)
{
	int mymin=m;
	if(mymin>n)
		mymin=n;
	memset(res,0,sizeof(res));
	int i,j,k;
	for(k=mymin;k>=1;k--){
		for(i=0;i<m;i++){
			if(m-i<k)
				break;
			for(j=0;j<n;j++){
				if(n-j<k)
					break;
				if(chk[i][j])
					continue;
				if(hash[i][j][k]==pattern[k][0]){
					if(pipei(m,n,i,j,k,0)){
						res[k]++;
						sets(i,j,k);
						continue;
					}
				}
				if(hash[i][j][k]==pattern[k][1]){
					if(pipei(m,n,i,j,k,1)){
						res[k]++;
						sets(i,j,k);
						continue;
					}
				}
			}
		}
	}
}
int main()
{
	build_pattern(512,512);
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		int i,j,k;
		int n,m;
		scanf("%d%d",&m,&n);
		getchar();
		init(m,n);
		build_hash(m,n);
		memset(chk,0,sizeof(chk));
		solve(m,n);
		int ans=0;
		for(i=1;i<=m && i<=n;i++)
			if(res[i])
				ans++;
		printf("Case #%d: %d\n",cas,ans);
		int mymin=(m<n?m:n);
		for(i=mymin;i>=1;i--){
			if(res[i])
				printf("%d %d\n",i,res[i]);
		}
	}
	return 0;
}

