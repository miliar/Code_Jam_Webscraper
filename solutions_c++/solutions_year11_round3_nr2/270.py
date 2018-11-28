#include<stdio.h>
#include<set.h>
FILE *in,*out,*dbg;
struct node
{
	int i;
	long long v;
};
struct cmp
{
	bool operator()(node x,node y)
	{
		if( x.v!=y.v ) return x.v>y.v;
		if( x.i!=y.i ) return x.i<y.i;
		return false;
	}
};
set<node,cmp> h;
node ht;
int i[1048576];
int main()
{
	in =fopen("b.in" ,"r");
	out=fopen("b.out","w");
//	dbg=fopen("debug.txt","w");
	int tests,test;
	long long t,v,sum;
	int l,n,c,a,s;
	fscanf(in,"%d",&tests);
	for(test=0;test<tests;test++)
	{
		fscanf(in,"%d%I64d%d%d",&l,&t,&n,&c);
		for(a=0;a<c;a++) fscanf(in,"%d",&i[a]);
		for(a=c;a<n;a++) i[a]=i[a-c];
		s=0;
		sum=0;
		for(a=0;a<n;a++)
		{
			sum+=i[a]*2;
			if( sum>t )
			{
				if( s==0 )
				{
					s=1;
					v=sum-t;
				}
				else
				{
					v=i[a]*2;
				}
				h.insert((node){a,v});
			}
		}
		while( l>0 && h.size()>0 )
		{
			ht=*h.begin();
			h.erase(ht);
			sum-=ht.v/2;
			l--;
		}
		h.clear();
		fprintf(out,"Case #%d: ",test+1);
		fprintf(out,"%I64d\n",sum);
	}
	return 0;
}