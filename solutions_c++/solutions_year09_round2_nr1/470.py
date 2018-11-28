#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 1005
#define S 1005

int l[N],r[N],p[N];
double c[N];
bool vst[N];

struct strin
{
	char str[S];
} f[N],list[N];
int ls;

FILE *fin=fopen("A-small.in","r"),*fout=fopen("A-small.out","w");
void get()
{
	memset(l,-1,sizeof(l));
	memset(r,-1,sizeof(r));
	memset(p,-1,sizeof(p));
	memset(vst,0,sizeof(vst));
	int lines,len,nl,x,y,front,n=0,s=0;
	char line[S],num[S],fea[S];
	bool a=0,b=0;
	fscanf(fin,"%d",&lines);
	fgets(line,S,fin);
	for(;lines;--lines)
	{
		fgets(line,S,fin);
		len=strlen(line);
		if(vst[n]==1)
		{
			if(vst[l[n]]==0)
				n=l[n];
			else
			{
				if(vst[r[n]]==1)
					n=p[n];
				else
					n=r[n];
			}
		}
		front=0;
		if(a==0)
		{
			nl=0;
			front=strchr(line,'(')-line;
			if(strchr(line,'(')==NULL)
				continue;
			memset(num,0,sizeof(num));
			for(y=front+1;y<len;++y)
			{
				if(('0'<=line[y] && line[y]<='9')||line[y]=='.')
					num[nl++]=line[y];
				else if(num[0]!=0)
					break;
			}
			num[nl]=0;
			if(num[0]!=0)
				sscanf(num,"%lf",&c[n]);
			else
				continue;
			front=y;
			a=1;
		}
		if(a==1)
		{
			sscanf(line+front,"%s",fea);
			if(fea[0]==')')
			{
				a=0;
				vst[n]=1;
				n=p[n];
			}
			else if('a'<=fea[0] && fea[0]<='z')
			{
				strcpy(f[n].str,fea);
				vst[n]=1;
				l[n]=s+1;
				p[s+1]=n;
				r[n]=s+2;
				p[s+2]=n;
				n=s+1;
				s+=2;
				a=0;
			}
		}
	}
}



bool is(int n)
{
	for(int x=0;x<ls;++x)
	{
		if(strcmp(f[n].str,list[x].str)==0)
			return 1;
	}
	return 0;
}
double find()
{
	double ans=1;
	int n=0;
	while(1)
	{
		if(n==-1)
			break;
		ans*=c[n];
		if(f[n].str[0]==0)
			break;
		if(is(n))
			n=l[n];
		else
			n=r[n];
	}
	return ans;
}

int main()
{
	int x,y,z,t;
	char temp[S];
	fscanf(fin,"%d",&t);
	for(z=1;z<=t;++z)
	{
		fprintf(fout,"Case #%d:\n",z);
		get();
		fscanf(fin,"%d",&y);
		for(;y;--y)
		{
			fscanf(fin,"%s%d",temp,&ls);
			for(x=0;x<ls;++x)
				fscanf(fin,"%s",list[x].str);
			fprintf(fout,"%.7lf\n",find());
		}
	}
	return 0;
}