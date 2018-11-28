#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <utility>
#include <stack>
#include <queue>
#include <map>

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define pi 2*acos(0.0)
#define eps 1e-9
#define PII pair<int,int> 
#define PDD pair<double,double>
#define LL long long
#define INF 1000000000

using namespace std;

double WP[110],OWP[110],OOWP[110];
int win[110],cnt[110];
int T,N,x,y,z;
char board[150][150];

int main()
{
	scanf("%d",&T);
	for(z=1;z<=T;z++)
	{
		scanf("%d",&N);getchar();
		for(x=1;x<=N;x++)
		{
			for(y=1;y<=N;y++) scanf("%c",&board[x][y]);
			getchar();
		}
		
		//hitung WP
		for(x=1;x<=N;x++)
		{
			win[x]=cnt[x]=0;
			for(y=1;y<=N;y++) if(board[x][y]!='.')
			{
				cnt[x]++;
				if(board[x][y]=='1') win[x]++;
			}
			WP[x]=win[x]/(double) cnt[x];
		}
		
		//hitung OWP
		for(x=1;x<=N;x++)
		{
			int hit=0;
			double temp=0;
			for(y=1;y<=N;y++) if(board[x][y]!='.')
			{
				hit++;
				if(board[x][y]=='0') temp+=(win[y]-1)/(double)(cnt[y]-1);
					else temp+=(win[y])/(double)(cnt[y]-1);
			}
			OWP[x]=temp/(double)hit;
		}
		
		//hitung OOWP
		for(x=1;x<=N;x++)
		{
			int hit=0;
			double temp=0;
			for(y=1;y<=N;y++) if(board[x][y]!='.')
			{
				hit++;
				temp+=OWP[y];
			}
			OOWP[x]=temp/(double)hit;
		}
		
		printf("Case #%d:\n",z);
		for(x=1;x<=N;x++) cout << 0.25*(WP[x]+OOWP[x])+0.5*OWP[x] << endl;
	}
	return 0;
}

