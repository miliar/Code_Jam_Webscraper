#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <bitset>
#include <stack>
#include <set>
#include <string>
#include <algorithm>
#include <cctype>
#include <climits>
#include <cassert>

using namespace std;

const int BUF_SIZE = 4096;
struct Node{
	double p;
	string feature;
	Node * left,*right;
};

Node * make_tree(char *s1,char *s2)
{
	if (s1 == s2){
		return NULL;
	}
	
	char *p = s1;
	while (*p == '(' || *p == '\n' || *p == ' ')
		p++;
	double xx;
//	cout << p << endl;
	sscanf(p,"%llf",&xx);
//	cout << xx << endl;
	
	while ((*p >='0' && *p <= '9')||*p == '.')	
		p++;
	while (*p == '\n' || *p == ' ')
		p++;
		
	Node *temp = new Node;
	
	temp->p = xx;
	temp->feature = "";
	temp->left = NULL;
	temp->right = NULL;
		
	if (*p == ')'){
		return temp; 
	}else{
		char *q = p;
		while (*p!=' ' && *p != '\n'){
			p++;
		}
		string sf = string(q,p);
		temp->feature = sf;
		
		while (*p != '('){
			p++;
		}
		q = p;
//		cout << q << endl;
		if (*p != '(')
			return temp;
			
		int num = 1;
		p++;
		while (num > 0){
			if(*p == '('){
				num++;
			}
			if (*p == ')'){
				num--;
			}
			p++;
		}
//		cout << q << endl;
//		cout << p << endl;
		temp->left = make_tree(q,p-1);
		
		while (*p != '('){
			p++;
		}
		q = p;
		num = 1;
		while (num > 0){
			if(*p == '('){
				num++;
			}
			if (*p == ')'){
				num--;
			}
			p++;
		}
//		cout << "xx";
//		cout << p-1 << "xx";
		temp->right = make_tree(q,p-1);
		return temp;
	}
}

double getp(Node *root,vector<string> v)
{
	int size = v.size();
	int i = 0;
	double res = 1.0;
//	cout << "size = " << size << endl;
	while (root != NULL){
		res *= root->p;
		//cout << root->feature << endl;
		bool xx = false;
		for (int i = 0 ;i < size ;i++){
			if (v[i] == root->feature){
				xx = true;
				break;
			}
		}
		if (xx){
		//	cout << v[i] << endl;
			root = root->left;
		}else{
			root = root->right;
		}
		i++;
	}
	return res;
}
int main()
{
//	freopen("A-large.in","r",stdin);
//	freopen("A-large.txt","w",stdout);
	int T;
	char buf[BUF_SIZE] = {0};
	cin >> T;
	for (int i = 1 ;i <= T ;i++){
		int lines ;
		scanf("%d\n",&lines);
//		cout << lines << endl;
		int l = 0;
		char ch;
		int len = 0;
		while (l < lines){
			ch = getchar();
			if (ch == '\n'){
				l++;
			}
			buf[len++] = ch;
		}
	//	cout << buf ;
		Node *root = make_tree(buf,buf+len);
		int num;
		scanf("%d\n",&num);
		printf("Case #%d:\n",i);
		for (int j = 0 ;j < num ;j++){
			string str;
			cin >> str;
			int n;
			cin >> n;
			vector<string> vs;
			for (int k = 0 ;k < n ;k++){
				cin >> str;
				vs.push_back(str);
			}
			double res = getp(root,vs);
			//cout << res << endl;
			
			printf("%.6lf\n",res);
			
		}
	}
	return 0;
}
