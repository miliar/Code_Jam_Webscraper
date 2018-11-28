#include <iostream>
#include<fstream>
#include <string>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include<math.h>
#include<sstream>
#include <algorithm>
#include <windows.h>   
using namespace std;
//ofstream fo("G:\\ASmallAns.txt",ios_base::out);
//char anss[100] ={0};
//::sprintf(anss,"Case #%d: %0.8lf\n",n,ans[c]);
struct aa{
	int x;
	int y;
};
int a[100];
int b[100];
int main()
{
	int i,j,n,m,t,p,ans;
	char str[100];
	//ofstream fo("G:\\ASmallAns.txt",ios_base::out);
	scanf("%d",&t);
	for (n=1;n<=t;n++)
	{
		scanf("%d",&m);
		for (i=0;i<m;i++)
		{
			scanf("%s",&str);
			a[i]=0;
			for (j=0;j<m;j++)
				if (str[j]=='1')
					a[i]=j;
			b[i]=a[i];
			
		}

		sort(b,b+m);
		ans=0;
		for (i=0;i<m;i++)
		{
			while(a[i]!=b[i])
			{
				for (j=0;j<m;j++)
				{
					//cout<<a[j]<<" ";
					if (a[j]>j)
						break;
				}
				//cout<<endl;

				if (j==m)
					break;
					

				for (j=i+1;j<m;j++)
				{
					if (a[j]==b[i])
						break;
				}
				p=a[j];a[j]=a[j-1];a[j-1]=p;
				ans++;
			}
		}

		printf("Case #%d: %d\n",n,ans);
	}
	//cin>>i;

}