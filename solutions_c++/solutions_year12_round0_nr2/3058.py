#include<fstream>
#define max(a,b) (a>b)?a:b
#define min(a,b) (a<b)?a:b
using namespace std;
int n,j,i,t,rez,s,p,v[102];
long solve(int n,int s,int p)
{long nr=0,i,m,r;
    for(i=1;i<=n;i++)
	{
	  m=v[i]/3;
	  r=v[i]-m*3;
	  if(m>=p)nr++;
	   else
	   {
		if(p<=m+r && r)
		{
		 if(p<=m+1)nr++; else
		 if(r==2 && s){ nr++; s--; }
		}
		else 
		if(s && m>=1)
		{
		 m--; 
		 if(p<=m+2){ s--; nr++; }
		}
	   }
	}
	return nr;
}

int main()
{
	ifstream f("dancing.in");ofstream g("dancing.out");
	f>>t;
	for(j=1;j<=t;j++)
	{
		f>>n>>s>>p;
		for(i=1;i<=n;i++)f>>v[i];
		rez=solve(n,s,p);
		g<<"Case #"<<j<<": "<<rez<<"\n";
	}
	f.close();g.close();
return 0;}
