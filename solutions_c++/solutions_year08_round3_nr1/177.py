#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

int main()
{
	int ncase;
	cin >> ncase;
	for(int icase=1; icase <= ncase; icase++)
	{
		int P,K,L;
		cin >> P >> K >> L;
		vector<int> freq; int ff;
		for(int i=0; i< L; i++)
		{
			cin >> ff; freq.push_back(ff);
		}
		sort(freq.begin(), freq.end(), greater<int>());
		vector< vector<int> > vv(K);
		vector<int> sum(K);
		for(int kk=0; kk < freq.size(); kk++)
		{
			int val = freq[kk];
			int minsize = vv[0].size(); int minid = 0;
			for(int mm=1; mm < sum.size(); mm++)
			{
				if (vv[mm].size() < minsize) { minsize = vv[mm].size(); minid = mm; }
			}
			vv[minid].push_back(val);
		}

		long long ret = 0;
		for(int ii=0; ii < vv.size(); ii++)
		{
			for(int jj=0; jj < vv[ii].size(); jj++)
			{
				ret += (long long)vv[ii][jj] * (jj+1);
			}
		}
		cout << "Case #" << icase << ": " << ret << endl;
	}
}
