#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
using namespace std;



int main()
{
	unsigned int N,K;
	int count = 0;
	bool state = 0;
	//ifstream InFile("A-small-attempt10.in");
	ifstream InFile("A-large.in");
	ofstream OutFile("A-Large-attempt_result.in");
	string line;
	int Google[31];
	Google[1]= 1;
	for (int i=2;i<=30;++i)
	{
		unsigned int increment = (int)pow(2,i-1);
		unsigned int preIndex = Google[i-1];
		int j = preIndex + increment;
		while(((j-preIndex-1)%(int)pow(2,i)) / (int)pow(2,i-1) != 0)
		{
			j += increment;
		}
		Google[i] = j;
	}
for (int k=1;k<31;++k)
{
	cout<<k<<"   "<<Google[k]<<endl;
}

	while(getline(InFile,line))
	{
		istringstream strm(line);
		if (strm>>N>>K)
		{
			++count;
			state = 0;
			unsigned firstOn = Google[N];
			if (K >= firstOn && (((K - firstOn) % (int)pow(2,N)) == 0))
			{
				state = 1;
			}
			OutFile<<"Case #"<<count;
			if (state == 1)
			{
				OutFile<<": ON"<<endl;
			}
			else
			{
				OutFile<<": OFF"<<endl;
			}
		}
	}
	return 0;
}