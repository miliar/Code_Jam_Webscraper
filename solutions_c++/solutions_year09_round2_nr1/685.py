#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <string>
#include <cctype>
using namespace std;
struct NODE {
	char name[16];
	double prob;
	NODE *t, *f;
};
void readnode(NODE *p) {
	p->t=p->f=0;
	p->name[0]=0;
	while (getchar()!='(');
	scanf("%lf", &(p->prob));
	char c;
	while (isspace(c=getchar()));
	if (c!=')') {
                ungetc(c,stdin);
		scanf("%s", p->name);
		p->t=new NODE;
		p->f=new NODE;
		readnode(p->t);
		readnode(p->f);
		while (getchar()!=')');
	}
}
void freenode(NODE *p) {
	if (p) {
		freenode(p->t);
		freenode(p->f);
		free(p);
	}
}
double dfs(NODE *p, set<string>&s) {
	if (p->name[0]) {
		return (p->prob)*dfs(s.find(p->name)==s.end()?p->f:p->t,s);
	} else return p->prob;
}
int main()
{
	freopen("A-large (1).in", "r", stdin);
	freopen("A.out", "w", stdout); 
	int N, L, A, n;
	scanf("%d", &N);
	char c, s[100];
	NODE *head;
	for (int tc=1; tc<=N; ++tc) {
        cerr << tc << " " << N << endl; 
		scanf("%d", &L);
		readnode(head=new NODE);
		scanf("%d", &A);
		printf("Case #%d:\n", tc);
		while (A--) {
			scanf("%s", s);
			scanf("%d", &n);
			set<string> prop;
			while (n--) {
				scanf("%s", s);
				prop.insert(s);
			}
			printf("%.7lf\n", dfs(head, prop));
		}
		freenode(head);
	}
}
