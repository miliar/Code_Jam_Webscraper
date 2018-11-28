#include <iostream>
#include <fstream>

using namespace std;

typedef __int64 LINT;

void main()
{
	ifstream ifs("B-large.in");
	ofstream ofs("B-large.out");

	LINT t,l,p,c;
	int ii,i,j;
	ifs>>t;
	for(ii=0; ii<t; ii++)
	{
		ifs>>l>>p>>c;
		
		for(i=0; p>c*l; i++)
			c*=c;		

		ofs<<"Case #"<<ii+1<<": "<<i<<endl;
	}
}
