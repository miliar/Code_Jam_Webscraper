#include<iostream>
#include<string>
#include<map>
#include<vector>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int tt=0;tt<t;tt++)
	{
		int s;
		cin>>s;
		string tmp;
		getline(cin,tmp);
		string *name = new string[s];
		map<string,int> *flag;
		for(int ts=0;ts<s;ts++)
		{
			getline(cin,name[ts]);	
			//cout<<name[ts]<<endl;
			//cin>>name[ts];
			//flag[name[ts]] = 0; 
		}
		//cout<<"get out"<<endl;
		int q;
		int cnt = 0;
		int swit = 0;
		cin>>q;
		getline(cin,tmp);
		flag = new map<string,int>;
		for(int i = 0;i<q;i++)
		{
			string temp;
			getline(cin,temp);
			//cin>>temp;
			if((*flag).find(temp) == (*flag).end())
			{
				(*flag)[temp] = 1;
				cnt++;
			}
			if(cnt == s )
			{
				swit++;
				delete flag;
				flag = new map<string,int>;
				(*flag)[temp] = 1;
				cnt=1;
			}
		}
		cout<<"Case #"<<tt+1<<": "<<swit<<endl;
	}
}

