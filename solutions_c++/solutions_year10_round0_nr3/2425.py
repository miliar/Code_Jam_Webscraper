#include<iostream>
#include<fstream>
#include<cmath>
#include<vector>
using namespace std;

int main()
{
	ifstream fin;
	fin.open("input.txt");
	
	int N;
	fin>>N;
	
	for(int z=0;z<N;z++)
	{
		int runs;
		vector<int> grps;
		int n_grps;
		long long revenue;
		int capacity;
		
		fin>>runs>>capacity>>n_grps;
		int grp_size;
		
		for(int i=0;i<n_grps;i++)
		{
			fin>>grp_size;
			if(i!=0)
				grps.push_back(grp_size + grps[i-1]);
			else
				grps.push_back(grp_size);
		}
		
		revenue = 0;
		for(int i=0;i<runs;i++)
		{
			int j;
			for(j=0;j<grps.size();j++)
			{
				if(grps[j]>capacity)
				break;
			}
			revenue += grps[j-1];
			if(j != grps.size() )
			{
				for(int k=j;k<n_grps;k++)
				{
					grps[k] -= grps[j-1];
				}
				for(int k=0;k<j;k++)
				{
					grps.push_back(grps[0] + grps[grps.size()-k-1]);
					grps.erase(grps.begin());
				}
			}	
		}
		grps.clear();
		cout<<"Case #"<<z+1<<": "<<revenue<<endl;
	}
	return 0;
}
