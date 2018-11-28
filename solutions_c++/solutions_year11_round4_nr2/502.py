#pragma comment(linker,"/STACK:16777216")
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<cstring>
#include<ctime>
#include<cmath>
#include<functional>

using namespace std;

#define ll long long
#define ld long double
#define si short int
#define pii pair<int,int>
#define vi vector<int>
#define vit vector<int>::iterator
#define sq(x) (x)*(x)

bool valid(char** mas,int x, int y, int k, ll** sumWs, ll** sumXs, ll** sumYs)
{
	ll sumW=sumWs[x+k][y+k]-sumWs[x][y+k]-sumWs[x+k][y]+sumWs[x][y]-mas[x][y]-mas[x][y+k-1]-mas[x+k-1][y]-mas[x+k-1][y+k-1]+4*'0',
		sumXW=sumXs[x+k][y+k]-sumXs[x][y+k]-sumXs[x+k][y]+sumXs[x][y]-(mas[x][y]-'0')*x-(mas[x][y+k-1]-'0')*x-(mas[x+k-1][y]-'0')*(x+k-1)-(mas[x+k-1][y+k-1]-'0')*(x+k-1),
		sumYW=sumYs[x+k][y+k]-sumYs[x][y+k]-sumYs[x+k][y]+sumYs[x][y]-(mas[x][y]-'0')*y-(mas[x][y+k-1]-'0')*(y+k-1)-(mas[x+k-1][y]-'0')*(y)-(mas[x+k-1][y+k-1]-'0')*(y+k-1);
	return 2*sumXW==(x*2+k-1)*sumW && 2*sumYW == (y*2+k-1)*sumW;
}

bool validAll(char** mas, int k, int r, int c, ll** sumWs, ll** sumXs, ll** sumYs)
{
	for(int i=0; i+k<=r; ++i)
		for(int j=0; j+k<=c; ++j)
			if(valid(mas,i,j,k, sumWs, sumXs, sumYs))
				return true;
	return false;
}

void test(int id)
{
	int r,c,d;
	scanf("%d%d%d",&r,&c,&d);
	char** mas=new char*[r];
	ll** sumWs=new ll*[r+1];
	ll** sumXs=new ll*[r+1];
	ll** sumYs=new ll*[r+1];
	for(int i=0; i<r; ++i)
	{
		mas[i]=new char[c+5];
		scanf("%s",mas[i]);
	}
	for(int i=0; i<=r; ++i)
	{
		sumWs[i]=new ll[c+1];
		sumXs[i]=new ll[c+1];
		sumYs[i]=new ll[c+1];
	}
	for(int i=0; i<=r; ++i)
	{
		sumWs[i][0]=sumXs[i][0]=sumYs[i][0]=0;
	}
	for(int j=0; j<=c; ++j)
	{
		sumWs[0][j]=sumXs[0][j]=sumYs[0][j]=0;
	}
	for(int i=1; i<=r; ++i)
	{
		for(int j=1; j<=c; ++j)
		{
			sumWs[i][j]=sumWs[i-1][j]+sumWs[i][j-1]-sumWs[i-1][j-1]+mas[i-1][j-1]-'0';
			sumXs[i][j]=sumXs[i-1][j]+sumXs[i][j-1]-sumXs[i-1][j-1]+(mas[i-1][j-1]-'0')*(i-1);
			sumYs[i][j]=sumYs[i-1][j]+sumYs[i][j-1]-sumYs[i-1][j-1]+(mas[i-1][j-1]-'0')*(j-1);
		}
	}
	for(int i=min(r,c); i>=3; --i)
		if(validAll(mas,i,r,c, sumWs, sumXs, sumYs))
		{
			printf("Case #%d: %d\n",id,i);
			return ;
		}
	printf("Case #%d: IMPOSSIBLE\n",id);
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=1; i<=t; ++i)
		test(i);
	return 0;
}