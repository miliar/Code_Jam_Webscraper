#include <iostream>
#include <vector>

using namespace std;

vector<int> qq;
vector<bool> qs;

vector<bool> s;

int p,q;
int mincoin;

int dfs(int n, int coins)
{
	if(coins>mincoin) return mincoin;
	if(n==0) return coins;
	int ret=-1;
	for(int i=0;i<q;i++)
		if(qs[i])
		{
			int out=qq[i];
			qs[i]=false;
			s[out]=false;

			int c=0;
			for(int j=out-1;j>=0;j--)
				if(s[j]) c++; else break;
			for(int j=out+1;j<p;j++)
				if(s[j]) c++; else break;

			if(ret==-1)
				ret=dfs(n-1,coins)+c;
			else
				ret=min(ret,dfs(n-1,coins)+c);
			s[out]=true;
			qs[i]=true;
		}
	return coins+ret;
}

int main()
{
	int TestCase;
	cin >> TestCase;
	for(int ti=0;ti<TestCase;ti++)
	{
		cin >> p >> q;

		qq.resize(q+1);
		qs.resize(q+1);
		s.resize(p+1);

		for(int i=0;i<p;i++) s[i]=true;

		for(int i=0;i<q;i++)
			cin >> qq[i];

		for(int i=0;i<q;i++)
			qq[i]--;

		for(int i=0;i<q;i++) qs[i]=true;

		mincoin=999999999;

		cout << "Case #" << ti+1 << ": " << dfs(q,0) << endl;
	}
	return 0;
}
