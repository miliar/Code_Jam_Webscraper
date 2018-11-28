#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

char s[110][5];
char t[110][5];
char a[110];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    int T,c,d,n,i,j,k,p,ca=1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&c);
		for(i=1;i<=c;i++)
			scanf("%s",s[i]);

		scanf("%d",&d);
		for(i=1;i<=d;i++)
			scanf("%s",t[i]);

		scanf("%d",&n);
		scanf("%s",a);

		int ok=0;
		for(i=1;i<n;i++)
		{
			ok=0;
			for(j=1;j<=c;j++)
			{
				if( ( a[i]==s[j][0] && a[i-1]==s[j][1] ) || (a[i]==s[j][1] && a[i-1]==s[j][0]) ) 
				{
                     a[i]=s[j][2];
					 a[i-1]=' ';
					 ok=1;
					 break;
				}
			}

			if(ok==1)
				continue;

			int flag=0;
			for(j=1;j<=d;j++)
			{
				flag=0;
				for(k=0;k<=i-1;k++)
				{
					if( (a[k]==t[j][0] && a[i]==t[j][1]) || (a[k]==t[j][1] && a[i]==t[j][0]) )
					{
						for(p=0;p<=i;p++)
							a[p]=' ';
						flag=1;
						break;
					}
				}
				if(flag==1)
					break;
			}
		}

		printf("Case #%d: [",ca++);
		ok=0;
		for(i=0;i<n;i++)
		{ 
		   if(a[i]!=' '&& ok==1)
			   cout<<", "<<a[i];
           if(ok==0 && a[i]!=' ')
		   {
			    cout<<a[i];
				ok=1;
		   }
		  
		}
		cout<<"]"<<endl;
	}
	return 0;
}