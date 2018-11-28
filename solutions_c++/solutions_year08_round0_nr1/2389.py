
#include  <stdio.h>
#include  <string.h>
#include  <stdlib.h>

int n,s,q;
char engine[101][100];
char str[100];
char ss[100];
char qq[100];

int  t[101][1001];
void get_a_line(char *p);
int fun(int b[],int Switch,int Pos);

int main(int argc,char *argv[])
{

	int i,j,min;
	int *b;

	memset(str,0,sizeof(str));
	get_a_line(str);
	n=atoi(str);
//	scanf("%d",&n);

	for(i=1;i<=n;i++)
	{
		memset(engine,0,sizeof(engine));
		memset(ss,0,sizeof(ss));
		memset(qq,0,sizeof(qq));

	
		get_a_line(ss);
		s=atoi(ss);
	//	printf("s=%d\n",s);
		for(j=0;j<s;j++)
			get_a_line(engine[j]);
	
		
		get_a_line(qq);	
		q=atoi(qq);
	//	printf("q=%d\n",q);
		b=(int *)malloc(q*sizeof(int));
		
		for(j=0;j<q;j++)
		{
			int k;
			memset(str,0,sizeof(str));
			get_a_line(str);
			for(k=0;k<s;k++)
				if(strcmp(engine[k],str)==0)
					break;
			b[j]=k;			
		 	
		}
		/*
		for(j=0;j<q;j++)
			printf("%d  ",b[j]);
		printf("\n");
		*/
		memset(t,0,sizeof(t));
		min=fun(b,0,0);
		
		for(j=1;j<s;j++)
		{
			int m=fun(b,j,0);
			if(m<min)
				min=m;
		}
		printf("Case #%d: %d\n",i,min);
		free(b);
					
	}
	return 0;
}

void get_a_line(char *p)
{
	int i=0;
	char c=getchar();
	while(c!='\n')
	{
		p[i++]=c;
		c=getchar();
	}
}

/*
int fun(int b[],int Switch,int Pos)
{
	int r=q;
	if(Pos>=q)
		return 0;
	if(b[Pos]==Switch)
	{
		int i;
		for(i=(Switch+1)%s;i!=Switch;i=(i+1)%s)
		{
			int m=fun(b,i,Pos+1)+1;
			if(m<r)
				r=m;
		}
	} else
		r=fun(b,Switch,Pos+1);
	return r;
}

*/

int fun(int b[],int Switch,int Pos)
{
	int r=q-1;
	if(Pos>=q)		return 0;
	if(t[Switch][Pos]!=0)  return t[Switch][Pos];

	if(b[Pos]==Switch)
	{
		int i;
		for(i=(Switch+1)%s;i!=Switch;i=(i+1)%s)
		{
			int m=fun(b,i,Pos+1);
			if(m<r)
				r=m;
		}
		r+=1;
	} else
		r=fun(b,Switch,Pos+1);

	t[Switch][Pos]=r;
	return r;
}

