#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"
#include "iostream"
#include "sstream"
#include "string"
#include "algorithm"
#include "vector"
#include "queue"
#include "map"

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

#define all(s) s.begin(), s.end()

struct s_s
{
	double w;
	string fea;
	int left, right;
};
int trees_count;
vector<s_s> trees;

int parse (string s)
{
	char c;
	stringstream st (s);

	st >> c;
	double w;
	st >> w;

	string fea;
	st >> fea;

	int cur_i = trees_count++;
	trees.push_back(s_s());

	trees.back().w = w;
	trees[cur_i].left = trees[cur_i].right = 0;

	if (fea.find(')') == -1)
	{
		trees.back().fea = fea;

		int first_brack = s.find('(');
		int second_brack = s.find('(', first_brack + 1);
		if (second_brack != -1)
		{
			int deep = 0;
			int start;
			bool right = false, p = false;
			for (int i = second_brack; i < s.length() ; i++)
			{
				if (s[i] == '(')
				{
					deep++;
					p = true;
					if (deep == 1)
						start = i;
				}
				if (s[i] == ')')
					deep--;
				if (deep == 0 && p)
				{
					int res = parse(s.substr(start, i - start + 1));
					if (right)
						trees[cur_i].right = res;
					else
						trees[cur_i].left = res;
					right = true;
					p = false;
				}
				
			}
		}
			
	}

	return cur_i;
}
vector<string> feas;

double rec (int cur)
{
	s_s & tree = trees[cur];
	if (tree.left)
	{
		s_s & sub_tree = trees[tree.left];
		if (tree.fea.empty() || binary_search(all(feas), tree.fea))
			return rec (tree.left) * tree.w;
	}
	if (tree.right)
	{
		s_s & sub_tree = trees[tree.right];
		
		return rec (tree.right) * tree.w;
	}
	return tree.w;
}

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	
	int test_count;
	cin >> test_count;



	for (int test = 0; test < test_count ; test++)
	{
		fprintf(stderr, "%d\n", test);
		

		int l, animal_n;
		cin >> l;
		string s;
		getline(cin, s);

		string tree_s;
		for (int i = 0; i < l ; i++)
		{
			getline(cin, s);
				
			tree_s += ' ' + s;
		}

		trees_count = 0;
		trees.clear();
		parse (tree_s);

		printf("Case #%d:\n", test + 1);
		cin >> animal_n;
		for (int i = 0; i < animal_n ; i++)
		{
			string name;
			cin >> name;
			int c;
			cin >> c;
			feas.clear();
			
			for (int j = 0; j < c ; j++)
			{
				string fea;
				cin >> fea;
				feas.push_back(fea);
			}

			sort(all(feas));

			printf("%.7f\n", rec(0));
		}


	}

}