#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <queue>
#include <cmath>
#include <string>

using namespace std;
#define pb push_back
vector< vector<int> > ids;
int N;

int recu(int idx)
{
	if(ids[idx].size()==0) return 1;
	vector<int> c;
	for(int i=0;i<ids[idx].size();i++)
	c.pb(recu(ids[idx][i]));
	sort(c.begin(),c.end());
	int ans = 1 + ids[idx].size();
	for(int i=0;i<c.size();i++)
	ans = max( ans, c[i] + (int)c.size()-1-i);
	return ans;
}

int main()
{

	int ctr = 0 ;
	int C;
	cin>>C;
	while(C--)
	{
		ctr++;
		cin>>N;
		vector<string> names(N);
		vector< vector<string> > rec(N);
		ids.clear();
		ids.resize(N);
		for(int i=0;i<N;i++)
		{
			string t;
			cin>>t;
			names[i] = t;
			int M;
			cin>>M;
			for(int j=0;j<M;j++)
			{
				cin>>t;
				if(t[0]>='A' && t[0]<='Z')
				{
					rec[i].pb(t);
				}
			}
		}
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<rec[i].size();j++)
			{
				for(int k=0;k<N;k++)
				if(names[k]==rec[i][j])
				ids[i].pb(k);
			}
		}
			
		cout<<"Case #"<<ctr<<": "<<recu(0)<<"\n";
	}
	return 0;
}

