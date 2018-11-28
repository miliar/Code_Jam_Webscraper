#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<algorithm>
#include<functional>

using namespace std;

class MinScalarProduct
{
private:
	long long scalarMultiply(vector<int> &v1, vector<int> &v2)
	{
		long long prod = 0;
		int sz = v1.size();

		for(int i=0;i<sz;i++)
		{
			prod += v1[i]*v2[sz-i-1];
		}

		return prod;
	}

public:
	long long GetMin(vector<int> v1, vector<int> v2)
	{
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end(), less<int>());

		return scalarMultiply(v1, v2);
	}
};

int main()
{
	char line[1000];

	int t;	
	cin.getline(line, sizeof(line));
	istringstream is1(line);
	is1>>t;

	for(int i=0;i<t;i++)
	{
		int n;
		cin.getline(line, sizeof(line));
		istringstream is2(line);
		is2>>n;

		vector<int> v1;
		cin.getline(line, sizeof(line));
		istringstream is3(line);
		for(int j=0;j<n;j++)
		{
			int val;
			is3>>val;
			v1.push_back(val);
		}

		vector<int> v2;
		cin.getline(line, sizeof(line));
		istringstream is4(line);
		for(int j=0;j<n;j++)
		{
			int val;
			is4>>val;
			v2.push_back(val);
		}

		MinScalarProduct msp;
		cout<<"Case #"<<i+1<<": "<<msp.GetMin(v1,v2)<<endl;
	}

	return 0;
}