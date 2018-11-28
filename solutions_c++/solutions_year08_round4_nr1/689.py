#include <stdio.h>
#include <algorithm>

#define MAXN 10000
#define INF 1000000000

//#define DEBUG

using namespace std;

class Node{
	public:
		Node():zero(INF), one(INF){}
	int type, changeable;
	int zero, one;
};

Node node[MAXN];

inline int min(int a, int b){ return (a<b) ? a : b; }

int main()
{
	int icase, ncase;
	int i, n, V, t;
	int ans;
	Node left, right;
	
	scanf("%d", &ncase);
	for(icase=0; icase<ncase; ++icase){
		scanf("%d%d", &n, &V);
		for(i=0; i<(n-1)/2; ++i){
			scanf("%d%d", &node[i].type, &node[i].changeable);
			node[i].zero = node[i].one = INF;
		}
		for(;i<n; ++i){
			scanf("%d", &t);
			if(t){
				node[i].one = 0;
				node[i].zero = INF;
			}
			else{
				node[i].one = INF;
				node[i].zero = 0;
			}
		}
		for(i=(n-1)/2-1; i>=0; --i){
			left = node[i*2+1];
			right = node[i*2+2];
			if(node[i].type == 1){ // AND
				node[i].one = min(node[i].one, left.one + right.one);
				node[i].zero = min(node[i].zero, min(left.zero + right.zero, min(left.one + right.zero, left.zero + right.one)));
			}
			else{ // OR
				node[i].one = min(node[i].one, min(left.one+right.one, min(left.one+right.zero, left.zero +right.one)));
				node[i].zero = min(node[i].zero, left.zero + right.zero);
			}

			if(node[i].changeable){
				if(node[i].type == 1){
					node[i].one = min(node[i].one, min(left.one+right.one+1, min(left.one+right.zero+1, left.zero+right.one+1)));
					node[i].zero = min(node[i].zero, left.zero+right.zero+1);
				}
				else{
					node[i].one = min(node[i].one, left.one+right.one+1);
					node[i].zero = min(node[i].zero, min(left.one+right.zero+1, min(left.zero+right.one+1, left.zero+right.zero+1)));
				}
			}
		}
		if(V)
			ans = node[0].one;
		else
			ans = node[0].zero;
#ifdef DEBUG
		for(i=0; i<n; ++i)
			printf("%10d %10d\n", node[i].zero, node[i].one);
#endif
		printf("Case #%d: ", icase+1);
		if(ans == INF)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}
