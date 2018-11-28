#ifdef LOCAL
#pragma warning(disable:4786)
#define ll __int64
#define FORMATLL "%I64d" 
#else
#define ll long long
#define FORMATLL "%lld"
#endif
#include <iostream>
#include <strstream>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <complex>
#include <cstdio>
#include <string>
#include <stack>
#include <cctype>
#include <cassert>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstring>
#include <functional>
#include <cstdlib>
#include <queue>
using namespace std;
#define trav(it,cont) for(it=(cont).begin(); it!=(cont).end(); ++it)
#define forn(i,n) for(i=0;(i)<(n);++i)
#define forab(i,a,b) for(i=(a);i<(b);++i)
#define MAX(a,b) ((a)<(b)?(b):(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define clr(a) memset(a,0,(sizeof a));
#define SWAP(a,b) a^=b,b^=a,a^=b;
using namespace std;

// template here

// template end

// global variable
int n;
char strtmp[2000];
char text[20000];
char str[1000];
char str2[1000];
set<string> lookup;
// global end

struct Tree
{
	string name;
	double p;
	Tree* lt, *rt;
	Tree(){
		lt = rt = NULL;
	}
};
Tree *head;

void deleteTree(Tree* t)
{
	if(t==NULL)return;
	deleteTree(t->lt);
	deleteTree(t->rt);
	delete t;
}
void printTree(Tree* t)
{
	if(t==NULL)return;
	cout << t->name << "_" << t->p << endl;
	cout << "  ";printTree(t->lt);
	cout << "  ";printTree(t->rt);
}

int scan(Tree* t, int b, int e)
{
	int i, bb, ee;
	double p;
	
	for(i=b; i< e; i++){
		if(text[i]=='(')break;
	}
	bb = i+1;
	
	for(i=bb; i< e; i++){
		if(text[i] == ')' || text[i] == '(')break;
	}
	ee = i;
	
	if(text[i] == ')'){
		text[ee-1] = 0;
		sscanf(text+bb, "%lf", &p);
		t->p = p;	
		return ee+1;
	}else{
		t->lt = new Tree;
		t->rt = new Tree;

		sscanf(text+bb, "%lf%s", &p, str2);
		t->name = string(str2);
		t->p = p;
		int e2 = scan(t->lt, ee, e);
		e2 = scan(t->rt, e2, e);
		i = e2;
		while(text[i] != ')')i++;
		return i+1;
	}
}

char input()
{
	int i, lv;
	scanf("%d", &n);gets(strtmp);
	
	lv = 0;
	forn(i,n){
		gets(strtmp+lv);
		lv += strlen(strtmp+lv);
	}

	lv = 0;
	for(i=0; strtmp[i]; ++i){
		if(strtmp[i] == '('){
			text[lv++] = ' ';
			text[lv++] = '(';
			text[lv++] = ' ';
		}else if (strtmp[i] == ')'){
			text[lv++] = ' ';
			text[lv++] = ')';
			text[lv++] = ' ';
		}else{
			text[lv++] = strtmp[i];
		}
	}
	text[lv] = 0;

	scan(head, 0, lv);

//	printTree(head);
	return 1;
}

double dfs(Tree* t)
{
	if(t->name == ""){
		return t->p;
	}
	if(lookup.find(t->name) == lookup.end()){
		return t->p * dfs(t->rt);
	}else{
		return t->p * dfs(t->lt);
	}
}

int main()
{
#ifdef LOCAL
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int i, k, lv, ca, ica, n, m;
	string name, fea;
	double p;
	scanf("%d", &ca);
	
	forn(ica,ca){
		head = new Tree;
		input();

		scanf("%d", &n);
		printf("Case #%d:\n", ica+1);

		forn(i,n){
			cin >> name >> m;	
			lookup.clear();
			forn(k,m){
				cin >> fea;
				lookup.insert(fea);
			}

			p = dfs(head);
			printf("%.7lf\n", p);
		}
		deleteTree(head);
	}
	return 0;
}
