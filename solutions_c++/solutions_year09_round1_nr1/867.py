#include <fstream>
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

vector<bool> happy_vec[11], visited[11], known[11];

bool happy(int n, int base)
{
	if(happy_vec[base].size() < n-1)
	{
		happy_vec[base].resize(n+5);
		visited[base].resize(n+5);
		known[base].resize(n+5);
	}
	if(1 == n)	return true;
	if(0 == n)	return false;
	
	if(visited[base][n])
	{
		if(known[base][n])
		{
			return happy_vec[base][n];
		}
		else
		{
			known[base][n] = true;
			return (happy_vec[base][n] = false);
		}
	}
	
	int k=0, tmp = n;
	while(tmp > 0)
	{
		k += ((tmp%base)*(tmp%base));
		tmp /= base;
	}
	
	known[base][n] = true;
	visited[base][n] = true;
	happy_vec[base][n] = happy(k,base);
	return happy_vec[base][n];
}

int main()
{
	int T;
	string str;
	ifstream fin("A-small-attempt0.in");
	ofstream fout("Multi-base happiness.txt");
	
	fin>>T;
	
	getline(fin,str);
	for(int test=1; test<=T; test++)
	{
		getline(fin,str);
		stringstream ss(str);
		vector<int> bases;
		int k;
		while(ss>>k)	bases.push_back(k);
		
		for(int i=2; ;i++)
		{
			bool hpy=true;
			for(int j=0; j<bases.size(); j++)	
			{
				int m=0, tmp = i;
				while(tmp > 0)
				{
					m += ((tmp%bases[j])*(tmp%bases[j]));
					tmp /= bases[j];
				}
				if(!happy(m,bases[j]))
				{
					hpy = false;
					break;
				}
			}
			if(hpy)
			{
				fout<<"Case #"<<test<<": "<<i<<"\n";
				break;
			}
		}
	}
	return 0;
}
