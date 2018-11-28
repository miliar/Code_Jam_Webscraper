#include <stdio.h>
#include <string.h>

struct Tree {
	int l,r;
	int f;
	char fe[20];
	float w;
}tree[100];

int main() {
	int TC, T;
	int i,j;
	freopen("3.txt","r",stdin);
	//freopen("2.txt","w",stdout);
	scanf("%d",&TC);
	for(T=1;T<=TC;T++) {
		int L;
		scanf("%d\n",&L);
		int node=0;
		tree[0].l=-1;
		tree[0].r=-1;
		tree[0].f=0;
		node++;

		int cur=0;
		for(i=0;i<L;i++) {
			char line[200];
			gets(line);
			char*p = line;
			while (*p==' ') p++;
			if (*p==')') {
				cur=tree[cur].f;
			}
			else {
				if (tree[cur].l==-1) {
					tree[cur].l=node;
				}
				else {
					tree[cur].r=node;
				}

				tree[node].f=cur;
				tree[node].l=tree[node].r=-1;
				cur=node;
				node++;

				p++;
				sscanf(p, "%f", &tree[cur].w);
				while(*p!=')' && *p!=' ') p++;
				if (*p==')') {
					cur=tree[cur].f;
				}
				else {
					p++;
					sscanf(p, "%s", tree[cur].fe);
				}
			}
		}

		int m,n;
		scanf("%d",&m);
		printf("Case #%d:\n",T);
		for(i=0;i<m;i++) {
			char pat[200];
			scanf("%s%d", pat, &n);
			char fe[200][20];
			for(j=0;j<n;j++) {
				scanf("%s", fe[j]);
			}
			int cur=1;
			double value=1;
			while(1) {
				value*=tree[cur].w;
				if (tree[cur].l==-1) break;

				for(j=0;j<n;j++) {
					if (strcmp(fe[j],tree[cur].fe)==0) {
						break;
					}
				}
				if (j<n) {
					cur=tree[cur].l;
				}
				else {
					cur=tree[cur].r;
				}
			}
			printf("%.6lf\n",value);
		}
	}
	return 0;
}