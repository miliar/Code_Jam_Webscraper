#include <vector>
#include <list>
#include <map>
#include <set>
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
#include<math.h>
using namespace std;
const int maxn = 1000;
int T,M,N;
int c[maxn][maxn],tc[maxn][maxn];
bool solve(int x,int y,int s)
{
	int i,j,k;
	bool yes=false;
	int f=0,t=0;
	if(c[x][y]==0)f=0;
	else f=1;
	for(i=x;i<x+s;i++)
	{
		t=f;
		for(j=y;j<y+s;j++)
		{
			if(c[i][j]!=t )return false;
			t=1-t;
		}
		f=1-f;
	}
	for(i=x;i<x+s;i++)
		for(j=y;j<y+s;j++)c[i][j]=-1;
	return true;
}

bool isyes(int x,int y,int s)
{
	int i,j,k;
	bool yes=false;
	int f=0,t=0;
	if(c[x][y]==0)f=0;
	else f=1;
	for(i=x;i<x+s;i++)
	{
		t=f;
		for(j=y;j<y+s;j++)
		{
			if( c[i][j] !=t )return false;
			t=1-t;            
		}
		f=1-f;
	}
	return true;
}

int main()
{
	//freopen("A-small-attempt0.in","r",stdin); freopen("A-small-attempt0.out","w",stdout);
	//freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	//freopen("B-small-attempt0.in","r",stdin); freopen("B-small-attempt0.out","w",stdout);
	//freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	freopen("C-small-attempt0.in","r",stdin); freopen("C-small-attempt0.out","w",stdout);
	//freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int cases;
	scanf("%d",&cases);
	int i,j,k;
	char str[1000];
	for(int cas=1;cas<=cases;cas++)
	{
		scanf("%d%d",&M,&N);
		memset(c,0,sizeof(c));
		for(i=0;i<M;i++)
		{
			cin>>str;
			for(j=0;j<N/4;j++)
			{
				int tmp;
				if(isdigit(str[j]))tmp = str[j]-'0';
				else tmp = str[j]-'A' + 10;
				for(k=0;k<4;k++)
				{
					c[i][j*4+(3-k)]=tmp%2;
					tmp/=2;
				}
			}
		}
		vector< pair<int,int> >ans;
		memcpy(tc,c,sizeof(c));
		for(k=2;k<=min(M,N);k++)
		{
			bool yes = false;
			for(i=0;i<M-k+1 && !yes ;i++)
				for(j=0;j<N-k+1 && !yes;j++)
				{
					if(isyes(i,j,k))                        
						yes=true;
				}
				if(!yes)break;
		}

		for(k--;k>=1;k--)
		{
			bool yes = false;
			for(i=0;i<M-k+1;i++)
				for(j=0;j<N-k+1;)
				{
					if( solve(i,j,k) )
					{
						if(!yes)ans.push_back( make_pair(k,1) );
						else ans[ ans.size() - 1 ].second ++;
						yes=true;
						j+=k;
					}
					else j++;
				}
		}
		printf("Case #%d: %d\n",cas,ans.size());
		for(i=0;i<ans.size();i++)
			cout<<ans[i].first<<" "<<ans[i].second<<endl;
	}
}

