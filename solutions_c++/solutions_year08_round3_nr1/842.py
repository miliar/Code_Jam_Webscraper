#include <iostream>
#include <vector>
#include <list>
#include <deque>
#include <algorithm>
#include <iomanip>
#include <fstream>
#include <functional>
using namespace std;

int main()
{
	ifstream fin("A-small-attempt2.in");
	ofstream fout("A-small-attempt2.out");
	int n;
	fin>>n;
	for(int i=0;i!=n;++i)
	{
		long result=0;
		int P,K,L,pos=0,cnt=1;
		vector<int> num;
		fin>>P>>K>>L;
		for(int i1=0;i1!=L;++i1)
		{
			int temp;
			fin>>temp;
			num.push_back(temp);
		}
		sort(num.begin(),num.end(),greater<int>());
		while(cnt<=P)
		{
			for(int j=1;j<=K&&pos<num.size();++j)
			{
				result+=num[pos++]*cnt;
			}
			cnt++;
		}
		fout<<"Case #"<<i+1<<": "<<result<<endl;
	}
	return 0;

}