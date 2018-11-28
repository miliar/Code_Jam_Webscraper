// CJ2010.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#define size size()
#define all(s) s.begin(),s.end()
#define rall(s) s.rbegin(),s.rend()
#define ll long long

using namespace std;

int main(int argc, char* argv[])
{
	freopen( "C-small-attempt0.in","rt",stdin);
	freopen( "C-small.out","wt",stdout);
	int t;
	cin>>t;
	
	for( int ct = 1; ct <= t; ct++)
	{
		queue<int> p;// = new queue<int>();
		queue<int> q;
		int r,k,n;
		cin>>r>>k>>n;
		for(int i = 0; i< n;++i)
		{
			int l;
			cin>>l;
			p.push(l);
		}
		int res = 0;
		for(int i =0;i<r;++i)
		{
			int cnt = 0;
			while((!p.empty())&&cnt+p.front()<=k)
			{
				cnt+=p.front();
				q.push(p.front());
				p.pop();
			}
			res += cnt;
			while(!q.empty())
			{
				p.push(q.front());
				q.pop();
			}
		}
		cout<<"Case #"<<(ct)<<": "<<res<<endl;
	/*	int n,k;
		cin>>n>>k;
		int p = (n*2)-1;
		if( p > k )
		{
			cout<<"Case #"<<(ct)<<": OFF\n";
		}
		else
		{
			if( (k - p)%2==1)
				cout<<"Case #"<<(ct)<<": OFF\n";
			else
				cout<<"Case #"<<(ct)<<": ON\n";
		}*/
	}
	return 0;
}

