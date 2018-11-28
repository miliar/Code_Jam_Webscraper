#include<vector>
#include<algorithm>
#include<iostream>
#include<fstream>

using namespace std;

int main(int agrc, char* agrv[])
{

	if(agrc < 2)return 0;
	ifstream is(agrv[1]);
	ofstream os("A.out");

	int t;
	is>>t;
	for(int casenum = 0; casenum < t; casenum++)
	{
		int n;
		is>>n;
		vector<int> v1;
		vector<int> v2;
		for(int i = 0 ; i < n ; i++)
		{
			int temp;
			is>>temp;
			v1.push_back(temp);
		}
		for(int i = 0 ; i < n ; i++)
		{
			int temp;
			is>>temp;
			v2.push_back(temp);
		}
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		int res = 0;
		for(int i = 0 ; i < n; i ++)
		{
			res += v1[i] * v2[n - i - 1];
		}
		os<<"Case #"<<casenum + 1<<": "<<res<<endl;
	}
	return 0;
}