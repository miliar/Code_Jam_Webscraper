#include <cctype>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;
int two(int num);
int three(int num);
int a,b,check[1001];
int main() {
int i,j,k,n,count;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("outputproblemc.txt","w",stdout);
	while(scanf("%d",&n)==1)
	{
		for(i=1;i<=n;i++)
		{
			scanf("%d %d",&a,&b);
			count=0;
			for(k=0;k<=1000;k++)
			{
				check[k]=0;
			}
			for(j=a;j<=b;j++)
			{
				if(j>=10&&j<100)
				{
					count+=two(j);
				}
				else if(j>=100&&j<1000)
				{
					//printf("=============\n");
					count+=three(j);
					//printf("==============\n");
				}
			}
			printf("Case #%d: %d\n",i,count);
		}
	}
	fclose(stdout);
	fclose(stdin);
	return 0;
}
int two(int num)
{
	int div,number,mod;
	if(num%10!=0&&num%11!=0)
	{
		div=num/10;
		mod=num%10;
		number=(mod*10)+div;
		//printf("===>%d %d %d %d %d\n",a,num,number,b,check[number]);
		if(number>=a&&number<=b&&check[number]==0)
		{
        //printf("===>%d %d\n",num,number);
			check[num]=1;
			check[number]=1;
			return 1;
		}
	}
	return 0;
}
int three(int num)
{
	int div,number,mod,d;
	d=0;
	if(num%100!=0&&num%111!=0)
	{
		div=num/100;
		mod=num%100;
		number=(mod*10)+div;
//printf("1===>%d %d %d %d %d\n",a,num,number,b,check[number]);
		if(number>=a&&number<=b&&check[number]==0)
		{
        //printf("Count===>%d %d\n",num,number);
			check[num]=1;
			//check[number]=1;
			d++;
		}
        div=num/10;
        mod=num%10;
        number=(mod*100)+div;
//printf("2===>%d %d %d %d %d\n",a,num,number,b,check[number]);
        if(number>=a&&number<=b&&check[number]==0)
        {
// printf("Count===>%d %d\n",num,number);
		check[num]=1;
            	//check[number]=1;
            d++;
        }

	}
	return d;
}

