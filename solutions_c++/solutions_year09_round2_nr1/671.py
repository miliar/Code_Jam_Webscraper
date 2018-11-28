#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <set>
using namespace std;

struct node {
 string text;
 double weight;
 node *left;
 node *right;
 
 node() { }
 node(string text, double weight) : text(text), weight(weight) { }
};

set <string> has;

string name;

void construct(node* &cur, string inp)
{
 //cout << inp << endl;
 while (inp[0] != '(')
  inp.erase(inp.begin());
  
 inp.erase(inp.begin());
 
 while (inp[inp.size() - 1] != ')')
  inp.erase(inp.begin() + inp.size() - 1);
 
 inp.erase(inp.begin() + inp.size() - 1);
 
 double w;
 stringstream z(inp); z >> w;
  
 cur -> weight = w; 
 
 if (inp.find('(') == string::npos)
  return;
 
 string fe; z >> fe;
 cur -> text = fe;
 string rem = inp.substr(inp.find('('));
 
 string sl = "(";
 
 int diff = 1;
 for (int i = 1; i < rem.size(); i++)
 {
  if (rem[i] == '(') diff++; else
  if (rem[i] == ')') diff--;
  sl += rem[i];
  if (!diff)
  {
   rem = rem.substr(i + 1);
   break;
  }
 }
 
 node* theL = new node;
 theL -> left = NULL;
 theL -> right = NULL;
 
 node* theR = new node;
 theR -> left = NULL;
 theR -> right = NULL;
 
 construct(theL, sl);
 construct(theR, rem);
 
 cur -> left = theL;
 cur -> right = theR;
}

double solve(node* &cur)
{
 //a leaf
 if (cur -> left == NULL && cur -> right == NULL)
  return cur -> weight;
  
 if (has.count(cur -> text))   
  return cur -> weight * solve(cur -> left);
 else
  return cur -> weight * solve(cur -> right);
}

node* root;

int main()
{
 int T;
 scanf("%d", &T);
 
 for (int t = 0; t < T; t++)
 {
  string tot = "";
  root = new node();
  root -> left = NULL;
  root -> right = NULL;
  
  int L;
  scanf("%d\n", &L);
  
  string curL;
  for (int i = 0; i < L; i++)
  {
   getline(cin, curL);   
   tot += curL;
  }
  
  construct(root, tot);
  
  printf("Case #%d:\n", t + 1);
  
  int A;
  scanf("%d", &A); 
  for (int a = 0; a < A; a++)
  {
   has.clear();
   int nf; 
   cin >> name >> nf;   
   
   for (int f = 0; f < nf; f++)
   {
    string curA; cin >> curA;
    has.insert(curA);
   }
   
   printf("%.8lf\n", solve(root));
  }
 }
 
 return 0;
}
