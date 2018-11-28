#include <iostream>
#include <fstream>
#include <set>
#include <string>

using namespace std;

void main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("A-large.out");

	int t,n;
	int i,j;
	ifs>>t;
	for(i=0; i<t; i++)
	{
		int tot=0;
		int ot=0,rt=0;
		int op=1,rp=1;

		ifs>>n;
		for(j=0; j<n; j++)
		{
			char r;
			int p;
			ifs>>r>>p;

			if(r=='O')
			{
				ot+=max(abs(op-p)-rt,0)+1;
				tot+=max(abs(op-p)-rt,0)+1;
				rt=0;
				op=p;
			}
			else if(r=='B')
			{
				rt+=max(abs(rp-p)-ot,0)+1;
				tot+=max(abs(rp-p)-ot,0)+1;
				ot=0;
				rp=p;
			}
		}

		ofs<<"Case #"<<i+1<<": "<<tot<<endl;
	}
}