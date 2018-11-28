#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <string>
#include <set>
#include <stack>
using namespace std;

struct Node
{
	double weight;
	string feature;
	Node *left, *right;
}	nodes [1000000];

set<string> features;
stack<Node*> nstk; // node stack

stack<char> waitStk;

enum {
Wait_root_open, 
Wait_weight,
Wait_close_or_feature,
Wait_true_open,
Wait_true_close,
Wait_false_open,
Wait_false_close,
Wait_root_close };

char line [1024];
char buffer [1024];

int main()
{
	gets (line);
	int kase = atoi (line), serial = 0,
		nFeat, nNode;
	double p;

	char *token, ch;
	Node *ptr;
	bool built;

	string name;
	set<string>::iterator endItr;

	while (kase--)
	{
		//	start a test case

		gets (line);
		int L = atoi (line);

		nNode = 0;

		waitStk.push (Wait_root_open);
		built = false;

		//	parse and build tree
		while (L--) {
			gets (line);

			if (built) continue;

			token = strtok (line, " ");
			while (token)
			{
				if (token [0] == '(')
				{
					ptr = & (nodes [nNode++]); // new node
					ptr->left = ptr->right = NULL;
					ptr->feature = "";

					if (waitStk.top() == Wait_root_open) {
						waitStk.pop();
						waitStk.push (Wait_root_close);

					} else if (waitStk.top() == Wait_true_open) {
						waitStk.pop();
						waitStk.push (Wait_true_close);
						nstk.top()->right = ptr;

					} else { // if (waitStk.top() == Wait_false_open)
						waitStk.pop();
						waitStk.push (Wait_false_close);
						nstk.top()->left = ptr;
					}

					nstk.push (ptr);

					if (token [1] != '\0') {
						strcpy (buffer, token+1);
						strcpy (token, buffer);
						continue; // continue processing same token
					}

				} else if (isalpha (token [0])) {
					ptr = nstk.top();
					ptr->feature = token;
					waitStk.push (Wait_true_open);

				} else if (isdigit (token [0])) {
					ptr = nstk.top();
					ptr->weight = atof (token);

					for (int i=1; (ch = token [i]); ++i) {
						if (!isdigit (ch) && ch != '.') {
							strcpy (buffer, token + i);
							strcpy (token, buffer);

							ch = -1; // signal to continue processing same token
							break;
						}
					}

					if (ch == -1) {
						continue; // continue processing same token
					}

				} else if (token [0] == ')') {

					if (waitStk.top() == Wait_true_close) {
						waitStk.pop();
						waitStk.push (Wait_false_open);

					} else if (waitStk.top() == Wait_false_close) {
						waitStk.pop();

					} else if (waitStk.top() == Wait_root_close) {
						built = true;
					}

					nstk.pop();

					if (token [1] != '\0') {
						strcpy (buffer, token+1);
						strcpy (token, buffer);
						continue; // continue processing same token
					}
				}

				token = strtok (NULL, " ");
			}


			//	process line
		}

		gets (line);
		int A = atoi (line); // number of queries/animals

		printf ("Case #%d:\n", ++serial);

		while (A--) {
			//	start a query
			features.clear();

			gets (line);

			token = strtok (line, " ");
			name = token;

			//	parse list of features
			token = strtok (NULL, " ");
			nFeat = atoi (token);
			for (int i=0; i<nFeat; ++i) {
				token = strtok (NULL, " ");
				features.insert (string (token));
			}

			endItr = features.end(); // cache

			ptr = nodes; // root
			p = 1; // probability

			//	traverse the tree
			while (ptr ) {
				p *= ptr->weight;

				if (ptr->feature.length() == 0) break;
				if (features.find (ptr->feature) != endItr)
					ptr = ptr->right; // matched feature
				else
					ptr = ptr->left;
			}

			printf ("%.7lf\n", p);
			//	end a query
		}

		//	end a test case
	}
	return 0;
}