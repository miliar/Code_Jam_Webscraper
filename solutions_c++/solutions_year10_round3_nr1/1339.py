#include <fstream>
//#include <iostream>
#include <string>
#include <cmath>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int t;
	cin>>t;
	int n;
	vector<long long> left,right;
	for(int i=0;i<t;i++)
	{
		cin>>n;
		int sum=0;
		left.clear();
		right.clear();
		int a,b;
		for(int j=0;j<n;j++)
		{
			cin>>a>>b;
			left.push_back(a);
			right.push_back(b);
		}
		for(int j=0;j<n;j++)
		{
			long long v1,v2,v3;
			v1=right[j]-left[j];
			for(int k=j+1;k<n;k++)
			{
				v2=left[k]-left[j];
				v3=right[k]-left[j];
				if(v2*(v3-v1)<=0)
					sum++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<sum<<endl;
	}
	return 0;
}