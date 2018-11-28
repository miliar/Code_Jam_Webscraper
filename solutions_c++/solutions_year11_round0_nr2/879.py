#include <cstring>
#include <iostream>
#include <string>
#include <map>

using namespace std;

int t;
map <string, char> change, oppose;
string inp;

int main(void)
{
	cin>>t;
	for(int caseN=1;caseN<=t;caseN++)
	{
		change.clear();
		oppose.clear();

		int n;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			string str;
			cin>>str;
			change[str.substr(0, 2)]=str[2];
			swap(str[0], str[1]);
			change[str.substr(0, 2)]=str[2];
		}
		
		cin>>n;
		for(int i=0;i<n;i++)
		{
			string str;
			cin>>str;
			oppose[str]=0;
			swap(str[0], str[1]);
			oppose[str]=0;
		}

		cin>>n>>inp;

		string cur;
		for(int i=0;i<inp.size();i++)
		{
			cur+=inp[i];
			if(cur.size()<2) continue;

			string tail=cur.substr(cur.size()-2);
			if(change.count(tail))
			{
				cur=cur.substr(0, cur.size()-2) + change[tail];
			}

			for(int i=0;i<(int)cur.size()-1;i++)
			{
				string tar;
				tar+=cur[i];
				tar+=cur[cur.size()-1];
				if(oppose.count(tar)) { cur=""; break; }
			}
		}

		cout<<"Case #"<<caseN<<": [";
		for(int i=0;i<cur.size();i++)
		{
			if(i) cout<<", ";
			cout<<cur[i];
		}

		cout<<"]"<<endl;

	}
	return 0;
}
