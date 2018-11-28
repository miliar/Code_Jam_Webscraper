#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <istream>
#include <string>

using namespace std;

struct ft_node
{
  double weight;
  string feature;
  ft_node *left, *right;

  ft_node()
    : weight(0.0), 
      feature(""), 
      left(NULL), 
      right(NULL)
  { }

};



void
get_character(std::istream &in, char to_get)
{
  char ch = in.get();
  while (in && ch != to_get)
    {
      ch = in.get();
    }
}

bool
has_alpha(std::istream &in)
{
  char ch = in.get();
  while (in && isspace(ch))
    {
      ch = in.get();
    }
  if (in)
    {
      in.putback(ch);
      return isalpha(ch);
    }
  return false;
}


ft_node *
parse_feature_tree()
{
  get_character(cin, '(');
  ft_node *p = new ft_node;
  cin>>p->weight;
  if (has_alpha(cin))
    {
      cin>>p->feature;
      p->left = parse_feature_tree();
      p->right = parse_feature_tree();
    }
  get_character(cin, ')');
  return p;
}


void
print_feature_tree(ft_node *p, int tab)
{
  if (!p)
    return;

  for (int i = 0; i < tab; ++i)
    {
      cerr<<"\t";
    }

  cerr<<p->weight<<", "<<p->feature<<endl;
  print_feature_tree(p->left, tab+1);
  print_feature_tree(p->right, tab+1);
}


double
how_cute(ft_node *p, map<string, int> features)
{
  if (p->feature.size() == 0)
    {
      return p->weight;
    }

  if (features[p->feature] == 1)
    {
      return p->weight * how_cute(p->left, features);
    }
  else
    {
      return p->weight * how_cute(p->right, features);
    }
}


int
main()
{
  int t = 0;
  cin>>t;
  for (int i = 0; i < t; ++i)
    {
      int ft_lines;
      cin>>ft_lines;

      ft_node *p = parse_feature_tree();
      print_feature_tree(p, 0);

      int cases;
      cin>>cases;
      cout<<"Case #"<<i+1<<":\n";
      
      for (int j = 0; j < cases; ++j)
	{
	  string creature;
	  int n_features;
	  cin>>creature>>n_features;
	  map<string, int> features;
	  for (int k = 0; k < n_features; ++k)
	    {
	      string f;
	      cin>>f;
	      features[f] = 1;
	    }
	  printf("%0.7f\n", how_cute(p, features));
	}

    }
}
