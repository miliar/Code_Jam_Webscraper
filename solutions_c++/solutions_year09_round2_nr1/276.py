#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<vector>
#include<string>
#include<algorithm>
#include<assert.h>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)

struct Node {
	string feature;
	double weight;
	Node * left;
	Node * right;

	Node() {
		feature = "";
		weight = 0.0;
		left = right = NULL;
	}
};

string str;

vector<string>fl;

void remove_spaces() {
	int i,j;
	for(i = 0; i < str.size(); i++) if(str[i] != ' ') {
		str = str.substr(i);
		break;
	}
	for(i = (int)str.size() - 1; i >=0; i--) if(str[i] != ' ') {
		str = str.substr(0,i+1);
		break;
	}

	for(i = 0; i < str.size(); i++) {
		if(str[i] == '(') {
			for(j = i + 1; j < str.size(); j++) {
				if(str[j] != ' ') break;
			}
			str = str.substr(0,i+1) + str.substr(j);
		}
	}

	for(i = 0; i < str.size(); i++) {
		if(str[i] == ')') {
			for(j = i - 1; j >= 0; j--) {
				if(str[j] != ' ') break;
			}
			str = str.substr(0,j+1) + str.substr(i);
			i = j+1;
		}
	}

	for(i = 0; i < str.size(); i++) {
		if(str[i] == '(') {
			for(j = i - 1; j >= 0; j--) {
				if(str[j] != ' ') break;
			}
			str = str.substr(0,j+1) + str.substr(i);
			i = j+1;
		}
	}
}

void build_tree(int st, int en, Node * tree) {
	assert(str[st] == '(');
	assert(str[en] == ')');
	int i;
	string wt,nm;
	double w;
	for(i = st+1; i < en; i++) {
		if(str[i] == ' ' || str[i] == '(') break;
		wt += str[i];
	}
	//assert(i != en);
	if(str[i] == ' ') {
		for(++i; i < en; i++) {
			if(str[i] == '(') break;
			nm += str[i];
		}
	}
	sscanf(wt.c_str(),"%lf",&w);
	tree->weight = w;
	tree->feature = nm;
	//printf("%lf %s\n",w,nm.c_str());
	if(i == en) { //leaf node
		assert(nm == "");
		return;
	}
	//now determine the left and right
	int ct=1;
	int nw_st = i++;
	Node * left;
	Node * right;
	left = new Node();
	right = new Node();
	for(; i < en; i++) {
		if(str[i] == '(') ct++;
		if(str[i] == ')') {
			ct--;
			if(ct == 0) {			
				build_tree(nw_st,i,left);
				build_tree(i+1,en-1,right);
				break;
			}
		}
	}
	tree->left = left;
	tree->right = right;
}

bool doesHave(string s) {
	int i;
	rep(i,fl.size()) if( s == fl[i]) return true;
	return false;
}

double process(Node * tree) {
	if(tree->left == NULL && tree->right == NULL) return tree->weight;
	if(doesHave(tree->feature)) {
		return tree->weight * process(tree->left);
	}
	else return tree->weight * process(tree->right);
}

int main() {
	int i,T,kase=1;
	int L,j,n;
	char name[30];
	char s[100];
	int A;
	double res;
	scanf("%d",&T);
	while(T--) {
		printf("Case #%d:\n",kase++);
		scanf("%d",&L);
		str = "";
		gets(s);
		rep(i,L) {
			gets(s);
			str += s;
			str += " ";
		}
		remove_spaces();
		//printf("%s\n",str.c_str());
		Node * root;
		root = new Node();
		build_tree(0,(int)str.size()-1,root);
		scanf(" %d",&A);
		rep(i,A) {
			scanf("%s %d",name, &n);
			fl.clear();
			rep(j,n) {
				scanf(" %s",name);
				fl.push_back(name);
			}

			res = process(root);
			printf("%.10lf\n",res);
		}
	}
	return 0;
}