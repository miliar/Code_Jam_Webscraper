#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

struct tree_elem {
  vector <struct tree_elem*> *children;
  string *name;
} tree_elem;

int insert_path(struct tree_elem* node, string path)
{
				if (path.length() == 0)
								return 0;

				string rest = "";

				if (path.find_first_of("/") != string::npos)
				{
								rest = path.substr(path.find_first_of("/") + 1);
								path = path.substr(0, path.find_first_of("/"));
				}

				int idx = -1;

				for (size_t i = 0; i < node->children->size(); i++)
{
				if (*((*(node->children))[i]->name) == path)
idx = i; 
} 

				if (idx >= 0)
				{
								return insert_path((*(node->children))[idx], rest);
				}
				else 
				{
								struct tree_elem *n;
								n = (struct tree_elem *)malloc(sizeof(struct tree_elem));
                n->children = new vector<struct tree_elem*>();
								n->name = new string(path);
								node->children->push_back(n);
								return 1 + insert_path(n, rest);
				}
}



int main ()
{
				int t, n, m;
				struct tree_elem root;
        root.children = new vector<struct tree_elem*>();
        root.name = new string("");
				string path;
				cin >> t;
				for (int i = 0; i < t; i++)
				{
								cin >> n >> m;
								root.children->clear();
								for (int j = 0; j < n; j++)
								{
												cin >> path;
												insert_path(&root, path.substr(1));
								}
								int res = 0;
								for (int j = 0; j < m; j++)
								{
												cin >> path;
												res += insert_path(&root, path.substr(1));
								}
								cout << "Case #" << (i+1) << ": " << res << endl;
				}

	return 0;
}


