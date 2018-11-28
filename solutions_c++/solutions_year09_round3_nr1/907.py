#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <bitset>
#include <string.h>

int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("A.out","w",stdout);

	int T;
	char a[26];
	char n[10];
	char str[64];
	char re[64];
	scanf("%d",&T);
	gets(str);
	for(int ll=0;ll<T;ll++)
	{
		gets(str);
		int len=strlen(str);
		for(int i=0;i<26;i++)
			a[i]=-1;
		for(int i=0;i<10;i++)
			n[i]=-1;
		memset(re,0,sizeof(re));
		int b=0;
		for(int i=0;i<len;i++)
		{
			if(str[i]>='a'&&str[i]<='z')
			{
				int k=str[i]-'a';
				if(a[k]==-1)
				{
					b++;
					if(b==1)
						a[k]=1;
					else if(b==2)
						a[k]=0;
					else
						a[k]=b-1;
				}
				re[i]=a[k];
			}
			else
			{
				int k=str[i]-'0';
				if(n[k]==-1)
				{
					b++;
					if(b==1)
						n[k]=1;
					else if(b==2)
						n[k]=0;
					else
						n[k]=b-1;
				}
				re[i]=n[k];
			}
		}	
		__int64 t=0;
		if (b==1)
			b=2;
		for(int i=0;i<len;i++)
			t=t*b+re[i];
		if(len>1)
			printf("Case #%d: %I64d\n",ll+1,t);
		else
			printf("Case #%d: 1\n",ll+1);
	}
}