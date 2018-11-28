#include <fstream>
using namespace std;

int main()
{
	ifstream in("b.in");
	ofstream out("b.out");

	long int t,r,k,n,*g,p,cs,q;
	long long int s;
	in>>t;
	for(int i=1; i<=t; i++)
	{
		in>>r>>k>>n;
		g = new long int[n];
		for(int j=0; j<n; j++)
			in>>g[j];

		//algorithm
		s = 0;
		p = 0;
		for(int j=0; j<r; j++)
		{
			cs = 0;
			q = p;
			do
			{
				cs+=g[p];
				p = (p+1)%n;
			}
			while(p!=q && cs+g[p]<=k);
			s+=cs;
		}
		delete []g;
		out<<"Case #"<<i<<": "<<s<<"\n";
	}
	return 0;
}