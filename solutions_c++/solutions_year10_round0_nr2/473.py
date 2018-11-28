#include<stdio.h>
#include<string.h>
#include<vector.h>

FILE *in,*out;
void io()
{
	in =fopen("b.in" ,"r");
	out=fopen("b.out","w");
}

const int bigm=1000000000;
const int bigd=9;
const int bigb=30;

struct big
{
	vector<int> n;
	int l;
	void z(int p)
	{
		int a;
		while( p>(signed)n.size() ) n.push_back(0);
		l=p;
		for(a=0;a<l;a++) n[a]=0;
	}
	void i(int p,int v)
	{
		while( p>=(signed)n.size() ) n.push_back(0);
		n[p]=v;
		if( p>=l ) l=p+1;
	}
	big() { l=0; }
};

void reduce(big &x)
{
	int a;
	if( x.l==0 ) return;
		x.i(x.l,0);
		for(a=0;a<x.l-1;a++)
		{
			x.n[a+1]+=x.n[a]/bigm;
			x.n[a]%=bigm;
		}
	while( x.l>0 ) if( x.n[x.l-1]==0 ) x.l--; else break;
	if( x.l==0 ) return;
	if( x.n[x.l-1]>=0 )
	{
		x.i(x.l,0);
		for(a=0;a<x.l-1;a++)
		{
			if( x.n[a]<0 )
			{
				x.n[a+1]--;
				x.n[a]+=bigm;
			}
		}
	}
	else
	{
		x.i(x.l,0);
		for(a=0;a<x.l-1;a++)
		{
			if( x.n[a]>0 )
			{
				x.n[a+1]++;
				x.n[a]-=bigm;
			}
		}
	}
	while( x.l>0 ) if( x.n[x.l-1]==0 ) x.l--; else break;
}

void strtobig(char *x,big &y)
{
	int l;
	int a,s;
	l=strlen(x);
	if( x[0]!='-' )
	{
		y.z((l+bigd-1)/bigd);
		s=0;
		for(a=0;a<l;a++)
		{
			s=s*10+(x[a]-'0');
			if( (l-1-a)%bigd==0 )
			{
				y.n[(l-1-a)/bigd]=s;
				s=0;
			}
		}
	}
	else
	{
		y.z((l-1+bigd-1)/bigd);
		s=0;
		for(a=1;a<l;a++)
		{
			s=s*10+(x[a]-'0');
			if( (l-1-a)%bigd==0 )
			{
				y.n[(l-1-a)/bigd]=-s;
				s=0;
			}
		}
	}
	reduce(y);
}

void bigtostr(const big &x,char *y)
{
	int v;
	int a,s,d;
	if( x.l==0 )
	{
		strcpy(y,"0");
		return;
	}
	if( x.n[x.l-1]>=0 )
	{
		d=0;
		v=x.n[x.l-1];
		while( v>0 ) { v/=10; d++; }
		v=x.n[x.l-1];
		for(s=d-1;s>=0;s--) { y[s]='0'+v%10; v/=10; }
		for(a=1;a<x.l;a++)
		{
			v=x.n[x.l-1-a];
			for(s=bigd-1;s>=0;s--) { y[d+(a-1)*bigd+s]='0'+v%10; v/=10; }
		}
		y[d+(x.l-1)*bigd]=0;
	}
	else
	{
		d=0;
		v=-x.n[x.l-1];
		while( v>0 ) { v/=10; d++; }
		v=-x.n[x.l-1];
		y[0]='-';
		for(s=d-1;s>=0;s--) { y[s+1]='0'+v%10; v/=10; }
		for(a=1;a<x.l;a++)
		{
			v=-x.n[x.l-1-a];
			for(s=bigd-1;s>=0;s--) { y[d+(a-1)*bigd+s+1]='0'+v%10; v/=10; }
		}
		y[d+(x.l-1)*bigd+1]=0;
	}
}

void lltobig(long long x,big &y)
{
	long long t;
	if( x>=0 )
	{
		y.z(0);
		t=x;
		while( t>0 )
		{
			y.i(y.l,t%bigm);
			t/=bigm;
		}
	}
	else
	{
		y.z(0);
		t=-x;
		while( t>0 )
		{
			y.i(y.l,-t%bigm);
			t/=bigm;
		}
	}
}
big lltobig(long long x)	{ big y; lltobig(x,y); return y; }

bool operator ==(const big &x,const big &y)
{
	int a;
	if( x.l!=y.l ) return 0;
	for(a=0;a<x.l;a++) if( x.n[a]!=y.n[a] ) return 0;
	return 1;
}

bool operator !=(const big &x,const big &y)
{
	int a;
	if( x.l!=y.l ) return 1;
	for(a=0;a<x.l;a++) if( x.n[a]!=y.n[a] ) return 1;
	return 0;
}

bool operator <(const big &x,const big &y)
{
	int a;
	if( x.l<y.l ) { if( y.n[y.l-1]>0 ) return true; else return false; }
	if( x.l>y.l ) { if( x.n[x.l-1]>0 ) return false; else return true; }
	for(a=x.l-1;a>=0;a--)
	{
		if( x.n[a]<y.n[a] ) return true;
		if( x.n[a]>y.n[a] ) return false;
	}
	return false;
}

bool operator >(const big &x,const big &y)
{
	return y<x;
}

bool operator <=(const big &x,const big &y)
{
	return !(y<x);
}

bool operator >=(const big &x,const big &y)
{
	return !(x<y);
}

void neg(big &x)
{
	int a;
	for(a=0;a<x.l;a++) x.n[a]=-x.n[a];
}
big operator -(const big &x) { big y=x; neg(y); return y; }

big add(const big &x,const big &y)
{
	big z;
	int a;
	z.l=(x.l>y.l?x.l:y.l);
	z.z(z.l);
	for(a=0;a<z.l;a++)
	{
		if( a<x.l ) z.n[a]+=x.n[a];
		if( a<y.l ) z.n[a]+=y.n[a];
	}
	reduce(z);
	return z;
}
big operator +(const big &x,const big &y) { return add(x,y); }

big sub(const big &x,const big &y)
{
	big z;
	int a;
	z.l=(x.l>y.l?x.l:y.l);
	z.z(z.l);
	for(a=0;a<z.l;a++)
	{
		if( a<x.l ) z.n[a]+=x.n[a];
		if( a<y.l ) z.n[a]-=y.n[a];
	}
	reduce(z);
	return z;
}
big operator -(const big &x,const big &y) { return sub(x,y); }

big mul(const big &x,const big &y)
{
	big z;
	long long v;
	int w0,w1;
	int a,s;
	z.z(x.l+y.l);
	for(a=0;a<x.l;a++)
	{
		if( x.n[a]==0 ) continue;
		z.l=x.l+y.l;
		for(s=0;s<y.l;s++)
		{
			v=(long long)x.n[a]*(long long)y.n[s];
			z.n[a+s+1]+=z.n[a+s]/bigm;
			z.n[a+s]%=bigm;
			w0=v%bigm+z.n[a+s];
			w1=v/bigm+z.n[a+s+1]+w0/bigm;
			w0%=bigm;
			z.n[a+s]=w0;
			z.n[a+s+1]=w1;
		}
		reduce(z);
	}
	reduce(z);
	return z;
}
big operator *(const big &x,const big &y) { return mul(x,y); }

big div(const big &x,const big &y)
{
	big t;
	big z,w;
	big u,wy;
	long long v,v1,v2;
	long double v3;
	int l;
	int a;
	if( x.l<y.l )
	{
		z.z(0);
		return z;
	}
	l=x.l-y.l+1;
	z.z(l);
	w.z(l);
	t=x;
	t.i(x.l,0);
	v2=(long long)y.n[y.l-1]*(long long)bigm;
	if( y.l>=2 ) v2+=(long long)y.n[y.l-2];
	for(a=l-1;a>=0;a--)
	{
		t.i(a+y.l+1,0);
		if( t.n[a+y.l]!=0 )
		{
			v3=0;
			if( a+y.l>=2 ) v3+=(long double)t.n[a+y.l-2];
			v3+=(long double)t.n[a+y.l-1]*(long double)bigm;
			v3+=(long double)t.n[a+y.l]*(long double)bigm*(long double)bigm;
			v=(long long)(v3/(long double)v2);
		}
		else
		{
			v1=(long long)t.n[a+y.l-1]*(long long)bigm;
			if( a+y.l>=2 ) v1+=(long long)t.n[a+y.l-2];
			v=v1/v2;
		}
		z.n[a]=v;
		w.l=a+1;
		w.n[a]=v;
		t=t-w*y;
	}
	if( x>lltobig(0) )
	{
		if( y>lltobig(0) )
		{
			if( t<lltobig(0) ) z.n[0]--;
			if( t>=y ) z.n[0]++;
		}
		else
		{
			if( t<lltobig(0) ) z.n[0]++;
			if( t>=-y ) z.n[0]--;
		}
	}
	else
	{
		if( y>lltobig(0) )
		{
			if( t>lltobig(0) ) z.n[0]++;
			if( t<=-y ) z.n[0]--;
		}
		else
		{
			if( t>lltobig(0) ) z.n[0]--;
			if( t<=y ) z.n[0]++;
		}
	}
	reduce(z);
	return z;
}
big operator /(const big &x,const big &y) { return div(x,y); }

big mod(const big &x,const big &y)
{
	return x-(x/y)*y;
}
big operator %(const big &x,const big &y) { return mod(x,y); }

big gcd2(const big &x,const big &y);
big gcd(const big &x,const big &y)
{
	big z,w;
	if( x>lltobig(0) ) z=x; else z=-x;
	if( y>lltobig(0) ) w=y; else w=-y;
	if( z>w )
	{
		return gcd2(z,w);
	}
	else
	{
		return gcd2(w,z);
	}
}
big gcd2(const big &x,const big &y)
{
	if( y.l==0 ) return x;
	return gcd2(y,x%y);
}

char i[1024];
char o[1024];

int main()
{
	io();
	int k;
	int n;
	big x,y,z,m;
	int a,s;
	fscanf(in,"%d",&k);
	for(a=0;a<k;a++)
	{
		fscanf(in,"%d",&n);
		fscanf(in,"%s",&i);
		strtobig(i,x);
		lltobig(0,m);
		for(s=1;s<n;s++)
		{
			fscanf(in,"%s",&i);
			strtobig(i,y);
			m=gcd(m,x-y);
		}
		z=m-lltobig(1)-(x+m-lltobig(1))%m;
		bigtostr(z,o);
		fprintf(out,"Case #%d: ",a+1);
		fprintf(out,"%s\n",o);
	}
	return 0;
}