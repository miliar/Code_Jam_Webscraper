#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
using namespace std;

int main()
{
	string str="welcome to code jam";
	int n;
	cin>>n;
	string temp;
	getline(cin,temp,'\n');
	for(int c=1;c<=n;c++)
	{
		string s;
		getline(cin,s,'\n');
		vector<vector<int> > v(str.size(),vector<int> (s.size(),0));
		v[0][0]=(s[0]==str[0]);
		for(int i=1;i<v[0].size();i++)
		{
			v[0][i]=(v[0][i-1]+(s[i]==str[0]))%10000;
		}	
		for(int i=1;i<v.size();i++)
		{
			for(int j=1;j<v[i].size();j++)
			{
				v[i][j]=(v[i][j-1]+(s[j]==str[i]?v[i-1][j]:0))%10000;
				
			}
		}
		/*for(int i=0;i<v.size();i++)
		{
			for(int j=0;j<v[i].size();j++)
			{
				cout<<v[i][j]<<" ";
			}
			cout<<endl;
		}*/
		printf("Case #%d: %04d\n",c,v.back().back());
	}
	return 0;
}
