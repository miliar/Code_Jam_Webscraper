#include <vector>
#include <string>
#include <list>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include<iostream>
using namespace std;
int T,N;
int matrix[50][50];
bool check[50]; 
bool ischeck(int a[50],int b)
{
	for(int ii = b;ii < N;ii++)
	{
		if(a[ii] == 1)
			return false;
	}
	return true;
}
int main()
{
	freopen("..\\A-large.in","r",stdin);
	freopen("..\\A.out","w",stdout);
	scanf("%d",&T);
	for(int i = 1;i <= T;i++)
	{
		printf("Case #%d: ",i);
		scanf("%d",&N);
		int res = 0;
		string sss;
		for(int j = 0;j < N;j++)
		{
			cin>>sss;
			for(int k = 0;k < sss.size();k++)
				matrix[j][k] = sss[k] - '0';
		}
		memset(check,false,sizeof(check));
		for(int j = 1;j <= N;j++)
		{
			int cc = 0;
			bool flag = false;
			for(int k = 0;k < N;k++)
			{
				if(!check[k])
				{
					if(ischeck(matrix[k],j))
					{
						flag = true;
						check[k] = true;
					}
					cc++;
				}
				if(flag)
					break;
			}
			res += cc - 1;
		}
		printf("%d\n",res);
	}
	return 0;
}