#include "StdAfx.h"
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#include <cstdlib>
#include <vector>
//#include <map>
#include <set>
#include <stdlib.h>
#include <algorithm>
#define eps 1e-10
#define MAX 1000000000
using namespace std;


char map[11][11];
int mat[11][11];

int main()
{
	freopen("out.txt","w",stdout);
	int repeat,i,j,k,m,n,p,q,ans;
	double D;
	int cases=1;
	cin>>repeat;
	while(repeat--)
	{
		cin>>m>>n>>D;
		for(i=1;i<=m;i++)
			for(j=1;j<=n;j++)
			{
				cin>>map[i][j];
			}
			printf("Case #%d: ",cases++);
			ans=-1;
		for(k=3;k<=min(n,m);k++)
		{
			for(i=1;i<=m;i++)
				for(j=1;j<=n;j++)
				{
					if(i+k-1>m||j+k-1>n)
						continue;
					for(p=1;p<=k;p++)
						for(q=1;q<=k;q++)
						{
							mat[p][q]=map[i+p-1][j+q-1]-'0'+D;
						}
						double a1,b1,a2,b2,x,y;
						a1=b1=a2=b2=0;
					for(p=1;p<=k;p++)
						for(q=1;q<=k;q++)
						{
							if(p==1&&q==1)
								continue;
							if(p==1&&q==k)
								continue;
							if(p==k&&q==1)
								continue;
							if(p==k&&q==k)
								continue;
							a1+=mat[p][q]*p;
							b1+=mat[p][q];
							a2+=mat[p][q]*q;
							b2+=mat[p][q];
						}
					x=a1/b1;
					y=a2/b2;
					if(fabs(x-(1+k)/2.0)<eps&&fabs(y-(1+k)/2.0)<eps)
						ans=k;
						

				}

		}
		if(ans==-1)
			cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}

}