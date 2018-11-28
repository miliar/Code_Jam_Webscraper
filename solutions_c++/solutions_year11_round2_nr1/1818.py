#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <string>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;
typedef unsigned long long uint64;
typedef long long int64;
#define eps 1e-9
#define pi 3.1415926535897932384626433832795
#define MAX 105

int N;
vector<string> Map;
int cnt[MAX],win[MAX],lose[MAX];
double wp[MAX],owp[MAX],oowp[MAX];
vector<int> op[MAX];

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("A-large.in","r",stdin);
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int T,testcase=1;;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: \n",testcase++);
		scanf("%d",&N);
		string str;
		memset(cnt,0,sizeof(cnt));
		memset(win,0,sizeof(win));
		memset(lose,0,sizeof(lose));
		for(int i=0;i<N;i++)wp[i]=0.0;
		for(int i=0;i<N;i++)owp[i]=0.0;
		for(int i=0;i<N;i++)oowp[i]=0.0;
		Map.clear();
		for(int i=0;i<N;i++)
		{
			cin>>str;
			Map.push_back(str);
			op[i].clear();
		}
		//memset(cnt,0,sizeof(cnt));
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				if(i==j)continue;
				switch (Map[i][j])
				{
				case '1':
					cnt[i]++;
					win[i]++;
					op[i].push_back(j);
					break;
				case '0':
					cnt[i]++;
					lose[i]++;
					op[i].push_back(j);
					break;
				}
			}
		}
		for(int i=0;i<N;i++)
		{
			wp[i]=win[i]*(1.0)/(double)cnt[i];
		}
		double rpi=0.0,tmp=0.0;
		double ss=0,aa=0;
		for(int i=0;i<N;i++)
		{
			int sz=op[i].size();
			//rpi=0.25*wp[i];
			tmp=0.0;
			ss=0.0,aa=0;
			for(int j=0;j<sz;j++)
			{
				//if(op[i][j]==i)continue;
				if(cnt[op[i][j]]==1)continue;
				if(Map[i][op[i][j]]=='0')ss=ss+(win[op[i][j]]-1)*(1.0)/(double)(cnt[op[i][j]]-1);
				else ss=ss+(win[op[i][j]])*(1.0)/(double)(cnt[op[i][j]]-1);
				//aa=aa+(cnt[op[i][j]]-1);
			}
			owp[i]=ss*(1.0)/(double)cnt[i];
		}
		for(int i=0;i<N;i++)
		{
			tmp=0.0;
			int sz=op[i].size();
			for(int j=0;j<sz;j++)
			{
				//if(op[i][j]==i)continue;
				tmp+=owp[op[i][j]];
			}
			oowp[i]=tmp/cnt[i];
		}
		double ans;
		for(int i=0;i<N;i++)
		{
			ans=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
			printf("%.9lf\n",ans);
		}

	}
	return 0;
}