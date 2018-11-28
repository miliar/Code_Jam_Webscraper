#pragma warning(disable:4786)
#include<math.h>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<utility>
#include<algorithm>
#include<string.h>
#include<stdio.h>
#include<set>
#include<stdlib.h>
#include<sstream>
#include<functional>
#include<queue>
#include<stack>
using namespace std;

#define MAX(A,B) ((A)>(B)?(A):(B))
#define MIN(A,B) ((A)<(B)?(A):(B))
#define ABS(A) ((A)>0?(A):(-(A)))
#define S(X) ((X)*(X))

typedef pair<int,int> PII;
typedef __int64 LL;

int dr[]={-1,0,1,0};
int dc[]={0,1,0,-1};
//int dr[]={-2,-2,-1,1,2,2,1,-1};
//int dc[]={-1,1,2,2,1,-1,-2,-2};

map<vector<PII>,int> M;
char board[20][20];
vector<PII> A,B,Z,X;
int r,c,fault,t;

int OK(int x,int y)
{
	if(x<0 || x>=r || y<0 || y>=c) return 0;
	if(board[x][y]=='#') return 0;
	for(int i =0;i<t;i++) if(PII(x,y)==Z[i]) return 0;

	return 1;
}

int connected()
{
	int i,vis[10],s;
	queue<int> Qs;
	Qs.push(0);

	for(i=0;i<t;i++) vis[i]=0;

	for(i=1;i<t;i++) if(Z[i]==Z[i-1]) return 0;

	vis[0]=1;
	while(!Qs.empty())
	{
		s=Qs.front();
		Qs.pop();

		for(i=0;i<t;i++) if(!vis[i] && ABS(Z[s].first-Z[i].first)+ABS(Z[s].second - Z[i].second)==1)
		{
			vis[i]=1;
			Qs.push(i);
		}
	}

	for(i=0;i<t;i++) if(!vis[i]) return 0;
	return 1;
}

int MOVE(int n, int d,int y)
{
	Z = X;

//	for(int i=0;i<Z.size();i++) printf(">>%d %d	\n",Z[i].first,Z[i].second);

	if(!( OK(Z[n].first+dr[d],Z[n].second+dc[d]) && OK(Z[n].first-dr[d],Z[n].second-dc[d]) ) ) return 0;

	Z[n].first+=dr[d];
	Z[n].second+=dc[d];
	sort(Z.begin(),Z.end());

	if(!connected())
	{
		fault=1;
		if(y==1) return 0;
		if(y==0) return 1;
	}
	else
	{
		fault=0;
		return 1;
	}

	return 1;
}

queue<int> Q1,Q2;
queue<vector<PII> > Q;

int main()
{
//	freopen("A-small-attempt0.in","r",stdin); freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin); freopen("A-small-attempt1.out","w",stdout);
	freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);

	int T,ks,i,j,flag,d,ans,y;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		scanf("%d%d",&r,&c);
		for(i=0;i<r;i++) scanf("%s",board[i]);

		A.clear();
		B.clear();
		M.clear();

		Q=queue<vector<PII> > ();
		Q1=queue<int> ();
		Q2=queue<int> ();

		for(i=0;i<r;i++) for(j=0;j<c;j++)
		{
			if(board[i][j]=='o' || board[i][j]=='w') {A.push_back( PII(i,j) );}
			if(board[i][j]=='x' || board[i][j]=='w') {B.push_back( PII(i,j) );}

			if(board[i][j]!='#') board[i][j]='.';
		}

		sort(A.begin(),A.end());
		sort(B.begin(),B.end());

		if(A==B) {printf("Case #%d: 0\n",ks); continue;}

		Q.push(A);
		Q1.push(0);
		Q2.push(0);

		M[A]=0;
		flag=0;

		t=A.size();

		while(!Q.empty())
		{
			d=Q1.front(); Q1.pop();
			y = Q2.front(); Q2.pop();
			X = Q.front(); Q.pop();

			for(i=0;i<t;i++)
				for(j=0;j<4;j++)
					if( MOVE(i,j,y) )
					{
						if(M.find(Z) != M.end()) continue;
						if(Z == B) {ans=d+1; flag=1; goto end;}

						Q.push(Z);
						Q1.push(d+1);
						Q2.push(fault);
						M[Z]=1;
					}
		}
end:
		if(!flag) printf("Case #%d: %d\n",ks,-1);
		else printf("Case #%d: %d\n",ks,ans);

	}

	return 0;
}