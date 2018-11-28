#include<fstream>
#define dmax 103
using namespace std;
ifstream in("harmony.in");
ofstream out("harmony.out");

int t,n,x[dmax],a,b;

void solve()
{	
	int i,k,ok;
	
	for(k=a; k<=b; k++)
	{	ok = 1;
		for(i=1; i<=n && ok; i++)
			if( ! (k%x[i]==0 || x[i]%k==0))
				ok = 0;
		if(ok == 1)
		{	out<<k<<'\n';
			return ;
		}
	}	
	out<<"NO\n";
}	

int main()
{	
	int i,q;
	
	in>>t;
	
	for(q=1; q<=t; q++)
	{	
		in>>n>>a>>b;

		for(i=1; i<=n; i++)
			in>>x[i];
		
		out<<"Case #"<<q<<": ";
		solve();
	}
	
	
	in.close();
	out.close();
	return 0;
}	