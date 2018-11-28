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
	/*
	for(int i = 0; i < vs1.size(); i++)
	{
		if(have.find(vs1[i])!=have.end()) ans++;
	}*/
}


int main()
{
	string str;
	int i;
//	freopen("as.in", "r", stdin);
//	freopen("as.out", "w", stdout);
	
	freopen("al.in", "r", stdin);
	freopen("al.out", "w", stdout);
	while(scanf("%d%d%d", &L, &D, &N)!=EOF)
	{
		have.clear();
		memset(ok, 0, sizeof(ok));
		for( i = 0; i < D; i++)
		{
			char str[20];
			scanf("%s", str);
			string ts;
			for(int j = 0; j < strlen(str); j++)
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
			char s[2000];
			scanf("%s", s);
			string str(s);
			getans(str);
			printf("Case #%d: %d\n", i+1, ans);
		}
	}
	return 0;
}
