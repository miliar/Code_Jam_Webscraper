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
#include <cassert>
#include <cstring>
#include <queue>
#define vvi vector<vector<int> > 
#define pii pair<int,int>
#define vpii vector<vector<pair<int,int> > > 
#define mp(a,b) make_pair(a,b)
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define sz size()
#define pb push_back
#define all(x) x.begin(),x.end()
using namespace std;
char W[12][12];
int main()
{
	int tc;
	scanf("%d",&tc);
	int caseno=1;
	while(tc--){
		int r,c,d;
		scanf("%d%d%d",&r,&c,&d);
		for(int i=0;i<r;i++) scanf("%s",W[i]);
		int ret = 0;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				for(int k=3;i+k<=r && j+k<=c;k++){
					int ai = 0,bi =0 ,aj =0 ,bj = 0;
					for(int t=0;t<k;t++){
						for(int q=0;q<k;q++){
							if(t==0 && (q==0 || q==k-1)) continue;
							if(t==k-1 && (q==0 || q==k-1)) continue;
							ai += (2*t+1)*(d+W[i+t][j+q]-'0');
							bi += (d+W[i+t][j+q]-'0');
							aj += (2*q+1)*(d+W[i+t][j+q]-'0');
							bj += (d+W[i+t][j+q]-'0');
						}
					}
					if(ai%bi==0 && ai/bi == k && aj%bj==0 && aj/bj==k) ret=max(ret,k);
				}
			}
		}
		if(ret==0) printf("Case #%d: IMPOSSIBLE\n",caseno++);
		else printf("Case #%d: %d\n",caseno++,ret);
	}
	return 0;
}