// Author : Muhammad Rifayat Samee
// Problem : B
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
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif




using namespace std;

map<char,char>M;
map<string,char>S;

int isin[555];
int c,d,n;


int main()
{
	//freopen("B.in","r",stdin);
	//freopen("B.txt","w",stdout);
	int cases,i,j,k,in;
	char str[150],temp[150],cur,op,res[150],ct=1;

	scanf("%d",&cases);

	while(cases--)
	{
		M.clear();
		S.clear();
		memset(isin,0,sizeof(isin));

		scanf("%d",&c);
		
		for(i=0;i<c;i++)
		{
			scanf("%s",str);

			temp[0] = str[0];
			temp[1] = str[1];
			temp[2] = NULL;

			S[temp] = str[2];

			temp[0] = str[1];
			temp[1] = str[0];
			temp[2] = NULL;
			S[temp] = str[2];



		}
		
		scanf("%d",&d);

		for(i=0;i<d;i++)
		{
			scanf("%s",str);
			
			M[str[0]] = str[1];
			M[str[1]] = str[0];

		}

		scanf("%d",&n);

		scanf("%s",str);
		in = 0;
		for(i=0;i<n;i++)
		{
			if(i==0 || in==0)
			{
				isin[str[i]]++;
				cur = str[i];
				res[in] = str[i];
				in++;
			}
			else
			{
				    op = M[str[i]];
					temp[0] = res[in-1];
					temp[1] = str[i];
					temp[2] = NULL;

					if(S.find(temp) != S.end())
					{
						isin[res[in-1]]--;
						res[in-1] = S[temp];
						
					}
					else if(isin[op])
					{	
						memset(isin,0,sizeof(isin));
						res[0] = NULL;
						in = 0;
					}
					else
					{
						res[in] = str[i];
						isin[str[i]]++;
						in++;
					}
				
			}
		}
		res[in] = NULL;
		printf("Case #%d: [",ct++);
		
		for(i=0;res[i];i++)
		{
			if(i==0)
				printf("%c",res[i]);
			else
				printf(", %c",res[i]);
		}
		
		printf("]\n");


	}

	
	return 0;


}