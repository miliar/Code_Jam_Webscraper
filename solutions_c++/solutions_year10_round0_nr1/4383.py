#include<stdio.h>
#include<math.h>
#include<string.h>
using namespace std;

int main()
{
	int testcase,k,K,N,ar[24],alok=1,j=1,i,t;
	bool boool[24]={0};
	scanf("%d",&testcase);
	for(i=0;i<24;i++)
		ar[i]=(int)pow(2,i);
	
	while(testcase--)
	{
		scanf("%d%d",&N,&K);
		k=K;
		t=23;
		while(t>=0 && k>0)
		{
                   if(ar[t]<=k)
                   {
                   	k=k-ar[t];
                   	boool[t]=1;
                   }
                   t--;
         	}
		for(i=0;i<N;i++)
			if(!boool[i])
				alok=0;
		printf("Case #%d: ",j++);
		if(alok)
			printf("ON\n");
		else
			printf("OFF\n");
		memset(boool,0,24);
		alok=1;
	}
}
