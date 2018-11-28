#include <string>
#include <cstdio>
#include <set>
using namespace std;

struct Tree 
{
    double value;
    string name;
    Tree *left;
    Tree *right;
    Tree() {
        left = right = NULL;
        name = "";
        value = 0;
    }    
};    
Tree *head;

string str;
int len;
char tmp[100];
set<string> featureSet;

void outputAns() {
	Tree *p;
	double ans;
	p = head;
	ans = 1.0;
	while (p!=NULL) {
		ans *= p->value;
		if (featureSet.count(p->name))
			p = p->left;
		else 
			p = p->right;
	}
	printf("%.7lf\n", ans);
}

void deal() 
{
	int n;
	int v, i, j;

	scanf("%d", &n);

	for (i=0; i<n; ++i) {
		scanf("%s", tmp);
		scanf("%d", &v);
		featureSet.clear();
		for (j=0; j<v; ++j) {
			scanf("%s", tmp);
			str = tmp;
			featureSet.insert(str);
		}
		outputAns();
	}
	
}

int isChar(char ch) {
	if (ch >='0' && ch <='9') return 1;
	if (ch == '.') return 1;
	if (ch >='a' && ch <='z') return 2;
	if (ch == '(' || ch == ')' ) return 3;
	return 0;
}

int readTree(Tree *node, int pos) 
{
	int left, right;
	if (pos >= len ) return len;
    while (str[pos] != '(') pos++;
	++pos;
	while (isChar(str[pos]) != 1) ++pos;
	left = pos;
	while ((str[pos] >='0' && str[pos]<='9') || str[pos] == '.') 
		pos++;
	right = pos;
	string sub = str.substr(left, right-left);
	sscanf(sub.c_str(), "%lf", &node->value);
	// debug
	// printf("Get node value:%lf\n", node->value);
	
	while (isChar(str[pos]) == 0 && pos < len) 
		 pos ++;
	if (str[pos] == ')') return pos+1;
	if (isChar(str[pos]) !=2 ) {
		printf("-----------Error-------\n");
		return len;
	}
	left = pos;
	while (isChar(str[pos]) == 2) 
		pos++;
	right = pos;
	node->name = str.substr(left, right-left);
	// printf("get name %s\n", node->name.c_str());
	Tree *ltree = new Tree();
	Tree *rtree = new Tree();
	node->left = ltree;
	node->right = rtree;
	pos = readTree(ltree, pos);
	pos = readTree(rtree, pos);
	return pos;
}    


void init()
{
    int i, n;

    scanf("%d", &n);
    gets(tmp);
    str = "";
    for (i=0; i<n; ++i) {
        gets(tmp);
        str += tmp; 
    }  
    head = new Tree();
    len = str.size();
    readTree(head, 0);      
}    


void destory(Tree *head) {
	if (head->left != NULL)
		destory(head->left);
	if (head->right != NULL)
		destory(head->right);
	delete(head);
}
int main()
{
//	printf("%s\n", string("abcdee").substr(3,3).c_str());
    int ncase, icase;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    scanf("%d", &ncase);
    for (icase = 0; icase<ncase; ++icase) {
        init();
		printf("Case #%d:\n", icase+1);
		deal();
		destory(head);
    }    
    
    return 0;
}    

/*
2
13
(0.2 furry
(0.81 fast
(0.3)
(0.2)
)
(0.1 fishy
(0.3 freshwater
(0.01)
(0.01)
)
(0.1)
)
)

*/