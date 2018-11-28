#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	int cases;
	cin>>cases;
	for(int i=0;i<cases;i++)
	{
		int engines;
		cin>>engines;
		vector<string> e;
		for(int j=0;j<engines;j++)
		{
			
			char ms[200];
			cin.getline(ms,200);
			if(ms[0]=='\n' || ms[0]==0 || ms[0]=='\r') 
			{
				j--;continue;
			}
			e.push_back(string(ms));

		}
		int query;
		cin>>query;
		int k=0;
		int res=0;
		map<string,bool> used;
		for(int j=0;j<query;j++)
		{
			
			char ms2[200];
			cin.getline(ms2,200);
			if(ms2[0]=='\n' || ms2[0]==0 || ms2[0]=='\r') 
			{
				j--;continue;
			}
			string ms(ms2);
			//if(find(e.begin(),e.end(),ms)==e.end()) continue;
			if(used[ms]) continue;
			used[ms]=true;
			k++;
			if(k==engines)
			{
				used.clear();
				k=0;
				res++;
				used[ms]=true;
				k++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<res<<endl;

	}
}