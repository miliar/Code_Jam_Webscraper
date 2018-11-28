#include<stdio.h>

FILE *in,*out;
void io()
{
	in =fopen("c.in" ,"r");
	out=fopen("c.out","w");
}

int i[16384];
int b[16384];
int v[16384];
int l[16384];
int o[16384];

int main()
{
	io();
	int k;
	int r,c,n;
	int t,x,y,p,q;
	int a,s;
	fscanf(in,"%d",&k);
	for(a=0;a<k;a++)
	{
		fscanf(in,"%d%d%d",&r,&c,&n);
		for(s=0;s<n;s++) fscanf(in,"%d",&i[s]);
		t=0;
		y=0;
		for(x=0;x<n;x++)
		{
			for(s=0;s<n;s++)
			{
				q=i[(y+s)%n];
				if( t+q<=c ) t+=q;
				else break;
			}
			y=(y+s)%n;
			b[x]=y;
			v[x]=t;
			l[x]=-1;
			o[x]=-1;
			t-=i[x];
		}
		l[0]=0;
		x=0;
		t=0;
		for(s=0;s<r;s++)
		{
			t+=v[x];
			o[x]=t;
			if( l[b[x]]!=-1 )
			{
				p=l[x]-l[b[x]]+1;
				q=o[x]-o[b[x]]+v[b[x]];
				t+=((r-1-s)/p)*q;
				s+=((r-1-s)/p)*p;
				x=b[x];
				s++;
				break;
			}
			l[b[x]]=l[x]+1;
			x=b[x];
		}
		for(;s<r;s++)
		{
			t+=v[x];
			o[x]=t;
			x=b[x];
		}
		fprintf(out,"Case #%d: ",a+1);
		fprintf(out,"%d\n",t);
	}
	return 0;
}