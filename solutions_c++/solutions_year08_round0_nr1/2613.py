#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main()
{
int t=0,noCases;
cin>>noCases;

while (t!=noCases)
{
	t++;	
	int noSwitches=0;
	int noEngines;
	cin>>noEngines;
	cin.ignore(10,'\n');
	vector<string> engines(noEngines);
	for (int countEngines=0;countEngines<noEngines;countEngines++)
	{
		
		getline(cin,engines[countEngines]);
	}
	int noQueries;
	cin>>noQueries;
	cin.ignore(10,'\n');
	vector<string> queries(noQueries);
	for (int countQueries=0;countQueries<noQueries;countQueries++)
	{
		
		getline(cin,queries[countQueries]);
	}
	



	int countNext=0;
	vector<int> count(noEngines);
	for (int y=0;y<count.size();y++)
	{
		count[y]=0;
	}
	for (int i=0;i<queries.size();i++)
	{
		for (int j=0;j<engines.size();j++)
		{
			if((engines[j].compare(queries[i]))==0)
			{
				count[j]++;
			}
		}
		countNext=0;
		for (int k=0;k<count.size();k++)
		{
			if (count[k]>=1)
			{
				countNext++;
		
			}
		}
		if (countNext==noEngines)
		{
			i--;	
			noSwitches++;
			countNext=0;
			for (int l=0;l<count.size();l++)
			{
				count[l]=0;	
			}
		}
	}
	cout<<"Case #"<<t<<": "<<noSwitches<<endl;
}
	return 0;
}
		
	
