#pragma warning(disable : 4786)
#include<stdio.h>
#include<string>
#include<map>
#include<string.h>
#include<vector>
#include<cctype>

using namespace std;

struct node{
	string attr;
	int val;
	double prob;
	int flag;

	node *father, *left, *right;

	node (){ father = left = right = NULL; flag  = 0;}
	node( string _attr, int _val, double _prob){ 
		attr = _attr, val = _val, prob = _prob;
		father = left = right = NULL;
		flag = 0;
	}

	~node(){
		delete left;
		delete right;
	}
};

string ss;
map<string, int> mm;
int flag[1009];
int cnt = 0;
node *root;
char str[1009];

void make_tree(){
	mm.clear();
	cnt = 0;
	root = new node();

	int i, j;
	string ss1;
	double temp;

	node *curptr = root;
	for( i=0; ss[i]; ++i){
		if( isspace(ss[i])) continue;
		if( ss[i] == '(' ){
			if(curptr->flag == 0){
				curptr->flag = 1; 
			}
			else if( curptr->flag == 1){
				curptr->left = new node();
				curptr->right = new node();
				curptr->left->father = curptr;
				curptr->right->father = curptr;
				curptr->left->flag = curptr->right->flag = 1;
				curptr->flag = 2;
				curptr = curptr->left;				
			}
			else if( curptr->flag == 2){
				curptr = curptr->right;
			}
		}
		else if( isalpha( ss[i] )){
			ss1 = "";
			for( j = i; isalpha(ss[j]); ++j)
				ss1 += ss[j];
			curptr->attr = ss1;
			if( mm.find(ss1) == mm.end()){
				mm[ss1] = cnt;
				cnt++;
			}
			curptr->val = mm[ss1];
			i = j-1;
		}
		else if( isdigit(ss[i]) || ss[i] == '.'){
			ss1 = "";
			for( j = i; isdigit(ss[j]) || ss[j] == '.'; ++j)
				ss1 += ss[j];
			sscanf(ss1.c_str(), "%lf", &temp);
			curptr->prob = temp;
			i = j-1;
		}
		else if( ss[i] == ')'){
			if( curptr->father )
				curptr = curptr->father;
		}
	}
}

double traverse(node *curptr){
	double ret = 1.0, temp = 1.0;

	ret *= curptr->prob;
	if( curptr->left){
		if( flag[curptr->val]){
			if( curptr->left){
				temp = traverse( curptr->left);
				ret *= temp;
			}		
		}
		else {
			if(curptr->right){
				temp = traverse( curptr->right);
				ret *= temp;
			}
		}
	}

	return ret;
}

int main(){
	int T, X, i, j;
	string ss1;
	int L, A, n, cur;
	double ret;

	freopen("A-large.in", "r", stdin);
	freopen("A2.out", "w", stdout);

	scanf("%d", &T);
	for(X = 1; X <=T; ++X){
		scanf("%d", &L); gets(str);
		ss = "";

		for( i=0; i<L; ++i){
			gets(str); ss1 = str; ss += ss1;
		}

		make_tree();

		scanf("%d", &A);
		printf("Case #%d:\n", X);
		for(i=0; i<A; ++i){
			scanf("%s%d", str, &n);
			memset( flag, 0, sizeof(flag));
			for( j=0; j<n; ++j){
				scanf("%s", str); ss1 = str;
				if( mm.find( ss1 ) == mm.end()) continue;
				cur = mm[ss1];
				flag[ cur ] = 1;
			}
			
			ret = traverse(root);
			printf("%.10lf\n", ret);
		}

		delete root;
	}

	return 0;
}