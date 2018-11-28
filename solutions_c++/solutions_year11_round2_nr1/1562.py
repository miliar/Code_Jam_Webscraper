#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <cstdio>

using namespace std;

void prepere()
{
#ifdef _DEBUG
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
}

void solve()
{
	int t;
	cin>>t;
	for (int q=1;q<=t;++q)
	{
		int n;
		cin>>n;
		char ch;
		vector<int> win(n,0), all(n,0);
		vector<vector<int> > opp(n), board(n,vector<int>(n,0));
		vector<long double> res(n),r1(n),r2(n,0),r3(n,0);
		for (int i=0;i<n;++i)
			for (int j=0;j<n;++j)
			{
				cin>>ch;
				board[i][j]=(ch=='1'?1:0);
				if (ch=='1')
				{
					win[i]++;
					all[i]++;
					opp[i].push_back(j);
				}
				else if (ch=='0')
				{
					all[i]++;
					opp[i].push_back(j);
				}
			}
		for (int i=0;i<n;++i)
		{
			r1[i]=(win[i]+0.0)/all[i];
		}
		for (int i=0;i<n;++i)
		{
			for (int j=0;j<opp[i].size();++j)
			{
				r2[i]+=(win[opp[i][j]]-board[opp[i][j]][i]+0.0)/(all[opp[i][j]]-1);
			}
			r2[i]/=opp[i].size();
		}
		for (int i=0;i<n;++i)
		{
			for (int j=0;j<opp[i].size();++j)
			{
				r3[i]+=r2[opp[i][j]];
			}
			r3[i]/=opp[i].size();
		}
		cout<<"Case #"<<q<<":\n";
		for (int i=0;i<n;++i)
		{
			//cout<<i+1<<" "<<r1[i]<<" "<<r2[i]<<" "<<r3[i]<<" ";
		
			res[i]=0.25*r1[i]+0.5*r2[i]+0.25*r3[i];
			cout<<res[i]<<endl;
		}
	}
}

int main()
{
	prepere();
	solve();
	return 0;
}
