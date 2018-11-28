#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()	
	{
	int n;
	char str[63];
	long long x=1;
		
	scanf("%d ",&n);
	for(int i=1; i<=n; i++)
		{
		scanf(" %s",str);
		int k=strlen(str);
		long long t=2,pow;
		char arr[130]={-1};
		long long sum=0;
		int j;
		
		memset(arr,-1,sizeof(char)*130);
		
		j=0;
		arr[str[j++]]=1;
		while(k>1 && k>j && arr[str[j]]!=-1)j++;
		
		if(k>j)	arr[str[j]]=0;
		for(; j<k; j++)
			if(arr[str[j]]==-1)
				arr[str[j]]=t++;
		
		pow=1;
		for(j=k-1; j>=0; j--)
			{
			sum += arr[str[j]]*pow;
			pow *= t;
			}
		
		printf("Case #%d: %lld\n",i,sum);
		}
	}
