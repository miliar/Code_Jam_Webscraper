#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int main()
{
//	freopen("test.txt","r",stdin);
//	freopen("result.txt","w",stdout);
	int a[105];
	char b[105];
	int aa,bb;
	int n,m,i,j;
	int countnum;
	int index=1;
	scanf("%d",&n);
	while (n--)
	{
		scanf("%d",&m);
		for (i=0;i<m;i++)
		{
			scanf(" %c %d",&(b[i]),&(a[i]));
		}
		aa=1;bb=1;
		countnum=0;
		for (i=0;i<m;i++)
		{
			if (b[i]=='O')
			{
				
				for (j=i+1;j<m&&b[j]!='B';j++);
				int num=abs(a[i]-aa)+1;
				if (j>=m)
				{
					countnum+=(num);
					aa=a[i];
				}
				else
				{
					countnum+=(num);
					aa=a[i];
					bb=abs(a[j]-bb)<=num?a[j]:(a[j]>bb?bb+num:bb-num);
				}

			}

			else
			{
				for (j=i+1;j<m&&b[j]!='O';j++);
				int num=abs(a[i]-bb)+1;
				if (j>=m)
				{
					countnum+=(num);
					bb=a[i];
				}
				else
				{
					countnum+=(num);
					bb=a[i];
					aa=abs(a[j]-aa)<=num?a[j]:(a[j]>aa?aa+num:aa-num);
				}
			
			}

		}
		printf("Case #%d: %d\n",index++,countnum);

		
	}
//	fclose(stdin);
//	fclose(stdout);
	return 0;
}