
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

int map[102][102];
int mark[102][102];
char ans[102][102];
vector<pair<int, int> > father[102][102];
pair<int, int> son[102][102];

int t, h, w;

pair<int, int> findmax()
{
	int i, j, max=0, maxi, maxj;
	for(i=1; i<=h; i++)
		for(j=1; j<=w; j++)
			if(!mark[i][j] && map[i][j]>max)
			{
				max = map[i][j];
				maxi=i; maxj=j;
			}
	return make_pair(maxi, maxj);
}

bool check()
{
	int i, j;
	for(i=1; i<=h; i++)
		for(j=1; j<=w; j++)
			if(!mark[i][j])
				return false;
	return true;
}

void go(int i, int j)
{
	if(mark[i][j])
		return;

	int max=0, tmp, maxi, maxj;
	tmp = map[i][j]-map[i-1][j];		//north
	if(tmp>0 && tmp>max) {
		max = tmp; maxi=i-1; maxj=j;
	}

	tmp = map[i][j]-map[i][j-1];		//west
	if(tmp>0 && tmp>max) {
		max = tmp; maxi=i; maxj=j-1;
	}

	tmp = map[i][j]-map[i][j+1];		//east
	if(tmp>0 && tmp>max) {
		max = tmp; maxi=i; maxj=j+1;
	}

	tmp = map[i][j]-map[i+1][j];		//south
	if(tmp>0 && tmp>max) {
		max = tmp; maxi=i+1; maxj=j;
	}

	mark[i][j] = 1;
	if(max!=0) {
		son[i][j] = make_pair(maxi, maxj);
		father[maxi][maxj].push_back(make_pair(i, j));		
		go(maxi, maxj);
	}

}

void signletter(int i, int j, int tmp)
{
	if(mark[i][j]==1)
		return;

	mark[i][j] = 1;
	ans[i][j] = tmp;
	int k;
	for(k=0; k<father[i][j].size(); k++)
	{
		signletter(father[i][j][k].first, father[i][j][k].second, tmp);
	}
	if(son[i][j].first==0 || son[i][j].second==0)
		return;
	signletter(son[i][j].first, son[i][j].second, tmp);

}

int main()
{
	
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);

	int i, j, k, tmp;
	pair<int, int> max;

	cin>>t;
	for(i=0; i<t; i++)
	{
		memset(map, 63, sizeof(map));
		memset(mark, 0, sizeof(mark));
		memset(son, 0, sizeof(son));
		cin>>h>>w;


		for(j=1; j<=h; j++) {
			for(k=1; k<=w; k++) {
				father[j][k].clear();
				cin>>map[j][k];
			}
		}

		while(true)
		{
			max = findmax();
			go(max.first, max.second);
			if(check())
				break;
		}

		memset(mark, 0, sizeof(mark));
		tmp = 'a';

		for(j=1; j<=h; j++) {
			for(k=1; k<=w; k++) {
				if(!mark[j][k]) {
					signletter(j, k, tmp);
					tmp++;
				}
			}
		}

		cout<<"Case #"<<i+1<<":"<<endl;
		for(j=1; j<=h; j++) {
			for(k=1; k<=w; k++) {
				cout<<ans[j][k];
				if(k!=w)
					cout<<" ";
			}			
			cout<<endl;
		}
	}
	


	return 0;
}