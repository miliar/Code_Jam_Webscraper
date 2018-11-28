#include<iostream>
#include<sstream>
#include<string>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int cas=1;
	int t,i,j,k,len;
	char c[30];
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",cas);
		cas++;
		scanf("%s",c);
		len=strlen(c);
		for(i=1;i<len;i++)
			if(c[i]>c[i-1])
				break;
		if(i>=len)
		{
			for(j=len-1;j>=0;j--)
				if(c[j]!='0')
					break;
			printf("%c",c[j]);
			for(k=j;k<len;k++)
				printf("0");
			for(k=j-1;k>=0;k--)
				printf("%c",c[k]);
			printf("\n");
		}
		else
		{
			for(j=len-1;j>0;j--)
				if(c[j]>c[j-1])
					break;
			k=j-1;
			for(j=len-1;j>0;j--)
				if(c[k]<c[j])
					break;
			char tmp=c[j];
			c[j]=c[k];
			c[k]=tmp;
			for(j=0;j<=k;j++)
				printf("%c",c[j]);
			for(j=len-1;j>k;j--)
				printf("%c",c[j]);
			printf("\n");
		}
	}
	return 0;
}
