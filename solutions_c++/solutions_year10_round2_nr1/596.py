#include <iostream>
#include <string>
using namespace std;

struct node {
  string name;
  int n;
  node* child[100];
};

node* create_node(string name) {
  node* n = new node;
  n->name = name;
  n->n = 0;
  return n;
}

void delete_tree(node *ptr)
{
  int i;
  for(i=0;i<ptr->n;i++)
    delete_tree(ptr->child[i]); 
  delete ptr;
}

int main()
{
  int T,tcase;
  cin>>T;
  for(tcase=1;tcase<=T;tcase++)
    {
      int N,M,i,ans=0;
      cin>>N>>M;
      node* root = create_node("");
      for(i=0;i<N;i++)
	{
	  int j;
	  node *curnode = root;
	  string s,name;
	  cin>>s;
	  for(j=1;j<=s.size();j++)
	    {
	      int k;
	      if((s[j]=='/')||(j==s.size()))
		{
		  for(k=0;k<curnode->n;k++)
		    if(curnode->child[k]->name == name)
		      break;
		  if(k==curnode->n)
		    curnode->child[(curnode->n)++]=create_node(name);
		  curnode=curnode->child[k];
		  name="";
		}
	      else
		name+=s[j];
	    }
	}
      for(i=0;i<M;i++)
	{
	  int j;
	  node *curnode = root;
	  string s,name;
	  cin>>s;
	  for(j=1;j<=s.size();j++)
	    {
	      int k;
	      if((s[j]=='/')||(j==s.size()))
		{
		  for(k=0;k<curnode->n;k++)
		    if(curnode->child[k]->name == name)
		      break;
		  if(k==curnode->n)
		    {
		      //     cout<<"creating "<<name<<"\n";
		      ans++;
		      curnode->child[(curnode->n)++]=create_node(name);
		    }
		  curnode=curnode->child[k];
		  name="";
		}
	      else
		name+=s[j];
	    }
	}
      cout<<"Case #"<<tcase<<": "<<ans<<"\n";
      delete_tree(root);
    }
    return 0;
}
