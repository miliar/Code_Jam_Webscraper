#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<climits>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<deque>
#include<set>
#include<map>
using namespace std;

#define N 11000

int n,d;
int p[N],len[N];
int flag[N],pos;
int aaa;
int bbb;
int i,id;
int T;

inline int min(int x,int y){ return (x<y)?x:y; }


int main(){
	
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);scanf("%d",&T);
	for( id=1;id<=T;id++)
	{
		printf("Case #%d: ",id);
		scanf("%d",&n);
		for( i=0;i<n;i++)
			scanf("%d%d",&p[i],&len[i]);
		scanf("%d",&p[n]);
		for (i=0;i<N;i++)flag[i]=0;
		pos=1;
		bbb=min(p[0],len[0])+p[0];
		while(pos<=n && p[pos]<=bbb)
			flag[pos++]=p[0];
		for( i=1;i<n;i++)
		{
			if(flag[i]==0)
				continue;
			aaa=min(p[i]-flag[i],len[i])+p[i];

			while(pos<=n && p[pos]<=aaa)
				flag[pos++]=p[i];
		}
		if(flag[n])
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
