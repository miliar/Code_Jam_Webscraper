#include<stdio.h>
#include<string.h>
char a[100];
char t[100];
int count[10],count2[10];
int main()
{
	int in,d,n,m,s;
	scanf("%d",&in);
	for(n=0;n<in;n++)
	{
		scanf("%s",a);
		for(m=0;m<30;m++)
		{
			t[m]='0';
		}
		t[30]=0;
		d=strlen(a);
		d--;
		for(m=0;m<=9;m++)
		{
			count2[m]=0;
		}
		for(m=29;m>=0;m--)
		{
			if(d<0)
				break;
			t[m]=a[d--];
			count2[t[m]-'0']++;
		}
		while(1)
		{
			d=1;
			for(m=29;m>=0;m--)
			{
				if(t[m]=='9')
					t[m]='0';
				else
				{
					t[m]++;
					break;
				}
			}
			for(m=0;m<10;m++)
				count[m]=0;
			for(m=29;m>=0;m--)
			{
				count[t[m]-'0']++;
			}
			for(m=1;m<10;m++)
			{
				if(count[m]!=count2[m])
					break;
			}
			if(m==10)
				break;
		}
		printf("Case #%d: ",n+1);
		s=0;
		for(m=0;m<=29;m++)
		{
			if(t[m]!='0')
				s=1;
			if(s==1) printf("%c",t[m]);
		}
		printf("\n");
	}
}
