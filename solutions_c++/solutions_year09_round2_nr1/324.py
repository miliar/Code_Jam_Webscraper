#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <string>
#include <sstream>
#include <cmath>
#include <cstdio>

using namespace std;

struct Node{
	double d;
	string s;	
	Node * left;
	Node * right;
};

void destroy(Node * root){
	if (root == NULL) return;
	destroy(root->left);
	destroy(root->right);
	delete root;
}

Node * read(){
	Node* root;
	root = new Node;
	char c;
	cin >> c;
	//cout << "c = " << c << endl;
	double x;
	cin >> x;
	string ss = "";
	cin >> c;
	root -> d = x;
	//cout << "x = " << x << endl;
	//cout << "ss = " << ss << endl;
	if (c == ')'){
		root -> s = "";
		root -> left = NULL;
		root -> right = NULL;	
	}
	else {
		string empty = "";
		char cc = cin.peek();
		if (cin.peek() >= 'a' && cin.peek() <= 'z')
			cin >> ss;
		root -> s = (empty + c + ss);
		//cout << root->s << endl;
		root->left = read();
		root->right = read();
		cin >> c;
	}
	return root;	
}

int main(){		
	
	int N, L , A, n;
	cin >> N;
	for (int i = 1 ; i <= N ; i++){
		cin >> L;
		cout << "Case #" << i << ":" << endl;	
		Node * head = read();
		cin >> A;
		string a;
		for (int j = 0 ; j < A ; j++){
			double p = 1.0;
			cin >> a;
			cin >> n;
			string attr[n];
			for (int k = 0 ; k < n; k++) {
				cin >> attr[k];	
			}
			Node * temp = head;
			while (true){
				p *= temp -> d;
				if (temp->left == NULL) break;
				bool ok = false;
				for (int k = 0 ; k < n; k++){
					if (temp->s == attr[k]) {
						ok = true;
						break;		
					}
				}		
				if (ok) temp = temp->left;
				else temp = temp->right;					
			}	
			printf("%.10f\n", p);
		}
		destroy(head);
	}	
 
	return 0;
}