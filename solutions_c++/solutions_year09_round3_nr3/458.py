#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream fin("c.txt");
#define cin fin

ofstream fout("out.txt");
#define cout fout

int p, q;
bool prisoner[110];
int released[10];

int F(vector<int>v)
{
	int i, j, ret = 0;
	for(i=0; i<p; i++)
	{
		prisoner[i] = 1;
	}
	for(i=0; i<v.size(); i++)
	{
		j = v[i];
		while(--j >= 0)
		{
			if(prisoner[j])
				ret++;
			else
				break;
		}
		j = v[i];
		while(++j < p)
		{
			if(prisoner[j])
				ret++;
			else
				break;
		}
		prisoner[v[i]] = 0;
	}
	return ret;
}

int Solve()
{
	vector<int>v;
	int i, j, mn = INT_MAX;
	for(i=0; i<q; i++)
	{
		v.push_back(released[i]);
	}
	do
	{
		mn = min(mn, F(v));
	}
	while(next_permutation(v.begin(), v.end()));
	return mn;
}

int main()
{
	int n, i, j;
	cin>>n;
	for(i=0; i<n; i++)
	{
		cin>>p>>q;
		for(j=0; j<q; j++)
		{
			cin>>released[j];
			released[j]--;
		}
		int ans = Solve();
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}