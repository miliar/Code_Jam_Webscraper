#include <iostream>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
#include <deque>
#include <map>
#include <stack>
#include <sstream>

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((x).size())
#define sqr(x) ((x)*(x))
#define slen(x) ((x).length())

template<class T> T abs(T x) { return x > 0 ? x : -x;}

int n, m;
char tmp[1000];

struct node
{
	node *left;
	node *right;
	double value;
	string skill;
};

node* createNode()
{
	node *newNode = new node;
	newNode->left = NULL;
	newNode->right = NULL;
	newNode->value = 0.0;
	newNode->skill = "";
	return newNode;
}

int parse(node *root, string tree, int pos)
{
	int i = pos;
	bool point = false;
	double step = 0.1;

	while (!isdigit(tree[i])) i++;	
	
	root->value = 0.0;

	while ((tree[i] >= '0' && tree[i] <= '9') || tree[i] == '.')
	{
		if (tree[i] == '.')
			point = true;
		else
		{
			if (!point)
				root->value = root->value * 10 + tree[i] - 48;
			else
			{
				root->value = root->value + (tree[i] - 48) * step;
				step /= 10;
			}
		}
		i++;
	}
		
	while (isspace(tree[i])) i++;

	if (tree[i] == ')')
	{
		return i + 1;
	} else
	{
		while (isalpha(tree[i]))
			root->skill += tree[i++];
		while (tree[i] != '(') i++;
		root->left = createNode();
		i = parse(root->left, tree, i + 1);
		while (tree[i] != '(') i++;
		root->right = createNode();
		i = parse(root->right, tree, i + 1);
		while (tree[i] != ')') i++;
	}
	return i + 1;
}

bool hasAbility(vector<string> abil, string a)
{
	for (int i = 0; i < abil.size(); i++)
		if (abil[i] == a)
			return true;
	return false;
}

double solve(node *root, vector<string> abil)
{
	double result = root->value;
//	cout << result << " ";
	if (root->left == NULL)
		return result;
	if (hasAbility(abil, root->skill))
		return result * solve(root->left, abil);
	else
		return result * solve(root->right, abil);
}

int main()
{
	int i, j, f, l, k;
	node *root;
	
//	freopen("./input", "r", stdin);
//	freopen("output", "w", stdout);
	
	cin >> n;
	for (i = 0; i < n; i++)
	{
		cin >> l;
		gets(tmp);
		string tree = "";
		for (j = 0; j < l; j++)
		{
			gets(tmp);
			tree += tmp;
		}
		root = createNode();		
		parse(root, tree, 0);
		cin >> k;
		string name;
		string ability;
		vector<string> abil;
		int t;
		cout << "Case #" << i + 1 << ": " << endl;
		for (j = 0; j < k; j++)
		{
			cin >> name >> t;
			abil.clear();			
			for (f = 0; f < t; ++f)
			{
				cin >> ability;
				abil.pb(ability);
			}
			printf("%.7lf\n", solve(root, abil));
		}
	}
	
	return 0;
}
