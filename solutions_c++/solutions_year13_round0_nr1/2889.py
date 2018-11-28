#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<cmath>
#include<queue>
using namespace std;
typedef long long LL;
const double pi=acos(-1.0);
string a[4];
bool test(char c)
{
	for(int i=0;i<4;i++)
	{
		bool win=true;
		for(int j=0;j<4;j++)
		{
			if(a[i][j]==c || a[i][j]=='.') win=false;
		}
		if(win) return true;
	}
	for(int i=0;i<4;i++)
	{
		bool win=true;
		for(int j=0;j<4;j++)
		{
			if(a[j][i]==c || a[j][i]=='.') win=false;
		}
		if(win) return true;
	}
	bool win=true;
	for(int i=0;i<4;i++)
	{
		if(a[i][i]==c || a[i][i]=='.') win=false;
	}
	if(win) return true;
	win=true;
	for(int i=0;i<4;i++)
	{
		if(a[i][3-i]==c || a[i][3-i]=='.') win=false;
	}
	if(win) return true;
	return false;
}
bool has()
{
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(a[i][j]=='.') return true;
		}
	}
	return false;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n;
	scanf("%d",&n);	
	for(int tc=1;tc<=n;tc++)
	{
		for(int i=0;i<4;i++) cin>>a[i];
		cout<<"Case #"<<tc<<": "; 
		if(test('O')) cout<<"X won"<<endl;
		else if(test('X')) cout<<"O won"<<endl;
		else if(has()) cout<<"Game has not completed"<<endl;
		else cout<<"Draw"<<endl;
	}
	fclose(stdout);
	return 0;
}
