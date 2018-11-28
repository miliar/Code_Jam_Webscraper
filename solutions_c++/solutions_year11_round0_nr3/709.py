#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <iostream>


using namespace std;


int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int t;
	cin>>t;
	for (int aaa=0;aaa<t;aaa++)
	{
		int n;
		cin>>n;
		vector<int> v(n);
		int cnt = 0;
		int sumX = 0;
		int sumC = 0;

		for (int i=0;i<n;i++)
		{
			cin>>v[i];
			sumX ^= v[i];
			sumC += v[i];
		}

		sumC -= *min_element(v.begin(),v.end());
		
		cout<<"Case #"<<aaa+1<<": ";
		if (sumX != 0)
			cout<<"NO";
		else
			cout<<sumC;
		cout<<endl;
	}
	
    return 0;
}