#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include<iostream>
#include<fstream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>
#include<list>
#include<map>
#include<deque>
#include<stack>
#include<queue>
#include<string>
#include<sstream>
#include<time.h>
#include<numeric>
#include<functional>

using namespace std;
#define _CRT_SECURE_NO_WARNINGS
#define INF  ((1 << 31) - 1)
#define LLINF  ((ll)((1LL << 63) - 1))
#define eps 0.00000001
#define million 1000000
#define PI 3.14159265358979323846
#define sz(v) ((int)(v).size())
#define MP make_pair
#define PB push_back
#define all(v) (v).begin(), (v).end()
typedef long long ll;

struct node{
	node() {
		s = "";
		par = left = right = 0;
		val = 0.0;
	}
	string s;
	double val;
	node * par;
	node * left;
	node * right;
};

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int id = 0; id < T; ++id) {
		cout << "Case #" << id + 1 << ":\n";
		int L;
		cin >> L;
		string s;
		getline(cin, s);//non read
		string text = "";
		for (int i = 0 ;i < L; ++i) {
			getline(cin, s);
			text += s;
		}
		node * root;
		root = new node;
		node * cur = 0;
		double pow = 1.0;
		for (int i = 0; i < text.size(); ++i) {
			if (text[i] == '(') {
				pow = 1.0;
				if (cur) {
					if (!cur->left) {
						node * new_node = new node;
						cur->left = new_node;
						cur->left->par = cur;
						cur = cur->left;
					} else {
						node * new_node = new node;
						cur->right = new_node;
						cur->right->par = cur;
						cur = cur->right;
					}
				} else {
					node * new_node = new node;
					root = cur = new_node;
				}
			} else 
				if (text[i] == ')') {
					pow = 1.0;
					if (cur->par) 
						cur = cur->par;
				} else 
					if('a' <= text[i] && text[i] <= 'z') {
						pow = 1.0;
						cur->s += text[i];
					} else 
						if ('0' <= text[i] && text[i] <= '9') {
							cur->val += pow * (text[i] - '0');
							pow /= 10.0;
						}
		}	
		int anim = 0;
		cin >> anim;
		for (int i = 0; i < anim; ++i) {
			vector<string> prop;
			string s;
			cin >> s;
			int k;
			cin >> k;
			for (int j = 0; j < k; ++j) {
				cin >> s;			
				prop.push_back(s);
			}
			double pr = 1.0;
			sort(all(prop));
			node * cur = root;
			while (cur->left) {
				pr *= cur->val;
				if (binary_search(all(prop), cur->s)) {
					cur = cur->left;
				} else {
					cur = cur->right;
				}
			}
			pr *= cur->val;
			printf("%0.7lf\n", pr);
		}
	}
	return 0;
}