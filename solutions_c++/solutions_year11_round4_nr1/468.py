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
map<int,int> me;
int main()
{
	int m,n,t,s,r,x,i,j,bi,ei,wi;cin>>n;
	for(i=0;i<n;i++){
		scanf("%d %d %d %d %d",&x,&s,&r,&t,&m);
		double ret=0.0,las=t+0.0;me.clear();
		for(j=0;j<m;j++){
			scanf("%d %d %d",&bi,&ei,&wi);me[wi]+=(ei-bi);x-=(ei-bi);
		}
		me[0]+=x;
		map<int,int>::iterator it=me.begin();
		while(it!=me.end()){
			double y=(*it).first*1.0,z=(*it).second*1.0,w=z/(r+y);
			if(w>las){
				ret+=las+(z-las*(r+y))/(s+y);las=0;
			}
			else{
				ret+=w;las-=w;
			}
			it++;
		}
		printf("Case #%d: %.12f\n",i+1,ret);
	}
	return 0;
}
