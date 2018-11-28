#include <iostream>
#include <string>
#include <vector>

const int MAX_L = 20;
const int MAX_D = 5005;
const int MAX_N = 505;


struct NODE{
	NODE *child[26];
	int end;
	NODE(){
		end = 0;
		memset(child, NULL, sizeof(child));
	}
}*root;



int l, d, n;
int now[MAX_L][26];
int ans;

/*
int go()
{
	int i, j, res = 0;
	for(i = 0; i < d; i++){
		for(j = 0; j < l; j++){
			int data = dic[i][j] - 'a';
			if(now[j][data] == 0)  break;
		}
		if(j >= l)  res++;
	}
	return res;
}
*/

void dfs(int i, NODE* pp)
{
	int j, k;
	if(i == l){
		ans++;
		return;
	}
	for(j = 0; j < 26; j++){
		if(now[i][j]){
			if(pp->child[j] != NULL){
				dfs(i + 1, pp->child[j]);
			}
		}
	}
}

int go()
{
	int i, j;
	NODE* p = root;
	ans = 0;
	dfs(0, p);
	return ans;
}

void insert(NODE *p, char *t)
{
	int i, len = strlen(t);
	for(i = 0; i < len; i++){
		int data = t[i] - 'a';
		if(p->child[data] == NULL){
			p->child[data] = new NODE();
		}
		p = p->child[data];
		if(i == len - 1)  p->end = 1;
	}
}


int main()
{
	freopen("f://A-large.in", "r", stdin);
	freopen("f://A-large.out", "w", stdout);
	while(scanf("%d%d%d", &l, &d, &n) != EOF){
		int i, j, k;
		root = new NODE();
		for(i = 0; i < d; i++){
			//scanf("%s", dic[i]);
			char tmp[MAX_L];
			scanf("%s", tmp);
			insert(root, tmp);
		}
		for(i = 1; i <= n; i++){
			memset(now, 0, sizeof(now));
			char tmp[30 * 15];
			scanf("%s", tmp);
			int len = strlen(tmp);
			int nowi = 0;
			for(j = 0; j < len; j++){
				if(tmp[j] != '('){
					now[nowi++][tmp[j] - 'a'] = 1;
				}
				else{
					for(k = j + 1; k < len; k++){
						if(tmp[k] == ')'){
							j = k;
							nowi++;
							break;
						}
						else{
							now[nowi][tmp[k] - 'a'] = 1;
						}
					}
				}
			}
			printf("Case #%d: %d\n", i, go());
			/*
			for(i = 0; i < l; i++){
				for(j = 0; j < 26; j++){
					if(now[i][j]){
						printf("%c", 'a' + j);
					}
				}
				printf("\n");
			}
			*/
		}
	}
}