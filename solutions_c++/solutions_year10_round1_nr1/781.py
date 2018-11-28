#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
typedef unsigned long long ll;
using namespace std;

#define pb push_back
#define mp make_pair
#define sz size()
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<pii> > adjL;
int oo = (int) 1e9;

vector<vector<int > >vv,vis;

int ff(int i,int j,int n,int di,int dj)
{

	if(j>=vv.size() || j<0 || i >= vv.size() || i< 0 || vis[i][j] || vv[i][j]!=n )return 0;
	vis[i][j] = 1;
	int a = ff(i+di,j+dj,n,di,dj) + ff(i-di,j-dj,n,di,dj)+1;
	return a;
}
int main()
{
#ifndef ONLINE_JUDGE
freopen("a.txt", "rt", stdin);
freopen("b.txt", "wt", stdout);
#endif

	int t;scanf("%d",&t);
	for (int ii = 0; ii < t; ++ii) {
		cout<<"Case #"<<ii+1<<": ";
		int n,k;scanf("%d%d",&n,&k);
		vector<string >vs(n);
		for (int i = 0; i < n; ++i)
			cin>>vs[i];
		vv = vector<vector<int > >(n,vector<int>(n,0));
		for (int i = 0; i < n; ++i) {
			for (int j = n-1,cnt = n-1; j>=0; --j) {
				if(vs[i][j]=='R')
					vv[i][cnt--]=1;
				if(vs[i][j]=='B')
					vv[i][cnt--]=2;
			}
		}
//		for (int i = 0; i < n; ++i) {
//			for (int j = 0; j < n; ++j) {
//				cout<<vv[i][j]<<" ";
//			}
//			cout<<endl;
//		}
		int nr=0,nb=0;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				vis = vector<vector<int > >(n,vector<int >(n,0));
				if(vv[i][j]==1)
				{
					int h = ff(i,j,1,0,1);
					vis = vector<vector<int > >(n,vector<int >(n,0));
					int v = ff(i,j,1,1,0);
					vis = vector<vector<int > >(n,vector<int >(n,0));
					int d1 = ff(i,j,1,1,1);
					vis = vector<vector<int > >(n,vector<int >(n,0));
					int d2 = ff(i,j,1,1,-1);
					vis = vector<vector<int > >(n,vector<int >(n,0));
					nr = max(nr , max(h , max(v,max(d1,d2)) ) );

//					cout<<"d-> "<<d1<<" "<<d2<<endl;

				}
				if(vv[i][j] == 2)
				{
					int h = ff(i,j,2,0,1);
					vis = vector<vector<int > >(n,vector<int >(n,0));
					int v = ff(i,j,2,1,0);
					vis = vector<vector<int > >(n,vector<int >(n,0));
					int d1 = ff(i,j,2,1,1);
					vis = vector<vector<int > >(n,vector<int >(n,0));
					int d2 = ff(i,j,2,1,-1);
					vis = vector<vector<int > >(n,vector<int >(n,0));
					nb = max(nb , max(h , max(v,max(d1,d2)) ) );
//					cout<<i<<" "<<j<<"     "<<v<<" "<<h<<" "<<d1<<" "<<d2<<endl;
				}

			}
		}
//		cout<<nb<<" "<<nr<<endl;
		if(nb>= k && nr >= k)
			cout<<"Both\n";
		else if(nb >= k)
			cout<<"Blue\n";
		else if(nr>=k)
			cout<<"Red\n";
		else cout<<"Neither\n";
	}
	return 0;
}
