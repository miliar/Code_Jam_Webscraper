#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <cctype>

#define mp make_pair
#define pb push_back
#define all(v) (v).begin(),(v).end()
#define sz(v) ((int)(v.size()))

using namespace std;

typedef long long int64;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<string> vs;

const int inf=100000000;

template<class T> T abs(T x){return x>0 ? x:(-x);}
template<class T> T sqr(T x){return x*x;}

int k;
string s;
int cost[100][100];
int b[100][100];
int st;
int d[16][1<<16];

int get(int x,int mask)
{
	if(mask==(1<<k)-1)
	{
		return b[st][x];
	}
	int& res=d[x][mask];
	if(res!=-1) return res;
	res=inf;
	for(int i=0;i<k;i++){
		if((mask>>i)&1)
			continue;
		res=min(res,get(i,mask^(1<<i))+cost[x][i]);
	}
	return res;
}

int main()
{
	int tc;
	cin >> tc;
	for(int ic=0;ic<tc;ic++)
	{
		printf("Case #%d: ",ic+1);		
		cin >> k >> s;		
		memset(cost,0,sizeof(cost));
		memset(b,0,sizeof(b));
		for(int i=0;i<k;i++)
			for(int j=0;j<k;j++)
			{
				if(i==j)
				{
					cost[i][j]=inf;
					b[i][j]=inf;
					continue;
				}
				cost[i][j]=0;
				b[i][j]=0;
				for(int t=0;t<sz(s);t+=k)
				{
					if(s[t+i]!=s[t+j]) cost[i][j]++;
					if(t+k<sz(s))
					{
						if(s[t+j]!=s[t+k+i])
							b[i][j]++;
					}
				}
			}
		int res;
		res=inf;
		for(int i=0;i<k;i++)
		{
			st=i;
			memset(d,-1,sizeof(d));
			int cur=get(i,1<<i);
/*			if(i==3)
				cerr << cur << "\n";*/
			res=min(res,cur);
		}
		res++;
		cout << res;
		printf("\n");
	}
	return 0;
}
