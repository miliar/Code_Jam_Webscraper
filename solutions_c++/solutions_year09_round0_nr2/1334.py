#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <cctype>
#include <algorithm>
#include <functional>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define fo(i,n) for(i=0;i<(n);++i)

typedef vector<int> vi ;
typedef vector<string> vs ;
typedef vector<double> vd ;
#define sz(x) ((int)(x).size())
#define all(x) x.begin(),x.end()
#define pb(x) push_back(x)
typedef long long ll;
const int MAXSTATS=110;
bool V[MAXSTATS][MAXSTATS];
int di[]={-1,0,0,1};
int dj[]={0,-1,1,0};

int l,w;
vector<vector<int> > b;
vector<vector<char> >res;
bool valid(int i,int j,int k)
{
	return di[k]+i<l&&di[k]+i>=0&&dj[k]+j<w&&dj[k]+j>=0;
}
char a;
bool FF(int i,int j)
{
	int mni = i,mnj = j;
	for(int k= 0 ; k <4 ; k++ )
	{
		if(valid(i,j,k))
			if(b[mni][mnj]>b[i+di[k]][j+dj[k]])
				mni = i+di[k],mnj=j+dj[k];
	}
	if(mni==i&&mnj==j)
		if(res[mni][mnj]=='-')
		{
			res[mni][mnj]=a;
			return true;
		}
		else
			return false;
	if(res[mni][mnj]!='-')
	{
		res[i][j]=res[mni][mnj];
		return false;
	}
	else
	{
		bool f = FF(mni,mnj);
		res[i][j]=res[mni][mnj];

		return f;
	}

}

int main()
{
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);


	int tt;
		cin>>tt;
		int t=0;
		while(tt--)
		{
			cin>>l>>w;
			b.clear();
			b.resize(l,vector<int>(w,0));
			res.clear();
			res.resize(l,vector<char>(w,'-'));
			for(int i = 0 ; i < l ; i++)
				for(int j = 0 ; j < w; j++)
					cin>>b[i][j];


			a = 'a';
			for(int i= 0 ; i < l ; i ++)
				for(int j = 0 ;  j < w; j++)
				{
					if(res[i][j]=='-')
						if(FF(i,j))a++;
				}
			cout<<"Case #"<<++t<<":\n";
			for(int i = 0 ; i< l ;i++)
			{
				for(int j = 0 ; j < w ; j++)
				{
					if(j)cout<<" ";
					cout<<res[i][j];
				}
				cout<<endl;
			}

		}
	return 0;
}
