#include<iostream>
#include<stdio.h>
#include<memory.h>
#include<map>
#include<vector>
using namespace std;
char a[5001][3000];
char aa[3000];
__int64 q,xx;
int main()
{
	int n;
	int ca,i,l,d,k,qq,j;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	for(i=0;i<d;i++)
	{
		scanf("%s",a[i]);
	}
	for(ca=1;ca<=n;ca++)
	{
		scanf("%s",aa);
		int sum=0;
		for(i=0;i<d;i++)
		{
			k=0;
			for(j=0;aa[j];j++)
			{
				if(aa[j]=='(')
				{
					for(qq=j+1;aa[qq]!=')';qq++)
					{
						if(aa[qq]==a[i][k])
							break;
					}
					if(aa[qq]==')')
						break;
					for(;aa[qq]!=')';qq++) ;
					j=qq;
				}
				else if(aa[j]!=a[i][k])
					break;
				k++;
			}
			if(aa[j]==0)
				sum++;
		}
		printf("Case #%d: %d\n",ca,sum);
	}
	return 0;
}
