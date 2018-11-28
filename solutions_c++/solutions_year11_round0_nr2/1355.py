#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <complex>
#include <climits>
#include <queue>
#include <ctime>

using namespace std;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)

int n,ncom,nop;
int com[101][101],opp[101][101];
char a[1001];

int main()
{
	freopen("b.txt","rt",stdin);
	freopen("b.out","wt",stdout);
	int t;
	scanf("%d",&t);
	rep(tt,0,t)
	{
		memset(com,-1,sizeof(com));
		memset(opp,0,sizeof(opp));
		scanf("%d ",&ncom);
		rep(i,0,ncom){
			scanf("%s",a);
			com[a[0]-'A'][a[1]-'A']=com[a[1]-'A'][a[0]-'A']=a[2]-'A';
		}
		scanf("%d ",&nop);
		rep(i,0,nop)
		{
			scanf("%s",a);
			opp[a[0]-'A'][a[1]-'A']=opp[a[1]-'A'][a[0]-'A']=1;
		}
		scanf("%d ",&n);
		scanf("%s",a);
		vector<int>v;
		int nn = strlen(a);
		rep(i,0,nn)
		{
			v.PB(a[i]-'A');
			while(v.size()>=2){
				if(com[v[v.size()-1]][v[v.size()-2]]!=-1){
					int x = v[v.size()-1];
					int y = v[v.size()-2];
					v.pop_back();
					v.pop_back();
					v.PB(com[x][y]);
				}
				else
					break;
			}
			rep(j,0,v.size())
				if(opp[v[j]][v.back()])
				{
					v.clear();
					break;
				}
		}
		printf("Case #%d: ",tt+1);
		printf("[");
		rep(i,0,v.size())
		{
			printf("%c",v[i]+'A');
			if(i!=(int)v.size()-1)
				printf(", ");
		}
		printf("]\n");
	}

	return 0;
}
