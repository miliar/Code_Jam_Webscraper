#include<vector>
#include<map>
#include<fstream>
#include<iostream>
#include<algorithm>

using namespace std;

int main(int argc, char* argv[])
{
	if(argc < 2)return 0;
	ifstream is(argv[1]);
	ofstream os("A.out");

	int n;
	is>>n;
	for(int casenum = 0; casenum < n; casenum++)
	{
		int p,k,l;
		is>>p>>k>>l;
		vector<int> freq;
		for(int i = 0 ; i < l; i++)
		{
			int temp;
			is>>temp;
			freq.push_back(temp);
		}
		sort(freq.begin(),freq.end());
		int sum = 0;
		for(int i = l-1 ; i >= 0; i--)
		{
			sum += freq[i] * ((l - i - 1)/k + 1);
		}
		os<<"Case #"<<casenum+1<<": "<<sum<<endl;
	}
	return 0;
}