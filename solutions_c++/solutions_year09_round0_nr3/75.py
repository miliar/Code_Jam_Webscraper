#include <stdio.h>

#define MAX 1000

int main()
{
	char str[MAX];
	char wel[]="welcome to code jam";
	int v[MAX];
	int len;
	int i,j,k;
	int ccnt,ncase;
	int resp;
	scanf("%d ",&ncase);
	for(ccnt=1;ccnt<=ncase;++ccnt)
	{
		gets(str);
		for(i=0;str[i];++i)
			v[i]= (str[i]==wel[0]);
		len=i;
		for(i=1;wel[i];++i)
		{
			for(j=len-1;j>=0;--j)
			{
				v[j]=0;
				if(str[j]==wel[i])
					for(k=0;k<j;++k)
						v[j]+=v[k];
				v[j]%=10000;
			}
		}
		resp=0;
		for(i=0;str[i];++i)
			resp+=v[i];
		printf("Case #%d: %04d\n",ccnt,resp%10000);
	}
	return 0;
}

