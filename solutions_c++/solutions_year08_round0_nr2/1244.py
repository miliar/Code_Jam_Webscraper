#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<set>
using namespace std;
FILE *in,*out;
struct node{ int i,v,e; };
struct comp
{
	bool operator()(node x,node y)
	{
		if( x.v==y.v )
		{
			if( x.e==y.e ) return x.i<y.i;
			return x.e<y.e;
		}
		else return x.v<y.v;
	}
};
set<node,comp> h;
int main()
{
	int a,data,cnt,k,na,nb,ca,cb,aa,ab,i1,i2;
	node nt;
	in=fopen("bl.in","r");
	out=fopen("b.out","w");
	fscanf(in,"%d",&data);
	cnt=0;
begin: data--;
	fscanf(in,"%d%d%d",&k,&na,&nb);
	for(a=0;a<na+nb;a++)
	{
		fscanf(in,"%d:%d",&i1,&i2);
		nt.i=a;
		nt.v=i1*60+i2;
		nt.e=1;
		h.insert(nt);
		fscanf(in,"%d:%d",&i1,&i2);
		nt.v=i1*60+i2+k;
		nt.e=0;
		h.insert(nt);
	}
	ca=0; cb=0; aa=0; ab=0;
	for(a=0;a<2*(na+nb);a++)
	{
		nt=*h.begin();
		h.erase(nt);
		if( nt.e==0 )
		{
			if( nt.i<na ) ab++;
			else aa++;
		}
		else
		{
			if( nt.i<na )
			{
				if( aa>0 ) aa--;
				else ca++;
			}
			else
			{
				if( ab>0 ) ab--;
				else cb++;
			}
		}
	}
	cnt++;
	fprintf(out,"Case #%d: %d %d\n",cnt,ca,cb);
	if( data>0 ) goto begin;
//system("pause");
	return 0;
}
