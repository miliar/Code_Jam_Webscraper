#include <iostream>
#include <stdlib.h>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
int check(int num,int cnt,int A,int B)
{
	int res_c=0;
	for (int i=1;i<cnt;i++)
	{
		int num1=0;
		int digit_one=1,digit_two=1;
		for(int j=0;j<i;j++)
			digit_one=digit_one*10;
		for(int j=i;j<cnt;j++)
			digit_two=digit_two*10;
		num1=(num%digit_one)*digit_two+num/digit_one;
		int cnt2=0,x=num1;
		while(x!=0)
		{
			x/=10;
			cnt2++;
		}
		if(cnt2 == cnt && num1 <=B && num1> num)
		{
			res_c++;
		}
	}
	return res_c;
}
int main()
{
	freopen("G://GCJ/C-small.in","r",stdin);
	freopen("G://GCJ/3.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		int A,B;
		int res=0;
		scanf("%d%d",&A,&B);
		for (int j=A;j<=B;j++)
		{
			if (j < 10)
				continue;
			int cnt=0;
			int num=j;
			while(num != 0)
			{
				num=num/10;
				cnt++;
			}		
			int abcd=check(j,cnt,A,B);
			res=res+abcd;
		}
		printf("Case #%d: %d\n",i+1,res);
	}	
	return 0;
}