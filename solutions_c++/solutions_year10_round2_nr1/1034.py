#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define GI ({int _t; scanf("%d", &_t); _t;})
#define FOR(i, a, b) for (int i=a; i<b; i++)
#define REP(i, a) FOR(i, 0, a)
#define DBG(x) cout << #x << "::" << x << endl;
#define DBGV(_v) { FOR(_i, 0, _v.size()) { cout << _v[_i] << "\t";} cout << endl;}
#define sz size()
#define pb push_back

vector<string> explode(string delimiter, string str) {
    vector<string> arr;

    int strleng = str.length();
    int delleng = delimiter.length();
    if (delleng==0) return arr;
    int i=0, k=0, j=0; 
    while( i<strleng )
    {
		j=0;
        while (i+j<strleng && j<delleng && str[i+j]==delimiter[j]) j++;
        if (j==delleng) {
            arr.push_back( str.substr(k, i-k) );
            i+=delleng;
            k=i;
        }
        else {
            i++;
        }
    }
    arr.push_back(  str.substr(k, i-k) );
    return arr;
}

struct node { 
    string name; 
    vector <struct node*> child;
};

struct node* NewNode(string data) { 
  struct node* node = new(struct node);
  node->name = data; 
  return (node); 
} 

struct node* insert(struct node* node, string name) { 
	vector <struct node*> c = node->child;
	REP(i, c.sz) {
		if (c[i]->name == name) return NULL;
	}
	struct node *tmp = NewNode(name);
	return tmp;

}

struct node* fetch(struct node* node, string name) { 
	vector <struct node*> c = node->child;
	REP(i, c.sz) {
		if (c[i]->name == name) return c[i];
	}
	return NULL;

}

int main() {
	int kases = GI;
	for(int kase = 1; kase<= kases; kase++) {
		int n = GI, m = GI;
		struct node* root = NewNode("/");
		struct node* cur;struct node* tmp;
		REP(i, n) {
			string path;
			cin >> path;
			vector <string> tok = explode("/", path);
			cur = root;
			REP(j, tok.sz) {
				if (tok[j].sz > 0) {
					tmp =insert(cur, tok[j]);
					if (tmp != NULL) {
						cur->child.pb(tmp);
						cur = tmp;
					}
					else {
						cur = fetch(cur, tok[j]);
					}
				}
			}
		}
		int res = 0;
		REP(i, m) {
			string path;
			cin >> path;
			vector <string> tok = explode("/", path);
			cur = root;
			REP(j, tok.sz) {
				if (tok[j].sz > 0) {
					tmp =insert(cur, tok[j]);
					if (tmp != NULL) {
						res++;
						cur->child.pb(tmp);
						cur = tmp;
					}
					else {
						cur = fetch(cur, tok[j]);
					}
				}
			}
		}
		printf("Case #%d: %d\n", kase, res);
		
	}
}
