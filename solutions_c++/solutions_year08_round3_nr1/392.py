#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ifstream fin("Input.txt");
	ofstream fout("Output.txt");

	int testCNT = 0;
	fin>> testCNT;
	for(int i = 0; i < testCNT; i++)
	{
		int P = 0; fin >> P;
		int K = 0; fin >> K;
		int L = 0; fin >> L;
		vector<int> vec_keys_freq;
		for (int j = 0; j < L; j++)
		{
			int frq = 0;
			fin >> frq;
			vec_keys_freq.push_back(frq);
		}
		sort(vec_keys_freq.rbegin(),vec_keys_freq.rend());
#ifdef DEBUG
		cout <<"Total Count:" << vec_keys_freq.size()<<" Front elem: " <<vec_keys_freq.front() << "   End elem:" << vec_keys_freq.back()<<endl;
#endif
		long long sum = 0LL;
		for (int l = 0; l < L; ++l)
		{

			sum += vec_keys_freq[l]*( (int)(l / K) +1) ;
			
		}
		fout << "Case #"<<i+1<<": "<<sum<<endl;
	}
	
	return 0;
}