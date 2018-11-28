#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <set>
#include <stack>
#include <map>
#include <utility>

using namespace std;

int T,C,D,N;
map<pair<char,char>,string> combine;
map<char,char> opposed;
string invoke,result;

void solve()
{	
	int i,j;
	char c1,c2;
	bool flag;
	result=invoke[0];
	for (i=1;i<N;i++)
	{
		flag=false;
		result+=invoke[i];
		/*if (result.size()>1)
		{
			while ((combine.count(make_pair(c1=result[result.size()-1],c2=result[result.size()-2]))))
			{
				result=result.erase(result.size()-2,result.size());
				result+=combine[make_pair(c1,c2)];
				flag=true;
				if (result.size()<=1)
					break;
			}
		}/**/
		if (result.size()>1)
		{
			if (combine.count(make_pair(c1=result[result.size()-1],c2=result[result.size()-2])))
			{
				result=result.erase(result.size()-2,result.size());
				result+=combine[make_pair(c1,c2)];
				flag=true;
			}
		}/**/
		if (!flag)
		{
			for (j=0;j<result.size()-1;j++)
				if (opposed[result[j]]==result[result.size()-1])
				{
					result.clear();
					//result=result.erase(j,result.size());
					break;
				}
		}
	}
}

int main()
{
	string s;
	int i,j,k;
	ifstream cin("B-small.in");
	ofstream cout("B-small.out");
	cin >> T;
	for (i=0;i<T;i++)
	{
		result.clear();
		combine.clear();
		opposed.clear();
		cin >> C;
		for (j=0;j<C;j++)
		{
			cin >> s;
			combine[make_pair(s[0],s[1])]=s[2];
			combine[make_pair(s[1],s[0])]=s[2];
		}
		cin >> D;
		for (j=0;j<D;j++)
		{
			cin >> s;
			opposed[s[0]]=s[1];
			opposed[s[1]]=s[0];
		}
		cin >> N;
		cin >> invoke;
		solve();
		cout << "Case #" << i+1 << ": [";
		if (!result.empty())
		{
			cout << result[0];
			for (k=1;k<result.size();k++)
				cout << ", " << result[k];
		}
		cout << "]" << endl;
	}
	return 0;
}