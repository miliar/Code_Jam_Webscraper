#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<queue>
#include<deque>
#include<map>
#include<functional>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOREACH(i,x) for(typeof(x)::iterator it=(x).begin(); it!=(x).end(); ++it)
#define EACH(i,x) REP(i,(x).size())
#define sz	size()
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define pb	push_back
#define mp	make_pair
#define eps	1e-15
#define inf 0x3FFFFFFF

typedef long long int lint;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

int p;
int m[1050];
int price[1050];
int n;

struct node {
	node * left;
	node * right;
	int price;
	int m;

	node() : left(NULL), right(NULL), price(-1), m(-1){}
	~node() { if (left) delete left; if(right) delete right; }
};

map<pair<node*, int>, int> memo;

int find( node* nd, int skip )
{
	if (!nd->left) {
		if ( skip > nd->m ) return inf;
		return 0;
	}

	if (memo.find(make_pair(nd, skip)) != memo.end() ) {
		return memo[make_pair(nd, skip)];
	}
	int &ret = memo[make_pair(nd, skip)];
	
	int l = find(nd->left, skip);
	int r = find(nd->right, skip);
	if ( l >= inf || r >= inf ) ret = inf;
	else ret = nd->price + l + r;

	int t = find(nd->left, skip+1) + find(nd->right, skip+1);
	if (t < ret) ret = t;

	return ret;
}

int set_m( node* nd ) 
{
	if (!nd->left) return nd->m;
	nd->m = min(set_m(nd->left), set_m(nd->right));
	return nd->m;
}

void solve()
{
	scanf("%d",&p);
	n = 1 << p;
	memo.clear();

	vector<node*> v_old;
	REP(i,n) {
		int m;
		scanf("%d",&m);
		node* nd = new node();
		nd->m = m;
		v_old.push_back(nd);
	}

	int k = n;

	REP(i,p) {
		k /= 2;
		vector<node*> v_new;
		REP(i,k) {
			int price;
			scanf("%d",&price);
			node* nd = new node();
			nd->price = price;
			nd->left = v_old[i*2];
			nd->right = v_old[i*2+1];
			v_new.push_back(nd);
		}
		v_old = v_new;
	}

	node*root = v_old[ 0 ];

	set_m(root);

	printf("%d\n", find(root, 0) );

	delete(root);
}

int main(void)
{
	//freopen("","r",stdin);
	//freopen("T-small.out","w",stdout);
	int test;
	scanf("%d",&test);
	REP(i,test) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

