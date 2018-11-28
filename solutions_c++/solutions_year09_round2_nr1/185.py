#pragma warning(disable : 4786)

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

struct node{
	node(){
		w = 0;
		lc = rc = NULL;
	}

	double w;
	char name[15];
	node *lc, *rc;
};

char tree[10000];
char temp[100];
node* bst;
set<string> chs;
int len;
double ans;

void buildtree(int &idx, node* &bst){
	bst = new node;

	// 找到数字，读取权值
	while (!isdigit(tree[idx])) idx++;
	sscanf(&tree[idx], "%lf", &bst->w);

	// 找到数字后面的字母或者')'
	while (true){
		idx++;
		if (isalpha(tree[idx]) || tree[idx] == ')') break;
	}

	// 非叶子节点
	if (isalpha(tree[idx])){
		sscanf(&tree[idx], "%s", bst->name);

		while (tree[idx] != '(') idx++;
		buildtree(idx, bst->lc);
		//idx++;

		while (tree[idx] != '(') idx++;
		buildtree(idx, bst->rc);
	}
	// 叶子节点
	else {
		while (tree[idx] != ')') idx++;
	}
}

void init(){
	int L, i;

	memset(tree, 0, sizeof(tree));
	memset(temp, 0, sizeof(temp));

	scanf("%d\n", &L);
	for (i = 1; i <= L; i++){
		gets(temp);
		strcat(tree, temp);
		strcat(tree, " ");
	}

	len = strlen(tree);
	bst = NULL;
	int idx = 0;
	buildtree(idx, bst);
}

void solve(node* bst){
	if (bst == NULL) return;

	ans *= bst->w;

	if (chs.find(bst->name) != chs.end()){
		solve(bst->lc);
	}
	else {
		solve(bst->rc);
	}
}

void calc(){
	int N, i, j, tt;
	string temp;
	string animal;

	scanf("%d\n", &N);
	for (i = 1; i <= N; i++){
		cin >> animal;
		cin >> tt;
		chs.clear();
		for (j = 1; j <= tt; j++){
			cin >> temp;
			chs.insert(temp);
		}

		ans = 1;
		solve(bst);
		
		printf("%.7lf\n", ans);
	}
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T, i;
	scanf("%d\n", &T);
	for (i = 1; i <= T; i++){
		printf("Case #%d:\n", i);
		init();
		calc();
	}

	return 0;
}