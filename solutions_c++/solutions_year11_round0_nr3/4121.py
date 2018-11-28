#include<iostream>
#include<fstream>
using namespace std;

const int N = 1010;
unsigned int can[N];

int main()
{
	ifstream inf("C-large.in");
	ofstream outf("colarge.txt");

	int t,n,i,k;
	unsigned int ans,sum,min;
	while(inf>>t)
	{
		for(k=0;k<t;k++)
		{
			//ÊäÈë
			inf>>n;
			inf>>can[0];
			ans=can[0];
			sum=can[0];
			min=can[0];
			for(i=1;i<n;i++)
			{
				inf>>can[i];
				ans=ans^can[i];
				sum+=can[i];
				if(can[i]<min)
					min=can[i];
			}
			if(ans!=0)
			{
				outf<<"Case #"<<k+1<<": NO\n";
			}
			else
			{
				outf<<"Case #"<<k+1<<": "<<(sum-min)<<"\n";
			}
			
		}
	}
	inf.close();
	outf.close();
	return 0;
}