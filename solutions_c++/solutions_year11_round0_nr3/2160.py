#include <iostream>
#include <fstream>

using namespace std;

void main()
{
	ifstream ifs("C-large.in");
	ofstream ofs("C-large.out");

	int t,n,c;
	int i,j,k;
	ifs>>t;
	for(i=0; i<t; i++)
	{
		int sum;
		int minnum;
		int xorsum;

		ifs>>n;
		ifs>>c;
		sum=minnum=xorsum=c;

		for(j=1; j<n; j++)
		{
			ifs>>c;
			sum+=c;
			xorsum^=c;
			minnum=min(minnum,c);
		}

		if(xorsum!=0)
			ofs<<"Case #"<<i+1<<": NO"<<endl;
		else
			ofs<<"Case #"<<i+1<<": "<<sum-minnum<<endl;
	}
}