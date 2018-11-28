#include <stdio.h>
#include <string.h>

int n,m,len,ans;
int nc,nd;
int len_dir[100010];
char path[110];
char dir[100010][110];
struct node {
	int num;
	char name[110];
	node *ptr[510];
	
	node() {
		num = 0;
		memset(name,0,sizeof(name));
		for(int i=0;i<500;++i)
			ptr[i] = NULL;
	}
};

void Del(node *p) {
	if(p == NULL)	return;
	for(int i=0;i<500;i++)
		Del(p->ptr[i]);
	delete p;
}

node *Create(node *p,int now, bool flag){
	if(now >= len)	return NULL;
	int i,j,k,lenp;
	char name[110];
	lenp = 0;
	for(i=now;i<len && path[i] != '/';i++)
		name[lenp++] = path[i];
	name[lenp] = '\0';
	//puts(name);
	
	for(j=0;j<p->num;j++)
		if(p->ptr[j] != NULL && strcmp(name,p->ptr[j]->name) == 0) {
			Create(p->ptr[j],i+1,flag);
			break;
		}
	if(j >= p->num) {
		//printf("Create %s\n",name);
		if(flag == 1)	++ans;
		p->ptr[p->num] = new node();
		for(k=0;k<lenp;k++)
			p->ptr[p->num]->name[k] = name[k];
		p->ptr[p->num]->name[k] = '\0';
		Create(p->ptr[p->num],i+1,flag);
		p->num = p->num+1;
	}
	return p;
}

int main() {
	int t,c=0;
	
	scanf("%d",&t);
	while(t--) {
		scanf("%d%d",&n,&m);
		len = nc = nd = ans = 0;
		node *root = new node();
		for(int i=0;i<n;i++) {
			scanf("%s",path);
			len = strlen(path);
			Create(root,1,0);
		}
		for(int i=0;i<m;i++) {
			scanf("%s",path);
			len = strlen(path);
			Create(root,1,1);
		}
		//fprintf(stderr,"%d\n",c);
		printf("Case #%d: %d\n",++c,ans);
		Del(root);
		//puts("VV");
	}
	
	return 0;
}
