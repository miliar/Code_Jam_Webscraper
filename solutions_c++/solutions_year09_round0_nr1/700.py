#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <string.h>
#define MAX 76000

using namespace std;
struct box{
	int d;
	box *s[26];
}total[MAX],*cur,head;
char st[20],a[20][26];
int id,res,an,aNum[20];
bool u[20][26];
void insert(char *st){
	box *p = &head;
	for (char *i = st;*i;i++){
		if (p->s[*i-'a'] == NULL)
			p->s[*i-'a'] = cur++;
		p = p->s[*i-'a'];
	}
	p->d = ++id;
}
void dfs(int d,box *p){
	if (d == an){
		res++;
		return;
	}
	for (int i = 0;i < aNum[d];i++)
		if (p->s[a[d][i]])
			dfs(d+1,p->s[a[d][i]]);
}
int main(){
	int l,d,n,i,j,len,id = 0;
	string cst;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cur = &total[0],id = 0;
	scanf("%d%d%d",&l,&d,&n);
	for (i = 0;i < d;i++){
		scanf("%s",st);
		insert(st);
	}
	for (i = 1;i <= n;i++){
		cin >> cst;
		len = cst.size();
		memset(u,0,sizeof(u));
		memset(aNum,0,sizeof(aNum));
		j = 0,an = 0;
		while (j < len){
			if (cst[j] == '('){
				j++;
				while (cst[j] != ')'){
					if (!u[an][cst[j]-'a']){
						u[an][cst[j]-'a'] = true;
						a[an][aNum[an]++] = cst[j]-'a';
					}
					j++;
				}
			}else{
				u[an][cst[j]-'a'] = true;
				a[an][aNum[an]++] = cst[j]-'a';
			}
			an++,j++;
		}
		res = 0,st[l] = '\0';
		if (an == l) dfs(0,&head);
		printf("Case #%d: %d\n",i,res);
	}
	fclose(stdout);
}
