#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

void main(int argc, char* argv[])
{
	ifstream fin;
	ofstream fout;
	int N;	//#test cases

	fin.open(argv[1], ios::in);
	fout.open(argv[2], ios::out);

	fin>>N;

	for(int index=1;index<=N;index++)
	{
		long p,k,l;
		vector<long> freq;

		fin>>p>>k>>l;
		//freq = new int[l];
		long temp;

		for(int i=0;i<l;i++)
		{
			fin>>temp;
			freq.push_back(temp);
		}

		//process
		sort(freq.rbegin(), freq.rend());

		long res=0;
		long count=1;
		long circular = 0;

		int i;
		for(i=0;i<l;i++)
		{
			res += freq[i] * count;
			circular++;
			if(circular == k)
			{
				circular=0;
				count++;
			}
		}

		//output
		fout<<"Case #"<<index<<": "<<res<<"\n";
	}
		
	fin.close();
	fout.close();
}