/*
	2010-05-22 Google Code Jam Round 1B Question A
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
using namespace std;

struct Node {
	map<string, Node*> ctx;
}	nodes [21000];
int n_nodes;

char line [1024];
int main()
{
	int kase, serial=0,
		n, m, mkdir;

	Node *ptr;
	map<string, Node*>::iterator itr;
	string dir_name;

	gets (line);
	kase = atoi (line);
	while (kase--)
	{
		// BEGIN test case
		gets (line);
		sscanf (line, "%d %d", &n, &m);
		mkdir = 0;

		n_nodes = 1;
		nodes[0].ctx.clear();

		while (n--) {
			gets (line);

			ptr = nodes; // root
			for (char *ch=line+1; *ch; ++ch) {
				if (*ch == '/') continue;

				dir_name = "";
				do {
					dir_name = dir_name + *ch++;
				}
				while (*ch && (isalpha(*ch) || isdigit(*ch)));

				itr = ptr->ctx.find(dir_name);
				if (itr == ptr->ctx.end()) { // make new dir
					nodes[n_nodes].ctx.clear();
					ptr = ptr->ctx[dir_name] = &(nodes[n_nodes++]);
				}
				else
					ptr = itr->second;

				if (! *ch) break;
			}
		}
		while (m--) {
			gets (line);

			ptr = nodes; // root
			for (char *ch=line+1; *ch; ++ch) {
				if (*ch == '/') continue;

				dir_name = "";
				do {
					dir_name = dir_name + *ch++;
				}
				while (*ch && (isalpha(*ch) || isdigit(*ch)));

				itr = ptr->ctx.find(dir_name);
				if (itr == ptr->ctx.end()) { // make new dir
					++mkdir;
					nodes[n_nodes].ctx.clear();
					ptr = ptr->ctx[dir_name] = &(nodes[n_nodes++]);
				}
				else
					ptr = itr->second;

				if (! *ch) break;
			}
		}

		printf ("Case #%d: %d\n", ++serial, mkdir);
		// END test case
	}
	return 0;
}
