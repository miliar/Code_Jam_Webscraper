#include<stdio.h>
#include<iostream>
#include<string>
#define delenter(s) if(s[strlen(s)-1] == '\n') s[strlen(s)-1] = '\0';

using namespace std;

int main()
{
	int test,n,count,s,i,j,q;
	int sum,k,flag[110];
	string S[110],query;
	char temp[125];
	
	fgets(temp,105,stdin);
	sscanf(temp,"%d",&n);
	for(test = 1;test<=n;test++)
	{
		fgets(temp,105,stdin);
		sscanf(temp,"%d",&s);
		
		memset(flag,0,110*sizeof(int));
		count = 0;
		sum = 0;
		
		for(i=0;i<s;i++)
		{
			fgets(temp,105,stdin);
			delenter(temp);
			S[i] = string(temp);
		}
		fgets(temp,105,stdin);
		sscanf(temp,"%d",&q);
		for(i=0;i<q;i++)
		{
			fgets(temp,105,stdin);
			delenter(temp);
			query = string(temp);
			for(j=0;j<s;j++)
			{
				if (query==S[j])
				{
					if (flag[j] == 0)
					{
						flag[j] = 1;
						sum++;
						if (sum == s)
						{
							for(k=0;k<s;k++)
							{
								flag[k] = 0;
							}
							flag[j] = 1;
							sum = 1;
							count++;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n",test,count);
	}
	while(getchar()!=EOF);
	return 0;
}
