#include<fstream>
#define dmax 65
using namespace std;
ifstream in("base.in");
ofstream out("base.out");
int t,l,crt;
char x[dmax];
int y[dmax];
void conv()
{	int p,q,;
	long long sol=0,z=1;
	for(p=0;p<l;p++)
	{	z=1;
		for(q=1;q<=l-p-1;q++)
			z*=crt;
		z=y[p]*z;
		sol+=z;
	}
	out<<sol<<'\n';
}	
void solve()
{	int i,j,ok;
	for(i=0;i<l;i++)
	{	if(i==0)
			y[i]=1;
		else
		{	ok=0;
			for(j=0;j<i;j++)
				if(x[j]==x[i])
				{	ok=1;
					y[i]=y[j];
				}
			if(ok==0)
			{	if(crt==1)crt=2;
				y[i]=crt;
				crt++;
			}
		}
	}
	if((crt==1)||(crt==0))crt=2;
}
int main()
{	int i;
	in>>t;
	for(i=0;i<=t;i++)
	{	in.getline(x,dmax,'\n');
		l=strlen(x);
		if(i)
		{	solve();
			out<<"Case #"<<i<<": ";
			conv();
		}	
		crt=0;
	}	
	in.close();
	out.close();
	return 0;
}	