#include<cstdio>
#include<cstdlib>
#include<set>
using namespace std;
FILE *in,*out;
int c1[2000],c2[2000],i[2000][2000],p[2000],f[2000],b[2000];
int ql,qnl,qt,q[2][2000];
int main()
{
	int a,s,data,n,m,cnt,t1,t2,test,x;
	in=fopen("bl.in","r");
	out=fopen("b.out","w");
	fscanf(in,"%d",&data);
	cnt=0;
begin: data--;
	fscanf(in,"%d%d",&n,&m);
	for(a=0;a<m;a++)
	{
		c1[a]=0;
		c2[a]=0;
		for(s=0;s<n;s++) i[a][s]=0;
		f[a]=0;
		fscanf(in,"%d",&t1);
		for(s=0;s<t1;s++)
		{
			fscanf(in,"%d",&t2);
			t2--;
			fscanf(in,"%d",&i[a][t2]);
			i[a][t2]++;
			if( i[a][t2]==1 ) c1[a]++;
			else{ c2[a]++; p[a]=t2; }
		}
	}
	test=1;
	ql=0;
	qt=0;
	for(a=0;a<n;a++) b[a]=0;
	for(a=0;a<m;a++)
	{
		if( c1[a]==0 ){ q[qt][ql]=a; ql++; }
	}
	while( ql>0 )
	{
		qnl=0;
		for(a=0;a<ql;a++)
		{
			x=q[qt][a];
			if( f[x]==1 ) continue;
			if( c2[x]==0 )
			{
				test=0;
				goto finish;
			}
			b[p[x]]=1;
			for(s=0;s<m;s++)
			{
				if( i[s][p[x]]==2 ) f[s]=1;
				else if( i[s][p[x]]==1 )
				{
					c1[s]--;
					if( c1[s]==0 )
					{
						q[1-qt][qnl]=s;
						qnl++;
					}
				}
			}
		}
		qt=1-qt;
		ql=qnl;
	}
finish:
	cnt++;
//fprintf(out,"%d\n",test);
	if( test==1 )
	{
		fprintf(out,"Case #%d:",cnt);
		for(a=0;a<n;a++) fprintf(out," %d",b[a]);
		fprintf(out,"\n");
	}
	else fprintf(out,"Case #%d: IMPOSSIBLE\n",cnt);
	if( data>0 ) goto begin;
//system("pause");
	return 0;
}
