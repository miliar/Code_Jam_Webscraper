#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
#define MAXN 1005
struct Node{
public:
	int id;
	int value;
	bool operator<(Node a)const{
		return value<a.value;
	}
};
Node node[MAXN];
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int T, x, n;
	scanf("%d",&T);
	for(int t = 1; t <= T; t++){
		scanf("%d",&n);
		for(int i = 0; i < n; i++){
			scanf("%d",&x);
			node[i].value = x;
			node[i].id = i;
		}
		sort(node,node+n);
		int ans = 0;
		for(int i = 0; i < n; i++){
			if(node[i].id != i)
				ans++;
		}
		printf("Case #%d: %d.000000\n", t, ans);
	}
	return 0;
}
