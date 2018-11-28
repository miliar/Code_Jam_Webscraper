// Author : Muhammad Rifayat Samee
// Problem : A 
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>

#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif

using namespace std;

char str[55][55];
int n,m;


int isvalid(int i,int j)
{
	if(i>=0&&i<n && j>=0&&j<m)return 1;
	return 0;

}

int main()
{
	//freopen("a_l.in","r",stdin);
	//freopen("a_out.txt","w",stdout);
	
	int cases,i,j,k,f,ct=1;

	scanf("%d",&cases);

	while(cases--)
	{
		scanf("%d %d",&n,&m);

		for(i=0;i<n;i++)
		{
			scanf("%s",str[i]);
		}

		f = 0;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(str[i][j] == '#')
				{
					if(str[i][j+1] == '#' && isvalid(i,j+1))
					{
						str[i][j] = '/';
						str[i][j+1] = '\\';

					}
					else
					{
						f = 1;
						break;
					}
					
					if(str[i+1][j] == '#' && isvalid(i+1,j) && str[i+1][j+1]=='#' && isvalid(i+1,j+1))
					{
						str[i+1][j] = '\\';
						str[i+1][j+1] = '/';

					}
					else
					{
						f = 1;
						break;
					}

				}
			}
		}
		printf("Case #%d:\n",ct++);
		if(f==1)
			printf("Impossible\n");
		else
		{
			
			for(i=0;i<n;i++)
				printf("%s\n",str[i]);
		}
	}
	return 0;


}
