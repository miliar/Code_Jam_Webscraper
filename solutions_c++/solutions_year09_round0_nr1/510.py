#include <iostream>
#include <map>
#include <set>
#include <string>
#include <queue>
using namespace std;

bool ok[20][30];
set<string> have;
vector<string> vs1;
vector<string> vs2;
int ans;
int L, D, N;

bool Init(string & str, int &i)
{
	i = 0;
	if(str[i] != '(')
	{
		if(!ok[0][str[i]-'a']) return false;
		string ts ;
		ts += str[i];
		vs1.push_back(ts);
		i++;
	}
	else 
	{
		if(str[i] == '(') i++;
		while(str[i] != ')')
		{
			if(ok[0][str[i]-'a']) 
			{
				string ts ;
				ts += str[i];
				vs1.push_back(ts);
			}
			i++;
		}
		if(str[i] == ')')i++;
	}
	return true;
}

void getans(string &str)
{
	int len = 0;

	int st;
	if(!Init(str, st)) return ;
	

	for(int i = st; i < str.length();)
	{
		
		if(str[i] == '(') 
		{
			len++;
			i++;
			while(str[i] != ')')
			{
				if(!ok[len][str[i]-'a']) 
				{
					i++;
					continue;
				}
				for(int j = 0; j < vs1.size(); j++)
				{
					string ts = vs1[j];
					ts += str[i];
					if(have.find(ts)!= have.end()) 
					{
						vs2.push_back(ts);
					}
				}
				i++;
			}
			if(str[i] == ')')i++;
		}
		else 
		{
			len++;
			if(!ok[len][str[i]-'a']) 
			{
				i++;
				continue;
			}
			for(int j = 0; j < vs1.size(); j++)
			{
				string ts = vs1[j];
				ts += str[i];
				if(have.find(ts)!= have.end()) 
				{
					vs2.push_back(ts);
				}
			}
			i++;
		}
	vs1.swap(vs2);
	vs2.clear();
	}
	ans = vs1.size();
}


int main()
{
	string str;
	int i;
	freopen("A-large.in", "r", stdin);
	freopen("aout.txt", "w", stdout);
	while(cin>>L>>D>>N)
	{
		have.clear();
		memset(ok, 0, sizeof(ok));
		for( i = 0; i < D; i++)
		{
			cin>>str;
			string ts;
			for(int j = 0; j < str.length(); j++)
			{
				ts += str[j];
				ok[j][str[j]-'a'] = true;
				have.insert(ts);
			}
		}
		for( i = 0; i < N; i++)
		{
			vs1.clear();
			vs2.clear();
			ans = 0;
			cin>>str;
			getans(str);
			cout<<"Case #"<<i+1<<": "<<ans<<endl;
		}
	}
	return 0;
}
