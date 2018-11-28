#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>

using namespace std;


int p,q;
int qq[100];
int  was[1000];
int play()
{
	int i,j;
	for(i=1;i<=p;i++) was[i]=1;
	int ans=0;
	for(i=0;i<q;i++) 
	{
		was[qq[i]]=0;
		for(j=qq[i]-1;j>=1;j--) 
		{
			if(was[j]==0) break;
			ans++;
		}
		for(j=qq[i]+1;j<=p;j++) 
		{
			if(was[j]==0) break;
			ans++;
		}
	}
	return ans;
}
int mi;
int ft[100];
int val[100];
void dfs(int lv) 
{
	if(lv==q) 
	{
		int temp=play();
		if(temp<mi) mi=temp;
	}
	for(int i=0;i<q;i++) 
	{
		if(ft[i]) continue;
		qq[lv]=val[i];
		ft[i]=1;
		dfs(lv+1);
		ft[i]=0;
	}
}

int main()
{
	int i,j,k,ca,kk=1;
	freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%d",&ca);
	while(ca--) 
	{
		scanf("%d%d",&p,&q);
		for(i=0;i<q;i++) scanf("%d",&val[i]);
		mi=1<<29;
		dfs(0);
		printf("Case #%d: %d\n",kk++,mi);
	}
	return 0;
}