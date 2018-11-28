#include<stdio.h>
#include<algorithm>
#include<string.h>

using namespace std;

int next[23],rez[24];

int isdesc(int len)
{
	int i,sw=1;

	for(i=0;i<len-1;i++)
	{
		if(next[i]<next[i+1])
		{
			sw=0;
			break;
		}
	}
	return sw;
}
			

void solve(char s[22],int *lenu)
{
	int i,len,minpoz=-1,min=10,aux,pozj,j,t;

	len=strlen(s);
	len--;
	
	for(i=0;i<len;i++)
		next[i]=s[i]-'0';

	if(isdesc(len)==1)
	{
		sort(next,next+len);
		j=0;
		while(next[j]==0)
			j++;
		rez[0]=next[j];
		t=1;
		for(i=0;i<=j;i++)
			rez[t++]=0;
		for(i=j+1;i<len;i++)
				rez[t++]=next[i];
		*lenu=len+1;
		return;
	}
	else
	{
		for(i=len-2;i>=0;i--)
		{
			for(j=i+1;j<len;j++)
			{
				if(next[j]>next[i] && next[j]<min)
				{
					minpoz=i;
					min=next[j];
					pozj=j;
				}
			}
			if(minpoz!=-1)
				break;
		}
		*lenu=len;
		aux=next[minpoz];
		next[minpoz]=next[pozj];
		next[pozj]=aux;
		
		sort(next+minpoz+1,next+len);
	}
}
				
				
			
int main()
{
	int t,len,i,j;	
	FILE *f=fopen("b.in","r");
	FILE *g=fopen("b.out","w");
	char s[22];

	fscanf(f,"%i\n",&t);
	for(i=0;i<t;i++)
	{
		fgets(s,22,f);
		solve(s,&len);
		fprintf(g,"%s%i%s","Case #",i+1,": ");

		if(len==strlen(s))
		{
			for(j=0;j<len;j++)
				fprintf(g,"%i",rez[j]);
			fprintf(g,"%s","\n");
		}
		else
		{		
			for(j=0;j<strlen(s)-1;j++)
				fprintf(g,"%i",next[j]);
			fprintf(g,"%s","\n");
		}
	}
	fclose(f);
	fclose(g);
	return 0;
}	
			















	

	
	