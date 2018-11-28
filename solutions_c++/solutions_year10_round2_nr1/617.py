#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<list>
using namespace std;

struct dir{
	char*  name;
	list<struct dir*> child;
};

int count;


void insert(struct dir* nowdir, char *path){
	int i;
	char *addname;
	char tmp[2000];
	struct dir * nextdir;
	list<struct dir*>:: iterator it;

	//printf("haha:[%s]\n", nowdir->name);

	if(path[0] == 0)
		return;
	path = &path[1];	//skip '/'
	for(i = 0; path[i] != 0 && path[i] != '/'; ++i){
		tmp[i] = path[i];
	}
	tmp[i] = 0;
	path = &path[i];		// path for later function call
	addname = strdup(tmp);	
	
	//printf("add i[%d]name = [%s]\n",i, addname);
	
	for(it = (nowdir->child).begin(); it != (nowdir->child).end(); it++){
		if(strcmp((*it)->name, addname) == 0){
			nextdir = (*it);
			break;
		}
	}		
	if(it == nowdir->child.end()){
		struct dir * tmp;
		tmp = new struct dir;
		tmp->name  = addname;
		(nowdir->child).push_back(tmp);
		nextdir = tmp;
		++count;
	}
	
	insert(nextdir, path);
	return ;
}

int main(void){
	int I, T;
	scanf("%d", &T);
	for(I = 1; I <= T; ++I){
		struct dir * root = new struct dir;
		int i, n, m;
		root->name = "";
		scanf("%d%d", &n, &m);
		for(i = 0; i < n; ++i){ 
			char path[200];
			scanf("%s", path);
			insert(root, path);
		}
		count = 0;
		for(i = 0; i < m; ++i){
			char path[200];
			scanf("%s", path);
			insert(root, path);
		}
		printf("Case #%d: %d\n", I, count);	
	}
	
}
