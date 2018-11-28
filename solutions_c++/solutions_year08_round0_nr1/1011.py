#include<iostream>
#include<vector>
#include<fstream>

using namespace std;

int main()
{
	int n;
	ifstream fin("A-large.in",ifstream::in);
	fin>>n;
	for(int i=1;i<=n;i++)
	{
		int s,q;
		vector<string> searchEng;
		vector<string> searchQuery;
		vector<bool> visited;
		vector<int> engSwitch;
		fin>>s;
		//cout<<s<<endl;
		char temp[10];
		fin.getline(temp,100,'\n');
		for(int j=0;j<s;j++)
		{
			char mySEng[100];
			fin.getline(mySEng,100,'\n');
			string mySEng_str(mySEng);
			searchEng.push_back(mySEng_str);
			visited.push_back(false);
			//cout<<mySEng_str<<endl;
		}
		fin>>q;
		//cout<<q<<endl;
		fin.getline(temp,100,'\n');
		for(int j=0;j<q;j++)
		{
			char mySQuery[100];
			fin.getline(mySQuery,100,'\n');
			string mySQuery_str(mySQuery);
			searchQuery.push_back(mySQuery_str);
			//cout<<mySQuery_str<<endl;
		}

		for(int j=0;j<searchQuery.size();j++)
		{
			int myEng;
			int flag = 0;
			for(int k=0;k<searchEng.size();k++)
			{
				if(searchQuery[j].compare(searchEng[k]) == 0)
				{
					visited[k] = true;
					myEng = k;
					break;
				}
			}
			for(int k=0;k<visited.size();k++)
			{
				if(visited[k] == false)
					flag = 1;	
			}
			if(flag == 0)
			{
				engSwitch.push_back(myEng);	
				//cout<<searchEng[myEng]<<endl;
				for(int k=0;k<visited.size();k++)
					visited[k] = false;	
				visited[myEng] = true;
			}
		}
		for(int k=0;k<visited.size();k++)
		{
			if(visited[k] == false)
			{
				engSwitch.push_back(k);
				break;
			}
		}	

		cout<<"Case #"<<i<<": "<<engSwitch.size()-1<<endl;
	}
}
