#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>

void change(char &a,char &b)
{
	char tmp=a;
	a=b;
	b=tmp;
}

void main()
{
	if(!freopen("B-large (1).in","r",stdin)) exit(0);
	if(!freopen("B-large (1).out","w",stdout)) exit(0);
	
	int i,j,k,t,n,length,flag;
	int T;
	char N[24],tmp;
	int cnt;
	scanf("%d",&T);
	for(cnt=1;cnt<=T;cnt++)
	{
		scanf("%s",N);
		length=strlen(N);
		flag=1;
		for(i=length-1;i>0;i--)
		{
			if(N[i]>N[i-1])
			{
				t=i;
				for(j=i+1;j<length;j++)
					if(N[i-1]<N[j]&&N[j]<N[t])
						t=j;
				change(N[t],N[i-1]);
				for(j=i;j<length-1;j++)
					for(k=j+1;k<length;k++)
						if(N[k]<N[j])
							change(N[k],N[j]);
				flag=0;
				break;
			}
		}
		if(flag==1)
		{
			for(i=length-1;i>=0;i--)
				if(N[i]!='0')
					break;
			if(i!=0) change(N[0],N[i]);
			for(i=1;i<length-1;i++)
				for(j=i+1;j<length;j++)
					if(N[i]>N[j])
						change(N[i],N[j]);
			for(i=length+1;i>1;i--)
				N[i]=N[i-1];
			N[i]='0';
		}
		printf("Case #%d: %s\n",cnt,N);
	}

	getch();
	fclose(stdin);
	fclose(stdout);
}
