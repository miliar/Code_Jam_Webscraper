#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;


struct Node
{
	string f;
	double w;

	Node* child[2];

	Node()
	{
		child[0] = NULL;
		child[1] = NULL;
		f.clear();
	}
};

int N;
int L;
set <string> ft;

void Scan(Node *node)
{
	double d;
	string s;
	char c = '#';

	cin >> d;

	node->w = d;

	while( true )
	{
		cin >> c;

		if( c >= 'a' && c <= 'z' )
		{
			cin.putback( c );
			cin >> s;
			break;
		}
		if( c == ')' )
			return;
	}

	node->f = s;

	for(int i = 0; i < 2; i++)
	{
		c = '#';
		while( c != '(' )
			cin >> c;
		
		node->child[i] = new Node();

		Scan( node->child[i] );
	}

	c = '#';
	while( c != ')' )
		cin >> c;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> N;

	Node* root;
	string s;
	int n;

	cout.precision(8);

	for(int i = 0; i < N; i++)
	{
		root = new Node();

		cin >> n;

		cout << "Case #" << i+1 << ":\n";

		char c = '#';

		while( c != '(' )
			cin >> c;

		Scan(root);

		cin >> L;

		for(int j = 0; j < L; j++)
		{
			cin >> s;
			cin >> n;

			ft.clear();
			for(int k = 0; k < n; k++)
			{
				cin >> s;
				ft.insert( s );
			}

			Node* cur = root;

			double ans = 1;
			while( true )
			{
				ans *= cur->w;

				if( cur->f.empty() )
					break;

				if( ft.find( cur->f ) != ft.end() )
				{
					cur = cur->child[0];
				}
				else
					cur = cur->child[1];
			}

			cout << fixed << ans << endl;
		}
	}

	return 0;
}