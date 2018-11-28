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
int ar[1010];
int main()
{
	int tc;
	scanf("%d",&tc);
	int caseno=1;
	while(tc--){
		int n;
		scanf("%d",&n);
		int txor=0;
		int tsum=0;
		for(int i=0;i<n;i++){scanf("%d",ar+i);txor^=ar[i];tsum+=ar[i];}
		int ret=-1;
		for(int i=n-1;i>=0;i--){
			if(ar[i]==(ar[i]^txor)){
				ret=max(ret,max(ar[i],tsum-ar[i]));
			}
		}
		if(ret==-1) printf("Case #%d: NO\n",caseno++);
		else printf("Case #%d: %d\n",caseno++,ret);
	}
	return 0;
}