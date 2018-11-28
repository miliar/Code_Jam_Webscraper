#include <stdio.h>

char str[300*15];

int pos[30][30];

int parse(int st, int i)
{
	int j;
	for(j=0;j<30;++j)
		pos[i][j]=0;
	if(str[st]<='z' && str[st]>='a')
	{
		pos[i][str[st]-'a']=1;
		return st+1;
	}
	for(j=st+1;str[j]!=')';++j)
		pos[i][str[j]-'a']=1;
	return j+1;
}

int main()
{
	int n,m,l;
	char w[5100][30];
	int resp;
	int i,j,k;
	scanf("%d %d %d",&l,&n,&m);
	for(i=0;i<n;++i)
		scanf("%s",w[i]);
	for(i=0;i<m;++i)
	{
		resp=0;
		scanf("%s",str);
		k=0;
		for(j=0;str[k];++j)
			k=parse(k,j);
		for(j=0;j<n;++j)
		{
			for(k=0;k<l;++k)
				if(!pos[k][w[j][k]-'a'])
					break;
			if(k==l)
				++resp;
		}
		printf("Case #%d: %d\n",i+1,resp);
	}
	return 0;
}

