#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<deque>
using namespace std;
#define pb push_back
typedef long long lint;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
bool sumi[1100];int ka[1100];int re;
void dfs(int a){
	if(sumi[a]) return;re++;sumi[a]=true;dfs(ka[a]);return;
}
int main()
{
	int i,j,n,t,ret;cin>>t;
	for(i=0;i<t;i++){
		cin>>n;ret=0;memset(sumi,false,sizeof(sumi));
		for(j=0;j<n;j++) scanf("%d",&ka[j+1]);
		for(j=1;j<=n;j++){
			if(!sumi[j]){
				re=0;dfs(j);if(re>1) ret+=re;//cout<<j<<' '<<re<<endl;
			}
		}
		printf("Case #%d: %d.000000\n",i+1,ret);
	}
	return 0;
}
