#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <string>
#include <iostream>
#include <cassert>
#include <sstream>

using namespace std;

struct Tree {
	double p;
	string f;
	Tree * l, * r;

	void Read(istringstream & Cin)
	{
		char ch;
		Cin >> ch;
		assert(ch == '(');
		Cin >> p;
		Cin >> f;
		if (f != ")")
		{
			l = new Tree();
			r = new Tree();
			l -> Read(Cin);
			r -> Read(Cin);
			Cin >> ch;
		}
	}
};

void InsertSpace(char * s, string & t)
{
	for (int i = 0; s[i]; ++i)
	{
		if (s[i] == '(')
			t = t + s[i] + ' ';
		else
			if (s[i] == ')')
				t = t + ' ' + s[i];
			else
				t = t + s[i];
	}
}


char buf[100000];
char * cur_buf;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tt;
	scanf("%d\n", &tt);
	for (int ii = 1; ii <= tt; ++ii)
	{
		int o;
		scanf("%d\n", &o);
		cur_buf = buf;
		for (int i = 0; i < o; ++i)
		{
			gets(cur_buf);
			cur_buf += strlen(cur_buf);
			cur_buf[0] = ' ';
			cur_buf++;
			cur_buf[0] = 0;
		}
		string s_tree;
		InsertSpace(buf, s_tree);
		istringstream Cin (s_tree);
		Tree * tree = new Tree();
		tree -> Read(Cin);

		printf("Case #%d:\n", ii);

		int q;
		scanf("%d\n", &q);
		for (int i = 0; i < q; ++i)
		{
			string name, cur_f;
			int n;
			cin >> name >> n;
			set <string> anim;
			for (int j = 0; j < n; ++j)
			{
				cin >> cur_f;
				anim.insert(cur_f);
			}

			Tree * cur = tree;
			double cur_p = 1.0;
			while (cur -> f != ")")
			{
				cur_p *= cur -> p;
				if (anim.find(cur -> f) != anim.end())
					cur = cur -> l;
				else
					cur = cur -> r;
			}
			cur_p *= cur -> p;

			printf("%.10lf\n", cur_p);
		}
	}
	
	return 0;
}