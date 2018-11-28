
#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

ifstream fin("c.in");
#define cin fin

ofstream fout("c.out");
#define cout fout

long long solve(long long r, long long k, long long n, vector<long long>g)
{
	vector<vector<long long> >vec;
	map<vector<long long>, long long>mp;
	vector<long long>v;
	long long totalSum = 0;
	
	long long i = 0, j, jj;
	while(1)
	{
		if(i == r)
		{
			return totalSum;
		}
		if(mp.find(g) != mp.end())
			break;
		vec.push_back(g);
		mp[g] = i;
		long long sum = 0;
		for(j=0; j<n; j++)
		{
			if(sum + g[j] <= k)
				sum += g[j];
			else
			{
				vector<long long>tmp(n);
				for(jj=0; jj<n; jj++)
				{
					tmp[jj] = g[(j + jj) % n];
				}
				g = tmp;
				break;
			}
		}
		v.push_back(sum);
		totalSum += sum;
		i++;
	}

	long long ret = 0;
	for(j=0; j<mp[g]; j++)
	{
		ret += v[j];
	}
	
	long long sum = 0;
	for(j=mp[g]; j<i; j++)
	{
		sum += v[j];
	}
	
	r -= mp[g];
	
	long long m = r / (i - mp[g]);
	ret += (sum * m);

	
	for(j=0; j<r%(i - mp[g]); j++)
	{
		ret += v[mp[g] + j];
	}
	
	return ret;
}

int main()
{
	long long i, j, t, r, k, n;
	vector<long long>g;
	cin>>t;
	for(i=0; i<t; i++)
	{
		cin>>r>>k>>n;
		g.resize(n);
		for(j=0; j<n; j++)
		{
			cin>>g[j];
		}
		long long euro = solve(r, k, n, g);
		cout<<"Case #"<<i+1<<": "<<euro<<endl;
	}
	return 0;
}
