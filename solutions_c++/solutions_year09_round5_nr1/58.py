#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>

using namespace std;

const long long MOD=145;
char board[15][15];
char s[15][15];

vector<pair<long long,bool>>next[10000];
set<pair<long long,bool>>used;
long long res;
int n,m;

const int di[4]={-1,0,1,0};
const int dj[4]={0,1,0,-1};

long long pos(vector<pair<int,int> >c)
{
	long long r=0;
	long long M=1;
	sort(c.begin(),c.end());
	for(int i=0;i<c.size();i++)
	{
		r+=(c[i].first*m+c[i].second)*M;
		M*=MOD;
	}
	return r;
}

bool inside(int i,int j) { return i>=0 && j>=0 && i<n && j<m; }

bool connected(vector<pair<int,int>>&c)
{
	bool u[5]={0};
	int i,j,k,l=c.size(),n=1;
	u[0]=1;
	for(i=0;i<l&&n<l;i++)
		for(j=0;j<l;j++)
			for(k=0;k<l;k++)
				if (u[j] && !u[k])
					if (abs(c[j].first-c[k].first)+abs(c[j].second-c[k].second)==1) 
					{
						u[k]=true;
						++n;
					}
	return n==l;
}

void move(pair<long long,bool> Cur,vector<pair<long long,bool>>&next)
{
	int i,j,k;
	for(i=0;i<n;i++)
		for(j=0;j<m;j++) s[i][j]=board[i][j];
	
	long long cur=Cur.first;
	bool CON=Cur.second;
	vector<pair<int,int>>c;
	while(cur)
	{
		k=cur%MOD;
		c.push_back(make_pair(k/m,k%m));
		s[k/m][k%m]='x';
		cur/=MOD;
	}


	pair<long long,bool> x;
	int l=c.size(),ii,jj;
	while(l--)
	{
		i=c[l].first;
		j=c[l].second;
		for(k=0;k<4;k++)
		{
			ii=i+di[k];
			jj=j+dj[k];
			if (!inside(ii,jj)) continue;
			if (s[ii][jj]!='.') continue;
			ii=i-di[k];
			jj=j-dj[k];
			if (!inside(ii,jj)) continue;
			if (s[ii][jj]!='.') continue;
			c[l]=make_pair(ii,jj);
			bool con=connected(c);
			if (!con && !CON) continue;
			x=make_pair(pos(c),con);
			if (used.find(x)==used.end())
			{
				used.insert(x);
				next.push_back(x);
			}
		}
		c[l]=make_pair(i,j);
	}

}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t,T;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		int i,j;
		scanf("%d%d",&n,&m);
		gets(board[0]);
		for(i=0;i<n;i++) gets(board[i]);

		next[0].clear();
		used.clear();
		res=0;
		long long cur=0;
		long long M1=1,M2=1;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				if (board[i][j]=='x' || board[i][j]=='w') 
				{
					res+=M1*(i*m+j);
					M1*=MOD;
				}
				if (board[i][j]=='o' || board[i][j]=='w')
				{
					cur+=M2*(i*m+j);
					M2*=MOD;
				}
				if (board[i][j]!='#') board[i][j]='.';
			}

		pair<long long,bool>Res=make_pair(res,true),Cur=make_pair(cur,true);

		printf("Case #%d: ",t);
		if (Res==Cur)
		{
			puts("0");
			continue;
		}

		next[0].push_back(Cur);
		used.insert(Cur);
		for(i=0;!next[i].empty();i++)
		{
			next[i+1].clear();
			for(j=0;j<next[i].size();j++)
			{
				move(next[i][j],next[i+1]);
				if (used.find(Res)!=used.end()) break;
			}
			if (j<next[i].size()) break;
		}

		if (next[i].empty()) puts("-1"); else printf("%d\n",i+1);
		
	}

	return 0;
}