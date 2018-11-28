#include<fstream>
#include<algorithm>
using namespace std;
long t,i,a,b;
long long rez;
ofstream g("numbers.out");
void perm(long long b)
{long i,nr=b,nc=0,v[15]={0},aux,j;
	while(nr)
	{
	  v[++nc]=nr%10;
	  nr/=10;
	}
	reverse(v+1,v+nc+1);
	for(i=1;i<nc;i++)
	{
	   aux=v[nc];
	   for(j=nc;j>1;j--)v[j]=v[j-1]; 
	   v[1]=aux;
		nr=0;
	  for(j=1;j<=nc;j++)nr=nr*10+v[j];
	  if(nr<b && nr>=a)rez++;
	  //for(j=a+1;j<=b;j++)if(j==nr)g<<j<<"\n";
	}
}
long long solve(long a,long b)
{long long i;
	for(i=b;i>a;i--)
	  perm(i);
}
int main()
{
	ifstream f("numbers.in");
	f>>t;
	for(i=1;i<=t;i++)
	{
		f>>a>>b;
		rez=0;
		solve(a,b);
		g<<"Case #"<<i<<": "<<rez<<"\n";
	}
	f.close();g.close();
}