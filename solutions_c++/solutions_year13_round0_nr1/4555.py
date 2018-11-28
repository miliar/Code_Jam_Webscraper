#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<cstdio>
#include<cassert>
#include<iostream>
#include<queue>
#include<map>
#include<set>
#include<vector>
#include<ctime>

using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b)  ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))

#define MP make_pair
#define pb push_back
#define inf  1000000000
#define maxn 100001
#define maxc 100001
#define MP make_pair

//typedef long long LL;
typedef pair<int,int> pi;
typedef pair<pi,pi> pii;
typedef __int64 LL;

vector<int> box[25],res;
int cnt[202];
int need[25],n;
int memo[1<<20];


int solve(int mask)
{
	int ret=0,i,j;

	if(mask+1==(1<<n)) return 1;
	if(memo[mask]!=-1) return memo[mask];


	for(i=0;i<n;i++)
	{
		 if(mask&(1<<i)) continue;
		 if(cnt[need[i]]==0) continue;

		 --cnt[need[i]];
		 for(j=0;j<box[i].size();j++) cnt[box[i][j]]++;

		 int q=solve(mask|(1<<i));

		 if(q)
		 {
			 ret=1;
			 res.pb(i+1);
			 break;
		 }

		 ++cnt[need[i]];
		 for(j=0;j<box[i].size();j++) cnt[box[i][j]]--;
	}

	return memo[mask]=ret;
}


char grid[5][5];

int main()
{
	int i,j,k,tests,cs=0,K;
	string s;
	

	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%d",&tests);

	while(tests--)
	{	
		for(i=0;i<4;i++) scanf("%s",grid[i]);

		int X=0,O=0,cnt=0;

		int tx1=0,to1=0,tt1=0; 
		int tx2=0,to2=0,tt2=0;

		for(i=0;i<4;i++)
		{
			int tx=0,to=0,tt=0;
			for(j=0;j<4;j++)
			{
				if(grid[i][j]=='X') tx++;
				if(grid[i][j]=='O') to++;
				if(grid[i][j]=='T') tt++;

				if(grid[i][j]!='.') cnt++;

				if(i==j)
				{
					if(grid[i][j]=='X') tx1++;
					if(grid[i][j]=='O') to1++;
					if(grid[i][j]=='T') tt1++;
				}

				if(i==3-j)
				{
					if(grid[i][j]=='X') tx2++;
					if(grid[i][j]=='O') to2++;
					if(grid[i][j]=='T') tt2++;
				}
			}

			if(tx==4 || tx+tt==4) X=1;
			if(to==4 || to+tt==4) O=1;

			tx=0,to=0,tt=0;
			for(j=0;j<4;j++)
			{
				if(grid[j][i]=='X') tx++;
				if(grid[j][i]=='O') to++;
				if(grid[j][i]=='T') tt++;


			}
			
			if(tx==4 || tx+tt==4) X=1;
			if(to==4 || to+tt==4) O=1;
		}

		if(tx1==4 || tx1+tt1==4) X=1;
		if(to1==4 || to1+tt1==4) O=1;
		
		if(tx2==4 || tx2+tt2==4) X=1;
		if(to2==4 || to2+tt2==4) O=1;

		int D=0;

		if(!X && !O && cnt==16) D=1;

		printf("Case #%d: ",++cs);
		if(X)
			puts("X won");
		else if(O)
			puts("O won");
		else if(D)
			puts("Draw");
		else
			puts("Game has not completed");


	
	}

	return 0;
} 
