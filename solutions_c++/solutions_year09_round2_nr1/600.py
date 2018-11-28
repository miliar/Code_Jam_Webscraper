#include<iostream>
#include<string>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;

#define sz 1024*1024

struct node
{
	bool marked;
	double prob;
	string feature;
};

node tree[sz];
vector <string> animal[100];
vector <string> dectree;
	
void construct_tree()
{
	int pos = 0;
	double d = -1.0;
	double power;
	string str;
	for (int i = 0; i < dectree.size(); i++)
		for (int j = 0; j < dectree[i].size(); j++)
		{
			if (dectree[i][j] == '(')
			{
				if (!pos) pos = 1;
				else if (tree[2*pos].marked) pos = 2*pos+1;
				else pos = 2*pos;
				if (pos >= sz) { int n = 5; int m = 0; n = n/m; }
				tree[pos].marked = true;
				tree[pos].feature = "";
			}
			else if (dectree[i][j] == ')') pos /= 2;
			else if (dectree[i][j] >= 'a' && dectree[i][j] <= 'z')
			{
				str = "";
				while (j < dectree[i].size() && dectree[i][j] >= 'a' && dectree[i][j] <= 'z')
				{ str.append(1, dectree[i][j]); j++; }
				tree[pos].feature = str;
				j--;
			}
			else if (dectree[i][j] >= '0' && dectree[i][j] <= '1')
			{
				if (dectree[i][j] == '0') d = 0.0;
				else d = 1.0;
				power = 1.0;
				j++;
				while (j < dectree[i].size() && (dectree[i][j] == '.' || (dectree[i][j] >= '0' && dectree[i][j] <= '9')))
				{
					if (dectree[i][j] != '.')
					{
						power *= 0.1;
						d += power*double(dectree[i][j]-'0');
					}
					j++;
				}
				tree[pos].prob = d;
				j--;
			}
		}
}

void value(vector <string> &ani)
{
	int pos = 1;
	double prob = 1.0;
	int low, high, mid;
	while (tree[pos].marked)
	{
		prob *= tree[pos].prob;
		if (tree[pos].feature=="") break;
		else
		{
			low = 0; high = ani.size();
			while (high - low > 1)
			{
				mid = (high + low)/2;
				if (ani[mid] <= tree[pos].feature) low = mid;
				else high = mid;
			}
			if (ani.size() && ani[low] == tree[pos].feature) pos = 2*pos;
			else pos = 2*pos+1;
		}
	}
	printf("%.7lf\n", prob);
}

int main ()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small.txt", "w", stdout);
	int test_cases;
	cin >> test_cases;
	int l, a, n;
	string waste;
	for (int numb = 0; numb < test_cases; numb++)
	{
		cin >> l;
		memset(tree, 0, sizeof(tree));
		dectree.resize(l);
		cin.ignore();
		for (int i = 0; i < l; i++)
			getline(cin, dectree[i]);
		cin >> a;
		for (int i = 0; i < 100; i++)
			animal[i].clear();
		construct_tree();
		printf("Case #%d:\n", numb+1);
		for (int i = 0; i < a; i++)
		{
			cin >> waste;
			cin >> n;
			animal[i].resize(n);
			for (int j = 0; j < n; j++)
				cin >> animal[i][j];
			sort(animal[i].begin(), animal[i].end());
			value(animal[i]);
		}
	}
	return 0;
}