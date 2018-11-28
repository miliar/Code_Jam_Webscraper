#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <fstream>
using namespace std;

int CalcSwitches(const map<string,int> &SearchEngines, const vector<string> &vQueries);
int main()
{
	ifstream fin("test.in");
	ofstream fout("test.out");
	int N=0; // N test cases
	fin >> N;
	vector<int> res(N);

	for(int i = 0; i< N;++i)
	{

		// read inputs

		// read search engines
		int nS = 0; 
		fin >> nS;
		map<string,int> searchEngines;
		string s;
		getline(fin,s);
		for(int j = 0; j < nS; j++)
		{
			getline(fin,s);
			searchEngines.insert(make_pair<string,int>(s,j));
		}

		// read queries
		int nQ = 0;
		fin >> nQ;
		vector<string>  vQ;
		string q;
		getline(fin,q);
		for(int j = 0; j < nQ; j++)
		{
			getline(fin,q);
			vQ.push_back(q);
		}

		//calculate switches

		res[i] = CalcSwitches(searchEngines,vQ);
	}

	// output 
	for(int i = 0; i < N; i++)
	{
		fout << "Case #"<<i+1<<": "<<res[i]<<endl;
	}
	fin.close();
	fout.close();
	// exit
	return 0;

}
unsigned int Min(int * arr, unsigned int size, int ex)
{
	unsigned int res =  ~0;
	for (int i = 0; i < size; i++)
	{
		if (i != ex)
		{
			if (res > arr[i])
			{
				res=arr[i];
			}
		}
		
	}
	return res;
}
int CalcSwitches(const map<string,int> &SearchEngines, const vector<string> &vQueries)
{

	int res = vQueries.size();
	int *nCostN = new int[SearchEngines.size()];
	memset(nCostN,0,sizeof(int)*SearchEngines.size());
	
	
	for ( int rit = vQueries.size()-2, last = rit+1;rit >=0; --rit,--last)
	{
		int i = SearchEngines.find( vQueries[last])->second;
		int j = SearchEngines.find(vQueries[rit])->second;

		for (int k = 0; k < SearchEngines.size(); k++)
		{
			if(k!=j)
			{
				if(k==i)
				{
					nCostN[k]=Min(nCostN,SearchEngines.size(),i)+1;
				}
				
			}
		}
	}
	if (vQueries.size() >0)
	{
		res = Min(nCostN,SearchEngines.size(),SearchEngines.find(vQueries[0])->second);
	}
	else
	{
		res = 0;
	}
	
	delete[] nCostN;
	nCostN = NULL;
	return res;
}
