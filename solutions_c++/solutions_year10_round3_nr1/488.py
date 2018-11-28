#include <iostream>
#include <string.h>
using namespace std;

struct Node{
	int a,b;
}node[2000];

int main(void)
{
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int T;
	cin>>T;
	for(int W=1;W<=T;W++)
	{
		memset(node,0,sizeof(node));
		int n,sum=0;
		scanf("%d",&n);
		for(int i=1;i<=n;i++) scanf("%d%d",&(node[i].a),&(node[i].b));
		for(int i=1;i<n;i++)
			for(int j=i+1;j<=n;j++)
			{
				if(((node[i].a-node[j].a)*(node[i].b-node[j].b)<0) && node[i].a-node[i].b!=node[j].a-node[j].b) sum++;
			}
		printf("Case #%d: %d\n",W,sum);
	}
	return 0;
}