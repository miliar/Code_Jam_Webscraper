#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define Int signed long long int  /* 64b Unix : %lld , %llu  */
// #define Int __int64            /* 64b win  : %I64d, %I64u */

// #define DEBUG
#define DB(x) { cout << __LINE__ << ": " << #x << " " << x << endl; }
#define HERE { cout << "HERE\n"; }

#define INF 1000000000

#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define NL printf("\n");
#define RET return
#define sqr(x) ((x)*(x))
#define myabs(x) (((x)<0)?(-(x)):(x))

#define VAR(a,T) __typeof(T) a=(T)
#define BEG(c) (c).begin()
#define BEGR(c) (c).rbegin()
#define END(c) (c).end()
#define ENDR(c) (c).rend()
#define ALL(c) BEG(c), END(c)
#define POS(c,x) ((c).find(x) != END(c))
#define CLR(c) memset(c, 0, sizeof(c))
#define REVERSE(c) reverse(ALL(c))
#define SORT(c) sort(ALL(c))
#define SIZE(c) ((int) (c).size())
#define SSORT(c) stable_sort(ALL(c))
#define REP(i,e) for(int i = 0; i < (e); ++i)
#define FORU(i,b,e) for(int i = (b); i <= (signed)(e); ++i)
#define FORD(i,b,e) for(int i = (b); i >= (signed)(e); --i)
#define VELU(it,c) for(VAR(it, BEG(c)); it != END(c); ++it)
#define VELD(it,c) for(VAR(it, BEGR(c)); it != ENDR(c); ++it)
#define TLE FORU(yy,0,1000000000) FORU(xx,0,1000000000) cout << "\n";

typedef vector<int> vi;
typedef vector<string> vs;

template <class T> inline string toString (const T& t) {
  stringstream ss; ss << t; return ss.str();
}

vs split (string s, string del = " ") { vs res;
	int ss = SIZE(s), sdel = SIZE(del);
	for (int p = 0, q; p < ss; p = q+sdel) {
		if ((q = s.find(del, p)) == (signed)string::npos) q = ss;
		if (q-p>0) res.PB(s.substr(p,q-p));
	} return res;
}

int T;
int L; // #lines
int A; // #animals

struct node {
	double weight;
	string feature;
	node *L, *R;
};

node *root;
string tree;
int pos;

// tree ::= (weight [feature tree tree]) = token
// weight is a real number between 0 and 1, inclusive
// feature is a string of 1 or more lower case English letters

node* createTree () {
	//cout << "createTree: at = " << pos << endl;
	node* n = new node();
	n->L = NULL; n->R = NULL;

	while (pos < tree.size()-1) {
	  while (tree[pos] == ' ' || tree[pos] == '\n') ++pos;
		if (tree[pos] == '(') {
			++pos; n->L = createTree();
			//cout << "left son created: " << n->weight << endl;
			while ((pos < tree.size()-1) && (tree[pos] == ' ' || tree[pos] == '\n')) ++pos;
			if (tree[pos] == '(') {
				++pos; n->R = createTree();
			}
		} else {
			if (tree[pos] == ')') { ++pos; return n; }
			string descNode = "";
			while ((pos < tree.size()-1) && (tree[pos] != '(' && tree[pos] != ')')) {
				descNode += tree[pos];
				++pos;
			} if (tree[pos] == '(') --pos;

			//cout << "node desc: " << descNode << endl;

			// get weight * feature -> put into node
			vs descAnimal = split(descNode);
			n->weight = atof(descAnimal[0].c_str());
			if (descAnimal.size() == 2) {
				n->feature = descAnimal[1];
			} else {
				n->feature = "";
			}

			//cout << "NODE: " << n->weight << " " << n->feature << endl;
			//cout << "AT: " << pos << " " << tree[pos] << endl;
		}

		if (tree[pos] == ')') { ++pos; return n; }
		++pos;
	}

	cout << "OUT" << endl;
	return n;
}

void buildTree() {
	tree = "";
	string line;
	FORU(i,1,L) {
		getline(cin, line);
		tree += line;
	}
	//cout << tree << endl;

	// (0.5 cool  ( 1.000)  (0.5 ))
	// (0.2 furry  (0.81 fast    (0.3)    (0.2)  )  (0.1 fishy    (0.3 freshwater      (0.01)      (0.01)    )    (0.1)  ))

	int i = 0; while (tree[i] != '(') ++i;
	 pos = i+1;
	root = createTree();
}

void traverseBT (node *n) {
	if (n == NULL) return;
	//cout << "(" << n->weight << ", " << n->feature << ")" << endl;
	traverseBT(n->L);
	traverseBT(n->R);
}

double cute (node *n, string animal, vs feat) {
	double res = 1.0;
	if (n == NULL) return res;
	//cout << "cute " << animal << " " << n->weight << " " << n->feature << endl;

	res *= n->weight;
	bool hasFeat = false;
	FORU(i,0,feat.size()-1) if (n->feature == feat[i]) {
		hasFeat = true;
		//cout << animal << " has " << 	n->feature << endl;
		break;
	}

	if (hasFeat) {
		//cout << "going left" << " " << n->L << endl;
		return res * cute(n->L, animal, feat);
	} else {
		//cout << "going right" << " " << n->R << endl;
		return res * cute(n->R, animal, feat);
	}

	return res;
}

int main() {

	string animal;

  scanf("%d\n",&T);
  FORU(testcase,1,T) {
  	printf("Case #%d:\n",testcase);
  	scanf("%d\n",&L);
  	double ans = 0.0;
  	buildTree();
  	//cout << "TREE: " << endl;
  	//traverseBT(root);
  	//cout << endl;
  	scanf("%d\n",&A);
  	FORU(i,1,A) {
  		getline(cin, animal);
  		vs desc = split(animal);
  		string anim = desc[0];
  		vs feat;
  		int nf = atol(desc[1].c_str());
  		FORU(i,1,nf) feat.PB(desc[i+1]);

  		ans = cute (root, anim, feat);
  		printf("%.7lf\n",ans);
  	}
  }

  return 0;
}
