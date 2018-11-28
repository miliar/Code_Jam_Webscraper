#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
char str[101],i[100][101];
int b[1000];
FILE *in,*out;
int main()
{
	int a,s,d,data,c,cnt,n,m,mx;
	in=fopen("al.in","r");
	out=fopen("a.out","w");
	fscanf(in,"%d",&data);
	cnt=0;
begin: data--;
	fscanf(in,"%d",&n);
	fscanf(in,"%*[\r\n]s");
	for(a=0;a<n;a++)
	{
		fscanf(in,"%[^\r\n]s",i[a]);
		fscanf(in,"%*[\r\n]s");
	}
	fscanf(in,"%d",&m);
	fscanf(in,"%*[\r\n]s");
	for(a=0;a<m;a++)
	{
		fscanf(in,"%[^\r\n]s",str);
		fscanf(in,"%*[\r\n]s");
		for(s=0;s<n;s++) if( strcmp(str,i[s])==0 ) break;
		b[a]=s;
//fprintf(out,"%d\n",s);
	}
//printf("\n");
	c=0;
	for(a=0;a<m;)
	{
//printf("%d\n",a);
		mx=a-1;
		for(s=0;s<n;s++)
		{
			for(d=a;d<m;d++) if( b[d]==s ) break;
			if( d>mx ) mx=d;
		}
		a=mx;
		c++;
	}
//printf("\n");
	cnt++;
	if( c==0 ) c=1;
	fprintf(out,"Case #%d: %d\n",cnt,c-1);
	if( data>0 ) goto begin;
//system("pause");
	return 0;
}
