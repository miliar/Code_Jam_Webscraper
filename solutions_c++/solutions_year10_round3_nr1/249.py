#include <iostream>
#include <fstream>

using namespace std;

void main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("A-large.out");

	int a[1000],b[1000];
	int t,n;
	int ii,i,j;
	ifs>>t;
	for(ii=0; ii<t; ii++)
	{
		int y=0;
		ifs>>n;
		for(i=0; i<n; i++)
		{
			ifs>>a[i]>>b[i];

			for(j=0; j<i; j++)
				if( (a[j]-a[i])*(b[j]-b[i])<0 )
					y++;

		}

		ofs<<"Case #"<<ii+1<<": "<<y<<endl;
	}
}
