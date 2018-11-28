#include <stdio.h>
#include <string.h>
#include <stdlib.h>
typedef struct T
{
	char *dir;
	struct T *child;
	struct T *next;
}T;

T root;
int ans;

void delroot(T * t)
{
	if(NULL == t) return;
	if(t->dir != NULL) free(t->dir);
	delroot(t->next);
	delroot(t->child);
}

void insert(char *path, int flag)
{
	int len;
	char dir[120];
	int dirlen = 0;
	int i, j = 0;
	T *myroot = &root;
	T *temp;
	len = strlen(path);
	for(i = 0, j = 0; i <= len; i++) {
		if(path[i] == '/' || path[i] == '\0') {
			if(j == 0) continue;
			else {
				dir[j] = '\0';
				temp = myroot->child;
				while(temp) {
					if(strcmp(temp->dir, dir) == 0)break;
					temp = temp->next;
				}
				if(temp == NULL) {
					temp = (T*)malloc(sizeof(T));
					temp->child = NULL;
					temp->next = myroot->child;
					temp->dir = (char*) malloc(j + 1);
					strcpy(temp->dir, dir);
					if(flag)ans++;
					myroot->child = temp;
				}
				myroot = temp;
				j = 0;
			}
		} else {
			dir[j++] = path[i];
		}
	}
}

int main()
{
	int t;
	int i, j;
	int n, m;
	char path[200];
	freopen("in","r",stdin);freopen("out","w",stdout);

	scanf("%d", &t);
	for(i = 1; i <= t; i++) {
		scanf("%d %d", &n, &m);
		root.child = NULL;
		root.dir = NULL;
		root.next = NULL;
		ans = 0;
		for(j = 0; j < n; j++) {
			scanf("%s", &path);
			insert(path, 0);
		}
		for(j = 0; j < m; j++) {
			scanf("%s", &path);
			insert(path, 1);		
		}
		printf("Case #%d: %d\n", i, ans);
		delroot(root.next);
		delroot(root.child);
//		printf("Case #%d: %s\n", i, ( (k + 1>= (1<<n) && ( (k & ( k + 1) ) == 0) )  || n ==1 && k %2 == 1   )? "ON" : "OFF");
	}
	return 0;
}