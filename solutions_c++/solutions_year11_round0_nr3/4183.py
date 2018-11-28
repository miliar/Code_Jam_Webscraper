
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

ifstream fin("input.txt");
#define cin fin

ofstream fout("output.txt");
#define cout fout

int eshta(vector<int> v)
{
	int xor = 0;
	int tot = 0;

	int i;
	for(i=0; i<v.size(); i++)
	{
		xor ^= v[i];
		tot += v[i];
	}
	if(xor == 0)
	{
		return tot;
	}
	else
	{
		return -1;
	}
}

int main()
{
	int t, n, i, j;
	cin>>t;
	for(i=0; i<t; i++)
	{
		cin>>n;
		vector<int> v(n);
		for(j=0; j<n; j++)
		{
			cin>>v[j];
		}

		sort(v.begin(), v.end());
		cout<<"Case #"<<i+1<<": ";
		int sum = eshta(v);
		if(sum == -1)
		{
			cout<<"NO";
		}
		else
		{
			sum -= v[0];
			cout<<sum;
		}
		cout<<endl;
	}
	return 0;
}