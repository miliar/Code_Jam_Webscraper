#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <math.h>
#pragma comment (linker,"/STACK:16000000")
using namespace std;
const int maxn = 110;
char mas[maxn][maxn]={0};
char mas2[maxn][maxn]={0};
void rotate(int n)
{
	int i,j,ii;
	for (i=1;i<=n;i++)
	{
		for (j=1;j<=n;j++)
		{
			mas2[j][n-i+1] = mas[i][j];
		}
	}
	for (i=1;i<=n;i++)
		for (j=1;j<=n;j++)
			mas[i][j] = mas2[i][j];
	for (j=1;j<=n;j++)
	{
		for (i=n;i>=1;i--)
		{
			if (mas[i][j]=='.')
			{
				for (ii=i-1;ii>=1;ii--)
				{
					if (mas[ii][j]!='.')
					{
						mas[i][j] = mas[ii][j];
						mas[ii][j] = '.';
						break;
					}
				}
			}
		}
	}
	return;
}
bool getcnt(char ch, int n, int k)
{
	int i,j,w,cnt;
	for (i=1;i<=n;i++)
	{
		j = 1;
		while (j<=n)
		{
			w = j;
			while (w<n && mas[i][w]==mas[i][w+1])
				++w;
			cnt = w - j + 1;
			if (mas[i][j]==ch && cnt>=k)
				return true;
			j = w + 1;
		}
	}

	for (i=1;i<=n;i++)
	{
		j = 1;
		while (j<=n)
		{
			w = j;
			while (w<n && mas[w][i]==mas[w+1][i])
				++w;
			cnt = w - j + 1;
			if (mas[j][i]==ch && cnt>=k)
				return true;
			j = w + 1;
		}
	}

	int str,stb;
	for (i=1;i<=n;i++)
	{
		for (j=1;j<=n;j++)
		{
			if (mas[i][j]!=ch)
				continue;
			str = i;
			stb = j;
			while (str<=n && stb<=n && mas[str][stb]==mas[i][j])
			{
				++str;
				++stb;
			}
			cnt = str - i;
			if (cnt>=k)
				return true;
			str = i;
			stb = j;
			while (str<=n && stb>=1 && mas[str][stb]==mas[i][j])
			{
				++str;
				--stb;
			}
			cnt = str - i;
			if (cnt>=k)
				return true;
		}
	}
	return false;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i,j,n,m;
	//scanf("%d\n",&t);
	cin >> t;
	bool a,b;
	int k;
	for (int q=1;q<=t;++q)
	{
		printf("Case #%d: ",q);
		//scanf("%d %d",&n,&k);
		cin >> n >> k;
		for (i=1;i<=n;i++)
		{
			for (j=1;j<=n;++j)
			{
				cin >> mas[i][j];
			}
		}
		rotate(n);
		a = getcnt('R',n,k);
		b = getcnt('B',n,k);
		if (a && b)
			printf("Both\n");
		else if (a)
			printf("Red\n");
		else if (b)
			printf("Blue\n");
		else 
			printf("Neither\n");
	}
	return 0;
}