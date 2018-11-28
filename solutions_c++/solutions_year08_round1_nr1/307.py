#include<cstdio>
#include<cstdlib>
#include<set>
using namespace std;
struct node{ int i,v; };
struct comp{ bool operator()(node x,node y){ if( x.v==y.v ) return x.i<y.i; return x.v<y.v; } };
set<node,comp> h1,h2;
char str[101],i[100][101];
int b[1000];
FILE *in,*out;
int main()
{
	int a,data,n,cnt,sum;
	node nt;
	in=fopen("as.in","r");
	out=fopen("a.out","w");
	fscanf(in,"%d",&data);
	cnt=0;
begin: data--;
	fscanf(in,"%d",&n);
	for(a=0;a<n;a++)
	{
		nt.i=a;
		fscanf(in,"%d",&nt.v);
		h1.insert(nt);
	}
	for(a=0;a<n;a++)
	{
		nt.i=a;
		fscanf(in,"%d",&nt.v);
		h2.insert(nt);
	}
	for(a=0;a<n;a++)
	{
		nt=*h1.begin();
		h1.erase(nt);
		b[a]=nt.v;
	}
	for(a=0;a<n;a++)
	{
		nt=*h2.begin();
		h2.erase(nt);
		b[n-a-1]*=nt.v;
	}
	sum=0;
	for(a=0;a<n;a++)
	{
		sum+=b[a];
	}
	cnt++;
	fprintf(out,"Case #%d: %d\n",cnt,sum);
	if( data>0 ) goto begin;
//system("pause");
	return 0;
}
