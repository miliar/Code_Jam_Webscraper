#include <iostream>
#include <fstream>
using namespace std;

int candy[25];

int main()
{
	ofstream output;
	ifstream input;
	output.open("D:\\res.txt");
	input.open("D:\\C-small-attempt0.in");
	int t,tt;
	input >>t;
	for(int tt=1;tt<=t;tt++)
	{
		int n;
		input >>n;	
		for(int i=0;i<n;i++) input >>candy[i];
		int ans=-1;
		for(int i=1;i<(1<<n)-1;i++)
		{
			int a1=0,a2=0,b1=0,b2=0;
			for(int j=0;j<n;j++)
			{
				if(i&(1<<j))
				{
					a1+=candy[j];
					b1=b1^candy[j];
				}
				else
				{
					a2+=candy[j];
					b2=b2^candy[j];	
				}
			}
			if(b1==b2 && a2>ans) ans=a2;
		}	
		output <<"Case #"<<tt<<": ";
		if(ans==-1) output <<"NO"<<endl;
		else output <<ans<<endl;
	}
	input.close();
	output.close();
	return 0;
}
