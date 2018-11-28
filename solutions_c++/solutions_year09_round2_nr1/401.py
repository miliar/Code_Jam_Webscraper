/*
 *  Google Code Jam 2009
 *  Round 1B - Problem A - Decision Tree
 */


#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <list>

#define INPUT_FILE		"input.txt"
#define OUTPUT_FILE		"output.txt"

using namespace std;


int N, L, A;
double Rez;
struct tree
{
  double p;
  char s[16];

  tree *l, *r;
}*Tree;
vector<string> Features;


tree* ParseTree()
{
  tree *node;
  char ch;
  char s[32];
  

  while (true)
  {
    scanf("%c", &ch);
    if (ch == ' ' || ch == '\n')
	continue;
    if (ch == '(')
	break;
  }

  node = new tree;


  scanf("%lf", &node->p);
  strcpy(node->s, "");
  node->l = node->r = NULL;

  scanf("%s", node->s);

  int right = 0;
  if (node->s[0] == ')')
    {
      node->s[0] = 0;
      right = 1;
    }

  if (!right)
  {
    node->l = ParseTree();
    node->r = ParseTree();

    while (true)
      {
	scanf("%c", &ch);
	if (ch == ' ' || ch == '\n')
	  continue;
	if (ch == ')')
	  break;
      }
  }

  return node;
}

void Recurse(tree *node)
{
  int i, ok;

  if (!node)
    return;

  Rez *= node->p;

  ok = 0;
  for (i = 0; i < Features.size(); i++)
    if (!strcmp(Features[i].c_str(), node->s))
      {
	ok = 1;
	break;
      };

  if (ok)
    Recurse(node->l);
  else
    Recurse(node->r);
}


int main()
{
  int i, j, k, d;
  char s[1024];

  freopen(INPUT_FILE, "rt", stdin);
  freopen(OUTPUT_FILE, "wt", stdout);

  scanf("%d\n", &N);

  for (i = 0; i < N; i++)
  {
    scanf("%d\n", &L);

    Tree = ParseTree();

    printf("Case #%d:\n", i + 1);

    scanf("%d", &A);

    for (j = 0; j < A; j++)
      {
	scanf("%s", &s);
	scanf("%d ", &d);

	Features.clear();
	for (k = 0; k < d; k++)
	  {
	    scanf("%s", &s);
	    Features.push_back(s);
	  }

	Rez = 1;
	Recurse(Tree);
	printf("%.7lf\n", Rez);
      }

    Tree = NULL;
  }

  fclose(stdout);
  fclose(stdin);

  return 0;
}
