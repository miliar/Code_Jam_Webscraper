#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<bitset>
#include<cstring>
#include<climits>
#include<deque>
#include<utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>

using namespace std;

#define rep(i,n) for(int  i=0;i<(int)(n);++i)
long double ZERO=0;
const long double INF=1/ZERO,EPSILON=1e-12;
#define all(c) (c).begin(),(c).end() 
#define rep2(i,a,b) for(int i=(a);i<=((int)b);++i)
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define sz(v) ((int)((v).size()))
bool FindPath(vector<vector<int> > &canMatch,vector<int> &left,vector<int> &right,vector<bool>& visited,int i)
{

	foreach(j,canMatch[i])
	{
		if(visited[*j])
			continue;
		visited[*j]=1;
		if(right[*j]==-1 || FindPath(canMatch,left,right,visited,right[*j]))
		{
			left[i]=*j;
			right[*j]=i;
			return true;
		}
	}
return false;
}

int maxMatch(vector<vector<int> > &canMatch,int matchingtoSize,vector<int> &left,vector<int> &right)
{
	left.clear();
	right.clear();
	left.resize(canMatch.size(),-1);
	right.resize(matchingtoSize,-1);
	int sol=0;
	rep(i,canMatch.size())
	{
		vector<bool> visited(matchingtoSize);
		if(left[i]==-1)
		{
			if(FindPath(canMatch,left,right,visited,i))
				sol++;
		}
	}
	return sol;
}

int maxMatch(vector<vector<int> > &canMatch,int matchingtoSize)
{
	vector<int> left,right;
	return maxMatch(canMatch,matchingtoSize,left,right);
}

int main() {
	freopen("B-large.in","rt",stdin);
	freopen("B-small.txt","wt",stdout);
	int T;
	cin>>T;
	rep(t,T)
	{
		int tat;
		cin>>tat;
		int na,nb;
		cin>>na>>nb;
		vector<pair<int,int> > a,b;
		char c;
		rep(i,na)
		{
			int ha,ma,hd,md;
			cin>>ha>>c>>ma>>hd>>c>>md;
			ma+=ha*60;
			md+=hd*60;
			a.push_back(make_pair(ma,md));
		}
		rep(i,nb)
		{
			int ha,ma,hd,md;
			cin>>ha>>c>>ma>>hd>>c>>md;
			ma+=ha*60;
			md+=hd*60;
			b.push_back(make_pair(ma,md));
		}
		vector<vector<int> > adj(na+nb);
		rep(i,na)
		{
			rep(j,nb)
			{
				if(a[i].second+tat<=b[j].first)
				{
					adj[i].push_back(j+na);
				//	cerr<<i<<" "<<j+na<<endl;
				}
				
				if(b[j].second+tat<=a[i].first)
				{
					adj[j+na].push_back(i);
					//cerr<<j+na<<" "<<i<<endl;
				}
			}
		}
		vector<int> left;
		vector<int> right;
		maxMatch(adj,na+nb,left,right);
		int ra=0,rb=0;
		rep(i,sz(right))
		{
			if(right[i]==-1)
				i<na?ra++:rb++;
		}
		printf("Case #%d: %d %d\n",t+1,ra,rb);
	}
	return 0;
}
