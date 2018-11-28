#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))

struct node{
	char path[120];
	node *c[120];
	int n;
}mem[100000];
int tim,l,node_id;
char p[120];
void insert(node *root,char path[]){
	int i;	
	if(path[l] == '/') l++;
	if(path[l] == 0) return;
	i = 0;
	while(path[l] != '/' && path[l] != 0) p[i++] = path[l++];
	p[i] = 0;
	for(i = 0; i < root->n; i++){
		if(strcmp(root->c[i]->path,p) == 0){
			insert(root->c[i],path);
			return;
		}
	}
	root->c[root->n++] = &mem[node_id++];
	strcpy(root->c[root->n-1]->path,p);
	tim++;
	insert(root->c[root->n-1],path);
}

int main(){
	int t,T,n,m,i;
	char path[100010];
	freopen("A-large.in","r",stdin);
	freopen("1da.out","w",stdout);
	scanf("%d",&T);
	for(t = 1; t <= T; t++){
		scanf("%d%d",&n,&m);
		node_id = 0;
		for(i = 0; i < 100000; i++){
			for(int j = 0; j < 120; j++){
				mem[i].c[j] = 0;
			}
			mem[i].n = 0;
		}
		node *root = &mem[node_id++];
		for(i = 0; i < n; i++){
			scanf("%s",path);
			l = 0;
			insert(root,path);
		}
		tim = 0;
		for(i = 0; i < m; i++){
			scanf("%s",path);
			l = 0;
			insert(root,path);
		}
		printf("Case #%d: %d\n",t,tim);
	}
	return 0;
}