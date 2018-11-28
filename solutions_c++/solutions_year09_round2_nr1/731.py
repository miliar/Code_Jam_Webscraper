#include<stdio.h>
#include<string>
#include<string.h>
#include<stdlib.h>
#include<set>
using namespace std;
struct sir
{
	char c[15];
};
struct classcomp
{
	bool operator() (const sir &x,const sir &y)
	{
		int i;
		for(i=0; x.c[i] && y.c[i]; ++i)
		{
			if(x.c[i]==y.c[i])
				continue;
			if(x.c[i]<y.c[i])
				return true;
			return false;
		}
		if(x.c[i]==0 && y.c[i]!=0)
			return true;
		return false;
	}
};  
int p;
double rez;
char ptc[100];
set<sir,classcomp> s;
struct tree
{
	char *c;
	double p;
	tree *st,*dr;
};
char c[8500];
tree* back()
{
	int x=0;
	int y=0;
	tree *nod=new tree;
	nod->st=0;
	nod->dr=0;
	nod->p=0;
	nod->c=0;
       /* for(; c[p]>='0' && c[p]<='9'; ++p)
		x=x*10+c[p]-'0';
	nod->p=(double)x;
	if(c[p]=='.')
	{
		++p;
		for(; c[p]>='0' && c[p]<='9'; ++p)
			y=y*10+c[p]-'0';
		double y1=(double)y;
		while(y1>1)
			y1/=10;
		nod->p=nod->p+y1;
	}
     	*/
	int i;
	for(i=0; (c[p]>='0' && c[p]<='9') || c[p]=='.'; ++p,++i)
        	ptc[i]=c[p];
	ptc[i]='\0';
	sscanf(ptc,"%lf",&(nod->p));
	int p1=p;
	for(; c[p]>='a' && c[p]<='z'; ++p)
		;
	if(p!=p1)
	{
       		nod->c=new char[p-p1+2];
		memset(nod->c,0,p-p1+2);
		char *aux=nod->c;
		for(int i=0; p1<p; ++p1,++i)
			aux[i]=c[p1];
	}
	if(c[p]==')')
	{
		++p;
		return nod;
	}
	++p;
	nod->st=back();
	++p;
	nod->dr=back();
	++p;
	return nod;
}
void afla(tree* nod)
{
	rez*=nod->p;
	if(nod->st==0)
		return;
	sir ca;
	memset(ca.c,0,sizeof(ca.c));
	strcpy(ca.c,nod->c);
	if(s.find(ca)!=s.end())
		afla(nod->st);
	else
		afla(nod->dr);
}	
inline void rezolva()
{
	memset(c,0,sizeof(c));
	int l;
	scanf("%d\n",&l);
	int poz=0;
        for(int i=0; i<l; ++i)
	{
        	fgets(c+poz,85,stdin);
		for(int j=poz; c[j]; ++j)
		{
			if(c[j]==' ' || c[j]=='\n')
				continue;
			c[poz++]=c[j];
		}
	}
	p=0;
	tree* t=0;
	if(c[0]=='(')
	{
		++p;
        	t=back();
	}
       // if(t==0)
       // 	exit(4);
       	int a;
	scanf("%d\n",&a);
	char aux[15];
	int n;
	sir saux;
	for(int i=0; i<a; ++i)
	{
		s.clear();
        	scanf("%s",aux);
		scanf("%d",&n);
		for(int j=0; j<n; ++j)
		{
			scanf("%s",aux);
			strcpy(saux.c,aux);
			s.insert(saux);
		}
		rez=1;
		afla(t);
		printf("%lf\n",rez);
	} 
}	
int main()
{
	freopen("pa.in","r",stdin);
	freopen("pa.out","w",stdout);
        int T;
	scanf("%d\n",&T);
	for(int i=1; i<=T; ++i)
	{
		printf("Case #%d:\n",i);
		rezolva();
	}
        return 0;
}

