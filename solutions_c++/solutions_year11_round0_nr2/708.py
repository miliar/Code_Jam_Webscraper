#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <iostream>


using namespace std;

char rule[300][300];
bool ban[300][300];


int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int t;
	cin>>t;
	for (int aaa=0;aaa<t;aaa++)
	{
		memset(rule, 0, sizeof(rule));
		memset(ban, 0, sizeof(ban));

		int r;
		cin>>r;
		for (int i=0;i<r;i++)
		{
			string s;
			cin>>s;

			if (rule[s[0]][s[1]])
				throw 0;

			rule[s[0]][s[1]] = s[2];
			rule[s[1]][s[0]] = s[2];
		}
		cin>>r;
		for (int i=0;i<r;i++)
		{
			string s;
			cin>>s;
			ban[s[0]][s[1]] = 1;
			ban[s[1]][s[0]] = 1;
		}
		cin>>r;
		vector<char> v;
		string s;
		cin>>s;
		for (int i=0;i<r;i++)
		{
			v.push_back(s[i]);
			while (v.size() >= 2 && rule[v[v.size() -2]][v[v.size() - 1]] != 0)
			{
				char t = rule[v[v.size() -2]][v[v.size() - 1]];
				v.pop_back();
				v.pop_back();
				v.push_back(t);
			}
			for (int i=0;i<(int)v.size() - 1;i++)
				if (ban[v[i]][v.back()])
					v.clear();
		}

		cout<<"Case #"<<aaa+1<<": ";

		cout<<"[";
		for (int i=0;i<(int)v.size();i++)
		{
			if (i)
				cout<<", ";
			cout<<v[i];
		}

		cout<<"]";


		cout<<endl;
	}
	
    return 0;
}