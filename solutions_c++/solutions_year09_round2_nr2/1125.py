#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;

int main()
{
	int t,p,i,len,j;
	scanf("%d\n",&t);
	char c;
	int num[22];
	char str[100];
	for(p=0;p<t;p++)
	{
		fgets(str,100,stdin);
		//gets(str);
		//printf("%s\n",str);
		len=strlen(str);
		len--;
		for(i=0;i<len;i++)
			num[i]=str[i]-48;
		/*for(i=0;i<len;i++)
		{
			printf("%d",num[i]);
		}*/
		if(next_permutation(num,num+len)==false)
		{
			j=0;
			for(j=0;j<len;j++)
			{
				if(num[j]!=0)
				{
					break;
				}
			}
			if(j==len)
			{
				num[len]=0;
			}
			num[0]=num[j];// 10005
			if(j!=0)
				num[j]=0;
			for(i=len;i>=2;i--)
			{
				num[i]=num[i-1];
			}
			num[1]=0;
			len++;
		}
		printf("Case #%d: ",p+1);
		for(i=0;i<len;i++)
		{
			printf("%d",num[i]);
		}
		printf("\n");
	}
	return 0;
}
