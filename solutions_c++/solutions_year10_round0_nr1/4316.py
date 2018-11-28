#include<fstream>
#define dmax 35
using namespace std;
ifstream in("snc.in");
ofstream out("snc.out");

int n,k,T,v,ok;
bool pw[dmax],t[dmax];

void solve(int q)
{	int i,j,w;
	pw[1]=1;
	for(i=1;i<=k;i++)
	{	for(j=1;j<=n;j++)
			if(pw[j])
			{	if(t[j]==0)t[j]=1;
				else t[j]=0;
			}	
		for(j=2;j<=n;j++)
			if(!t[j-1] && pw[j])
				pw[j]=0;
		for(j=2;j<=n;j++)
			if(pw[j-1] && t[j-1])
				pw[j]=1;
		/*if(pw[1]==1 && t[1]==0)
		{	ok=1;
			for(j=1;j<=n;j++)
				if(pw[j] || t[j])ok=0;
			if(ok)out<<q<<"*";
		}*/		
	}
	out<<"Case #"<<q<<": ";
	if(pw[n] && t[n])out<<"ON\n";	
	else out<<"OFF\n";
	for(i=1;i<=n;i++)
		pw[i]=t[i]=0;
}	

int main()
{	int i;
	in>>T;
	for(i=1;i<=T;i++)
	{	in>>n>>k;
		solve(i);
	}
	in.close();
	out.close();
	return 0;
}	
