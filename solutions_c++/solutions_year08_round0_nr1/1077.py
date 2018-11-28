#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>
#include<sstream>
#include<cmath>
using namespace std;
int n,i,j,si[200];
char q[200],b[200][200],a[200];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,s,qn;
	scanf("%d",&n);
	for(t=1;t<=n;t++)
	{
		memset(si,0,sizeof(si));
		scanf("%d",&s);
		gets(a);
		for(i=0;i<s;i++)
		{
			gets(b[i]);
			
		}
		scanf("%d",&qn);gets(a);
		int sum=0,swith=0;
		for(i=0;i<qn;i++)
		{
			gets(q);
			for(j=0;j<s;j++)
				if(strcmp(q,b[j])==0)
				{
					if(si[j]==0)
					{
						si[j]=1;
						sum++;
						if(sum==s)
						{
							swith++;
							sum=1;
							memset(si,0,sizeof(si));
                            si[j]=1;
							break;
						}
						
					}

					break;
				}
				
		}
		printf("Case #%d: %d\n",t,swith);
	}
	return 0;
}