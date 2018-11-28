#include <cstdio>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
int main()
{
	int test,Test;
	scanf("%d",&Test);
	long long X,Y,M;
	long long counter;
	long long s1,s2,s3;
	int i,n,A,B,C,D,i1,i2,i3;
	int x1,x2,x3,y1,y2,y3;
	for (test=1;test<=Test;test++)
	{
		scanf("%d %d %d %d %d %lld %lld %lld",&n,&A,&B,&C,&D,&X,&Y,&M);
//		printf("%d %d %d %d %d %lld %lld %lld\n",n,A,B,C,D,X,Y,M);
		long long a[3][3]={0};
		a[X%3][Y%3]++;
		for (i=1;i<n;i++)
		{
			X=(A*X+B)%M;
			Y=(C*Y+D)%M;
			a[X%3][Y%3]++;
		}
		counter=0;
	/*	for (X=0;X<3;X++)
		{
			for (Y=0;Y<3;Y++)
			printf("%5lld ",a[X][Y]);
			printf("\n");
		}
	*/	for (i1=0;i1<9;i1++)
		{	
			x1=i1/3;
			y1=i1%3;
			s1=a[x1][y1];
			a[x1][y1]--;
			if (s1)
			for (i2=i1;i2<9;i2++)
			{
				x2=i2/3;
				y2=i2%3;
				s2=s1*a[x2][y2];
				a[x2][y2]--;
				if (s2)
				for (i3=i2;i3<9;i3++)
				{
					x3=i3/3;
					y3=i3%3;
					s3=s2*a[x3][y3];
					//printf("%d %d %d %d %d %d %lld\n",x1,y1,x2,y2,x3,y3,s3);
					if ((x1+x2+x3)%3==0&&(y1+y2+y3)%3==0)
					{
						if (i1==i2&&i1==i3) s3/=6;
						else if (i1==i2||i2==i3||i1==i3) s3/=2;
						counter+=s3;
					}
				}
				a[x2][y2]++;
			}
			a[x1][y1]++;
		}
		printf("Case #%d: %lld\n",test,counter);
	}
  	return 0;
}
