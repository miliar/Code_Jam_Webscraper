// Author : Muhammad Rifayat Samee
// Problem : C
// Algorithm:
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

using namespace std;

int main()
{
	//freopen("C.in","r",stdin);
	//freopen("C.out","w",stdout);
	
	int r,c,i,j,k,cases,n,ct=1,total,num,f;
	
	scanf("%d",&cases);
	while(cases--)
	{
		scanf("%d %d %d",&r,&k,&n);
		
		
		
		queue<int>Q;
		queue<int>q;
		for(i=0;i<n;i++)
		{
			scanf("%d",&num);
			Q.push(num);
		}

		total = 0;

		for(i=0;i<r;i++)
		{
			num = 0;
			
			while(!Q.empty() && num<=k)
			{
				f = Q.front();
				num = num + f;
				
				
				if(num>k)
				{
					num = num - f;
					break;
				}
				q.push(f);
				Q.pop();
				
			}
			total = total + num;
			
			while(!q.empty())
			{
				Q.push(q.front());
				q.pop();

			}
		}

		printf("Case #%d: %d\n",ct++,total);

	}


	return 0;


}