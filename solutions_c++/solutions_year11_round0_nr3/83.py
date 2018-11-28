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
int main()
{
	int i,j,n,t,a;cin>>n;
	for(i=0;i<n;i++){
		scanf("%d",&t);int ret=0,mi=10000000,s=0;
		for(j=0;j<t;j++){
			scanf("%d",&a);mi=min(mi,a);ret+=a;s^=a;
		}
		if(s>0) printf("Case #%d: NO\n",i+1);
		else printf("Case #%d: %d\n",i+1,ret-mi);
	}
	return 0;
}
