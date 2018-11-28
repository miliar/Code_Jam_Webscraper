#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <iomanip>
using namespace std;
int is_won(const string &a)
{
	char c='T';
	for (int i=0;i<a.size();i++)
	{
		if (c=='T')
			c = a[i];
		else
		{
			if (a[i]=='T')
				continue;
			if (c!=a[i])
				return 0;
		}
	}
	if (c=='.')
		return 0;
	return c;

}
int is_won(const vector<string>&a)
{

	for (int i=0;i<4;i++)
	{
		string temp;
		for (int j=0;j<4;j++)
		{
			temp+=a[i][j];
		}
		char winner = is_won(temp);
		if (winner)
			return winner;
	}
	for (int i=0;i<4;i++)
	{
		string temp;
		for (int j=0;j<4;j++)
		{
			temp+=a[j][i];
		}
		char winner = is_won(temp);
		if (winner)
			return winner;
	}
	{
		string temp;
		for (int j=0;j<4;j++)
		{
			temp+=a[j][j];
		}
		char winner = is_won(temp);
		if (winner)
			return winner;
	}
	{
		string temp;
		for (int j=0;j<4;j++)
		{
			temp+=a[3-j][j];
		}
		char winner = is_won(temp);
		if (winner)
			return winner;
	}
	return 0;	
}
int is_complete(const vector<string>&a)
{

	for (int i=0;i<4;i++)
	{
		for (int j=0;j<4;j++)
		{
			if (a[i][j]=='.')
				return 0;
		}
	}
	return 1;	
}
int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int test;
	cin>>test;
	for (int curtest =0; curtest < test;curtest++)
	{
		vector<string> m(4);
		for (int i=0;i<4;i++)
		{
			cin>>m[i];
		}
		char winner = is_won(m);
		cout<<"Case #"<<curtest +1<<": ";
		if (winner)
		{
			cout<<winner<<" won";
		}
		else
		{
			if (is_complete(m))
			{
				cout<<"Draw";
			}
			else
			{
				cout<<"Game has not completed";
			}
		}
		cout<<"\n";
	}
	
	

	return 0;
}