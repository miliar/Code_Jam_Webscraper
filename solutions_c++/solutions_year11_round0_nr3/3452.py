#include <iostream>
#include <fstream>
using namespace std;

void main()
{
	ofstream outfile( "C-large.out" );
	ifstream infile( "C-large.in" );

	unsigned long min,i, j, c[1001], n, t, Ssum, Psum,Stotal,Ttotal;
    infile>>t;
	for (i=1;i<=t;i++)
	{
		infile>>n;
		Stotal = Ttotal = 0;
		min=10000000;
		for (j=1;j<=n;j++){infile>>c[j];Stotal+=c[j];Ttotal^=c[j];if (c[j]<min)min=c[j];};
		if (Ttotal!=0){outfile<<"Case #"<<i<<": NO"<<endl;}
		else
		{
		outfile<<"Case #"<<i<<": "<<Stotal-min<<endl;
		}
	}

}