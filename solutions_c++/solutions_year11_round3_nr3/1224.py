#include <iostream>

// basic file operations
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <bitset>

#define loop(i,n)	for(int i=0;i<(n);++i)
#define loope(i,n)	for(int i=0;i<=(n);++i)

using namespace std;


void main()
{
	ifstream in ("inputS.in");
	ofstream out("outputS.out");

	double T;
	double Case=0;
	
	in>>T;
	
	int list[100];
	for(Case = 1;Case<=T;Case++)
	{
		double N;
		int mi;
		int ma;

		in>>N;
		in>>mi;
		in>>ma;

		loop(i,N)
		{
			in>>list[i];
		}

		
		int found=0;
		for(int i=mi;i<=ma;i++)
		{
			bool flag=true;
			for(int j=0;j<N;j++)
			{
				int r=0;
				r = (list[j]<i)?(i%list[j]):(list[j]%i);

				if(r!=0)
				{
					flag=false;
					break;
				}
			}
			if(flag==true) 
			{
				found=i;
				break;
			}
		}

		if(found>0)
			out<<"Case #"<<Case<<": "<<found<<endl;
		else
			out<<"Case #"<<Case<<": "<<"NO"<<endl;
	}
	in.close();
	out.close();
}
