#include <set>
#include <list>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <assert.h>

using namespace std;

int calc(int K, vector<int> indices)
{
	vector<int> val(K);
	for (int i=0; i<K; ++i)
		val[i] = -1;
	int co = 0;
	int nextco = 1;
	list<int> wheretoput;
	for (int i=0; i<K; ++i)
		wheretoput.push_back(i);
	list<int>::iterator it = wheretoput.begin();
	for (int i=1; i<=K; ++i)
	{
		for (nextco=1; nextco<i; nextco++)
		{
			it++; if (it==wheretoput.end()) it = wheretoput.begin();
		}
		val[*it] = i;
		it = wheretoput.erase(it);
		if (it==wheretoput.end()) it = wheretoput.begin();
		//if (i%1000==0) cout << i << endl;
	}
	for (int i=0; i<(int)indices.size()-1; ++i)
		cout << val[indices[i]-1] << " ";
	cout << val[*indices.rbegin()-1];
	return 0;
}

int main(int argc, char *argv[])
{
	if (argc<2)
	{
		cout << "Filename needed\n";
		return -1;
	}
	fstream fin(argv[1]);
	int numcases;
	fin >> numcases;
	for (int i=0; i<numcases; ++i)
	{
		int n,K;
		vector<int> indices;
		fin >> K >> n;
		for (int j=0; j<n; ++j)
		{
			int v;
			fin >> v;
			indices.push_back(v);
		}
		cout << "Case #" << i+1 << ": "; calc(K,indices); cout << endl;
	}
	fin.close();
	return 0;
}