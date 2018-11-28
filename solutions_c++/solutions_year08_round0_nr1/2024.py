#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	int switch_number;
	int case_number;
	int engine_number;
	int query_number;
	string engine_name;
	vector<string> engines;
	string query_name;
	vector<string> queries;
	vector<bool> is_seen;
	int number_of_different_queries;
	string tmp;
	cin>>case_number;
	//cout<<"case number="<<case_number<<endl;
	for(int i=0;i<case_number;i++)
	{
		switch_number=0;
		number_of_different_queries=0;
		cin>>engine_number;
		cin.ignore();
		//getline(cin,engine_number);
		//cout<<"number of engines="<<engine_number<<endl;
		for(int j=0;j<engine_number;j++)
		{
			//cin>>engine_name;
			getline(cin,engine_name);
			//cout<<"engine name="<<engine_name<<endl;
			engines.push_back(engine_name);
			is_seen.push_back(false);
		}
		//cout<<"test1"<<endl;
		cin>>query_number;
		cin.ignore();
		//cout<<"number of queries"<<query_number<<endl;
		for(int j=0;j<query_number;j++)
		{
			getline(cin,query_name);
			//cout<<"query name"<<query_name<<endl;
			queries.push_back(query_name);
		}
		for(int j=0;j<query_number;j++)
		{
			int k;
			tmp=queries[j];
			for(k=0;;k++)
			{
				if(tmp==engines[k]) break;
			}
			if(is_seen[k]==false) {
				is_seen[k]=true;
				number_of_different_queries++;
				//cout<<engines[k]<<" "<<k<<" is seen"<<endl;
			}
			if(number_of_different_queries==engine_number)
			{
				//switch
				//cout<<"switching"<<endl;
				switch_number++;
				for(int z=0;z<engine_number;z++)
					is_seen[z]=false;
				is_seen[k]=true;
				number_of_different_queries=1;
			}
		}
		cout<<"Case #"<<i+1<<": "<<switch_number<<endl;
		is_seen.clear();
		engines.clear();
		queries.clear();
	}
	return 0;
}

