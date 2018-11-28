#include <cstdio>
#include <cstring>

using namespace std;

const int childCnt = 26;

class WTree
{
	public:
		WTree(): root(new Node(false)) {}
		~WTree()
		{
			delete root;
		}

		void addWord(const char* s)
		{
			insert(s, root);
		}

		int matchCount(const char* pattern)
		{
			return count(pattern, root);
		}

	private:
		struct Node
		{
			Node* child[childCnt];
			bool leaf;

			Node(bool isLeaf = false): leaf(isLeaf)
			{
				memset(child, 0, sizeof(child));
			}

			~Node()
			{
				for (int i = 0; i < childCnt; ++i)
					delete child[i];
			}
		};

		void insert(const char* what, Node* where)
		{
			if (!*what)
			{
				where->leaf = true;
			}
			else
			{
				Node** child = where->child + (*what - 'a');

				if (!*child)
				{
					*child = new Node(false);
				}

				insert(what + 1, *child);
			}
		}

		int count(const char* pattern, Node* where)
		{
			if (!where)
			{
				return 0;
			}
			else if (!*pattern && where->leaf)
			{
				return 1;
			}
			else
			{
				if (*pattern == '(')
				{
					int cnt = 0;
					const char* end;
					for (end = pattern + 1; *end != ')'; ++end)
						;

					for (const char* p = pattern + 1; p != end; ++p)
						cnt += count(end + 1, where->child[*p - 'a']);

					return cnt;
				}
				else
				{
					return count(pattern + 1, where->child[*pattern - 'a']);
				}
			}
		}

		Node* root;
};

int main()
{
	int l, d, n;
	WTree t;

	scanf("%d %d %d", &l, &d, &n);

	const char* buf = new char[l+1];

	for (int i = 0; i < d; ++i)
	{
		scanf("%s", buf);
		t.addWord(buf);
	}

	delete buf;

	buf = new char[28 * l + 1];

	for (int i = 1; i <= n; ++i)
	{
		scanf("%s", buf);
		printf("Case #%d: %d\n", i, t.matchCount(buf));
	}

	delete buf;

	return 0;
}
