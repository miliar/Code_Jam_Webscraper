#include <iostream>
#include <string>
#include <set>

using namespace std;

struct Node
{
	long double p;
	string dec;
	Node *c, *cd;

	Node()
	{
		c = cd = NULL;
	}

	~Node()
	{
		if (c != NULL)
			delete c;
		if (cd != NULL)
			delete cd;
	}
};

Node *root;

void Build(Node *curr)
{
	char c;

	cin >> curr->p;
	while ((c = getchar()) == ' ' || c == '\n');

	if (c == ')')
		return;

	ungetc(c, stdin);

	cin >> curr->dec;

	curr->c = new Node;
	curr->cd = new Node;

	while ((c = getchar()) == ' ' || c == '\n');
	Build(curr->cd);

	while ((c = getchar()) == ' ' || c == '\n');
	Build(curr->c);
	while ((c = getchar()) != ')');
}

int main()
{
	char c;
	int cn, n, l, a, i, j;
	string s;
	set<string> ch;
	Node *curr;
	long double ans;

	cout.setf(ios::fixed);
	cout.precision(7);
	cin >> n;

	for (cn = 1; cn <= n; cn++)
	{
		root = new Node;

		cin >> l;

		while ((c = getchar()) == ' ' || c == '\n');
		Build(root);

		cout << "Case #" << cn << ":\n";
		getline(cin, s);
		cin >> a;

		for (i = 0; i < a; i++)
		{
			ch.clear();
			cin >> s >> l;
			for (j = 0; j < l; j++)
			{
				cin >> s;
				ch.insert(s);
			}

			curr = root;
			ans = root->p;

			while (curr->c != NULL)
			{
				if (ch.find(curr->dec) != ch.end())
					curr = curr->cd;
				else
					curr = curr->c;
				ans *= curr->p;
			}

			cout << ans << endl;
		}

		delete root;
	}

	return 0;
}
