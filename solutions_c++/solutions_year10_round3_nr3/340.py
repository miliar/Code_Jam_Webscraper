#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef pair<int,int> pii;
typedef long long ll;
const int maxn = 512+5;

int r;
int cb[maxn][maxn];
int cs[maxn+1];
char buf[maxn];
int M,N;
void init()
{
}

int solve()
{
	memset(cs,0,sizeof cs);
	r = 0;
	
	while(1)
	{
		
		int maxs = 0;
		int posx = -1;
		int posy = -1;
		for(int i = 0;i<M;i++)
		{
			for(int j = 0;j<N;j++)
			{
				int v = cb[i][j];
				if(v == '#')
					continue;
				for(int s = 2;s<=M && s<=N;s++)
				{
						
					int x,y;
					for(x = i;x<s+i && x<M;x++)
					{
						int find = 0;
						for(y = j;y<s+j && y<N;y++)
						{
							if(x == i && y ==j)
								continue;
							if(cb[x][y] == '#'){find = 1;break;}
							if(x > i && y == j)
							{
							 if(cb[x][y] != !cb[x-1][y]){find = 1;break;}
							 
							}
							if(x == i && y>j)
							{
								if(cb[x][y] != !cb[x][y-1]){find = 1;break;}
							}
							if(x > i && y >j)
							{
								if(cb[x][y] != !cb[x][y-1]){find = 1;break;}
								if(cb[x][y] != !cb[x-1][y]){find = 1;break;}
							}
						}
						if(find == 1)break;
					}
					if(x == s+i && y == s+j)
					{
						if(s > maxs)
						{
							maxs = s;
							posx = i;
							posy = j;
						}
					}
					else
					{
						break;
					}
				}
			}
			
		}
		if(maxs >=2)
		{
			cs[maxs]++;
			for(int i=posx;i< posx+maxs && i<M;i++)
			{
				for(int j = posy;j < posy+maxs && j<N;j++)
				{
					cb[i][j] = '#';
				}
			}
		}
		else
		{
			for(int i=0;i<M;i++)
				for(int j=0;j<N;j++)
					if(cb[i][j] != '#')cs[1]++;
			break;
		}
		
	}
	
	for(int i = (M<N)?M:N;i>=1;i--)
		if(cs[i] > 0)r++;
	return r;
}

int main()
{
//	freopen("c-test.in","r",stdin);//freopen("c-test.out","w",stdout);
	freopen("c-small-attempt0.in","r",stdin);freopen("c-small.out","w",stdout);
//	freopen("c-large.in","r",stdin);freopen("c-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		cin>>M>>N;
		gets(buf);
		for(int i=0;i<M;i++)
		{
			gets(buf);
			for(int j=0;j< N/4;j++)
			{
				int value;
				if(buf[j] >= '0' && buf[j] <= '9')
				{
					value = buf[j] - '0';
				}
				if(buf[j] >= 'A' && buf[j] <= 'F')
				{
					value = buf[j] - 'A'+10;
				}
				cb[i][j*4+0] = value/8;
				cb[i][j*4+1] = (value/4)%2;
				cb[i][j*4+2] = (value/2)%2;
				cb[i][j*4+3] = value%2;
			}
		}

		solve();
	
		cout<<"Case #"<<caseId<<": "<<r<<endl;
		for(int i = (M<N)?M:N;i>=1;i--)
		{
			if(cs[i] >0)
				cout<<i<<" "<<cs[i]<<endl;
		}
		cerr<<caseId<<"/"<<testcase<<endl;
	}
	return 0;
}