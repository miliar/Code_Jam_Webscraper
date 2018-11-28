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
int two[15]={1};
int a[12][2000]={0};
int use[12][2000]={0};
int x[2000]={0};
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i,j,n,m,h,k;
	for (i=1;i<=12;i++)
		two[i] = two[i-1] * 2;
	scanf("%d\n",&t);
	for (int q=1;q<=t;++q)
	{
		cin >> h;		
		for (i=0;i<two[h];++i)
			cin >> x[i];
		for (i=0;i<two[h];i++)
			a[0][i] = use[0][i] = 0;
		for (i=1;i<=h;i++)
			for (j=0;j<two[h-i];j++)
			{
				cin >> a[i][j];
				use[i][j] = 0;
			}

		for (i=0;i<two[h];i++)
		{
			j = x[i] + 1;
			k = i / two[j];
			while (j<=h)
			{
				use[j][k] = 1;
				j++;
				k /= 2;
			}
		}
		int cnt = 0;
		for (i=0;i<=h;i++)
		{
			for (j=0;j<two[h-i];j++)
				cnt += use[i][j];
		}

		printf("Case #%d: %d\n",q,cnt);
		fflush(stdout);				
	}
	return 0;
}