/* 
 * SOUR:
 * ALGO:
 * DATE: Sun, 13 Sep 2009 00:29:53 +0800
 * COMM:
 * */
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cassert>
using namespace std;
typedef long long LL;
const int maxint = 0x7fffffff;
const long long max64 = 0x7fffffffffffffffll;
/*
tree ::= (weight [feature tree tree])
weight is a real number between 0 and 1, inclusive
feature is a string of 1 or more lower case English letters
 * */
const int N = 10010;
char s[N][128];
int hash[N];

int ELFHash(char *str)
{
	int hash = 0;
	int x = 0;
	while (*str) {
		hash = (hash <<4) + (*str++);	
		if ((x = hash & 0xF0000000L) != 0) {
			hash ^= (x >> 24);	
			hash &= ~x;	
		}
	}
	return (hash & 0x7FFFFFFF);	
}


int top;
struct T {
	int idx;
	double w;
	T *left, *right;
} pool[N];
int pt;

int length;
void dfs(T * root)
{
	//printf("%*s dfs begin\n",length,"");
	char t[128];
	while ((t[0] = getchar()) != '(') ;

	scanf("%lf", &root->w);
	do {
		t[0] = getchar();
	} while (t[0] == ' ' || t[0] == '\n');
	if (t[0] == ')') {
		return;
	}
	int len = 1;
	char ch= getchar();
	while(ch != ' ' && ch != '\n') {
		t[len++] = ch;
		ch = getchar();
	}
	t[len] = 0;
	//scanf("%s\n", t + 1);
	strcpy(s[top], t);
	root->idx = top, top++;

	length += 4;
	//printf("%*s %.3f\n", length, "", root->w);
	if(root->left == NULL) root->left = &pool[pt++]; dfs(root->left);
	if(root->right == NULL) root->right = &pool[pt++]; dfs(root->right);
	length -= 4;

	while ((t[0] = getchar()) != ')') ;
	//printf("%*s dfs end\n",length,"");
}

int n;
char buf[N][128];
bool find(int idx) 
{
	int i;
	for(i = 0;i < n;i++) {
		if(hash[idx] == ELFHash(buf[i]) && 0 == strcmp(buf[i],s[idx]))
			return true;
	}
	return false;
}
double cacu(T * root)
{
	if (root == NULL) {
		return 1.00;
	}
	//printf("cacu:%.3f\n",root->w);
	double tmp = root->w;
	if (root->idx > 0 && find(root->idx)) {
		tmp *= cacu(root->left);
	} else {
		tmp *= cacu(root->right);
	}
	return tmp;
}

int main()
{

	int i, j, k, C, L,m;
	char t;
	scanf("%d\n", &C);
	for (int c = 1; c <= C; c++) {
		scanf("%d\n", &L);
		memset(pool, 0, sizeof(pool));
		length = 0;
		T *root = &pool[0];
		top = 1;
		pt = 1;
		dfs(root);
		while((t = getchar()) != '\n');
		for(i = 0;i < top;i++) {
			hash[i] = ELFHash(s[i]);
		}

		scanf("%d", &m);
		printf("Case #%d:\n", c); 
		while (m-- > 0) {
			char t[128];
			scanf("%s", t);
			scanf("%d", &n);
			for (i = 0; i < n; i++) {
				scanf("%s", buf[i]);
			}
			double res = cacu(root);
			printf("%.7lf\n", res);
		}

	}
	return 0;
}
