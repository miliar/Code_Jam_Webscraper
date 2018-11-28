#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;
int winner(vector<string> b,char c)
{
	int i,j,count;
	//cout<<"In winner\n";
	for(i=0;i<4;i++)
	{
		count=0;
		for(j=0;j<4;j++) {
			//cout<<b[i][j]<<" ";
			if(b[i][j]==c || b[i][j]=='T')
			{
				count++;
			}
		}
		//cout<<count;
		if(count==4)
		return 1;
	}
	//cout<<"No row\n";
	for(i=0;i<4;i++)
	{
		count=0;
		for(j=0;j<4;j++) {
			if(b[j][i]==c || b[j][i]=='T')
			count++;
		}
		if(count==4)
		return 1;
	}
	//cout<<"No Col\n";	
	count=0;
	for(j=0;j<4;j++) 
	{
			if(b[j][j]==c || b[j][j]=='T')
			count++;
	}
	if(count==4)
	return 1;
	//cout<<"No dig 1\n";
	count=0;
	for(j=0;j<4;j++) 
	{
			if(b[j][3-j]==c || b[j][3-j]=='T')
			count++;
	}
	if(count==4)
	return 1;
	//cout<<"No dig 2\n";	
	return 0;
}
int empty(vector<string> b)
{
	int i,j;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++) {
			if(b[j][i]=='.')
			return 1;
		}
	}
	return 0;
}
int main()
{
	int t,i,ans=-1;
	vector<string> status;
	status.push_back("X won");
	status.push_back("O won");
	status.push_back("Draw");
	status.push_back("Game has not completed");
	vector<string> b;
	string s;
	cin>>t;
	int tc=0;
	
	while(t--)
	{
		ans=-1;
		b.clear();
		for(i=0;i<4;i++)
		{
			cin>>s;
			b.push_back(s);
		}
		//cout<<"start game\n";
		if(winner(b,'X'))
		ans=0;
		else if(winner(b,'O'))
		ans=1;
		else if(!empty(b))
		ans=2;
		else
		ans=3;
		tc++;
		cout<<"Case #"<<tc<<": "<<status[ans]<<endl;
	}
	return 0;
}
