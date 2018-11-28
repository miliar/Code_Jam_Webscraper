# include <iostream>
# include <vector>
# include <string>
# include <algorithm>

using namespace std;
vector<string> nodes;
vector<string> queries;

int func()
{
	int count = 0,i;
	vector<string> tmp(nodes.begin(), nodes.end());
	for(i=0;i<queries.size();i++)
	{
		vector<string>::iterator vi = find(tmp.begin(),tmp.end(),queries[i]);
		if ( vi != tmp.end() )
		{
			tmp.erase(vi);
			if(tmp.size() == 0)
			{
				count++;
				tmp = nodes;
				vi = find(tmp.begin(),tmp.end(),queries[i]);
				tmp.erase(vi);
			}
		}
	}
	return count;
}

int main()
{
	//freopen("t2.txt","w",stdout);
	int cases,i;
	cin>>cases;
	for(int l=0;l<cases;l++)
	{
		int S;
		cin>>S;
		getchar();
		nodes.clear();
		queries.clear();
		char tt[1024];
		for(i=0;i<S;i++)
		{
			cin.getline(tt,1024);
			string st(tt);
			nodes.push_back(st);
		}
		int Q;
		cin>>Q;
		getchar();
		for(i=0;i<Q;i++)
		{
			cin.getline(tt,1024);
			string st(tt);
			queries.push_back(st);
		}
		cout<<"Case #"<<l+1<<": "<<func()<<endl;
	}
}
