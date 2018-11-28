#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <map>
using namespace std;

struct Node{
	double value;
	string key;
	Node *right, *left;
	Node(double v) : value(v), right(NULL), left(NULL) {}
}*head;

int T, L, A, n, nCase=1;
string line, tmp;
int ptr, linecnt;

bool newToken;
int nCondition;
//string path[101];
map<string, bool> something;

string getToken(){
	if(!newToken){
		newToken = true;
		return tmp;
	}

	while(!(isdigit(line[ptr])||isalpha(line[ptr])||line[ptr]=='.'||line[ptr]=='\0')) ptr++;	
	while(line[ptr]=='\0'){
		if(linecnt==L) return "0.00";
		getline(cin, line), ptr=0;
		linecnt++;
		while(!(isdigit(line[ptr])||isalpha(line[ptr])||line[ptr]=='.'||line[ptr]=='\0')) ptr++;	
	}
	while(!(isdigit(line[ptr])||isalpha(line[ptr])||line[ptr]=='.'||line[ptr]=='\0')) ptr++;
	
	int pos=ptr;
	while( (isdigit(line[ptr])||isalpha(line[ptr])||line[ptr]=='.')) ptr++;
	tmp = line.substr(pos, ptr-pos);
	return tmp;
}
void createTree(Node* ptr){
	string token = getToken();
	if(isdigit(token[0])){
		newToken = false;
		return;
	}
	ptr->key = token;
	ptr->right = new Node( atof(getToken().c_str()) );
	createTree(ptr->right);
	ptr->left = new Node( atof(getToken().c_str()) );
	createTree(ptr->left);
}
void deleteTree(Node* ptr){
	if(ptr->right!=NULL) deleteTree(ptr->right);
	if(ptr->left!=NULL) deleteTree(ptr->left);
	delete ptr;
}
double probability(){
	Node *ptr=head;
	double ret=ptr->value;

	while(ptr->key!=""){
		if(something.find(ptr->key)!=something.end()) ptr= ptr->right;
		else ptr = ptr->left;
		ret *= ptr->value;
	}
	return ret;
}
void travel(Node* ptr){
	printf("%f", ptr->value);
	if(ptr->right!=NULL){
		printf("(%s)\n{\n", (ptr->key).c_str());
		travel(ptr->right);
		travel(ptr->left);
		printf("}");
	}
	printf("\n");
	
}

int main(){
	cin>>T;
	while(T-->0){
		cin>>L;
		getline(cin, tmp);
		line="", ptr=0; linecnt = 0;
		newToken=true;
		head = new Node( atof(getToken().c_str()) );
		createTree(head);
//		travel(head);
		getToken();
		cin>>A;
		printf("Case #%d:\n", nCase++);
		for(int i=0;i<A;i++){
			cin>>tmp;
			cin>>nCondition;
			something = map<string, bool>();
			for(int j=0;j<nCondition;j++){
				cin>>tmp;
				something[tmp] = true;
			}
			printf("%.7f\n", probability() );
		}
		deleteTree(head);
	}
    return 0;
}
