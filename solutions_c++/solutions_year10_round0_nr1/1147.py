#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int T, N, k;
	int min[30];
	ifstream datain("A-large.in");
	ofstream dataout("A-large.out");
	datain>>T;
	//cout<<T<<endl;
	for (int i=0; i<30; i++)
	{
		min[i] = 1;
		for (int j=0; j<=i;j++)
			min[i] = min[i]<<1;
		//cout<<min[i]<<endl;
	}
	for (int x=1; x<=T ;x++)
	{
		datain>>N>>k;
		//cout<<N<<' '<<k<<endl;
		if ((k+1) % min[N-1] == 0)
		{
			dataout<<"Case #"<<x<<": ON"<<endl;
		}
		else
		{
			dataout<<"Case #"<<x<<": OFF"<<endl;
		}
	}
	datain.close();
	dataout.close();
	return 0;
}

