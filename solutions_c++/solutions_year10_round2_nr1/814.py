#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
class node;

class node
{public:
  vector< node > subDir;
  string name;
  
};


void PrintTree(node *t,string s)
{
  if(t!=NULL)
    cout<<s<<t->name<<endl;
  for(int i=0;i<t->subDir.size();i++)
    PrintTree(&(t->subDir[i]),s+"   ");
}

int Answer()
{
  int n,m;
  node root,*current,temp;
  string input,dirName;
  cin>>n>>m;
  for(int i=0;i<n;i++)
    {
      cin>>input;
      input=input+'/';
      int last=1;
      current=&root;
      //cout<<"Processing : "<<input<<endl;
      for(int j=1;j<input.size();j++)
	{if(input[j]=='/')
	    {dirName=input.substr(last,j-last);
	      //      cout<<"Tocken "<<dirName<<endl;
	      last=j+1;
	      int k;
	      int size=(*current).subDir.size();
	      for(k=0;k<size;k++)
		{if(dirName==((*current).subDir[k].name))
		    { current=&((*current).subDir[k]);
		      break;
		    }
		}
	      if(k>=size)
		{
		  temp.name=dirName;
		  temp.subDir.clear();
		  (*current).subDir.push_back(temp);
		  current=&(*current).subDir[current->subDir.size()-1];
		}
	    }
	}

      
    }
  

  //  PrintTree(&root,"");
  


  int ans=0;

  for(int i=0;i<m;i++)
    {
      cin>>input;
      input=input+'/';
      int last=1;
      current=&root;
      //  cout<<"Processing : "<<input<<endl;
      for(int j=1;j<input.size();j++)
	{if(input[j]=='/')
	    {dirName=input.substr(last,j-last);
	      //      cout<<"Tocken "<<dirName<<endl;
	      last=j+1;
	      int k;
	      int size=(*current).subDir.size();
	      for(k=0;k<size;k++)
		{
		  if(dirName==((*current).subDir[k].name))
		    { current=&((*current).subDir[k]);
		      //      cout<<"moovin "<<dirName<<endl;
		      break;
		    }
		}
	      if(k>=size)
		{
		  temp.name=dirName;
		  temp.subDir.clear();
		  (*current).subDir.push_back(temp);
		  current=&(*current).subDir[current->subDir.size()-1];
		  ans++;
		  //cout<<"New created "<<dirName<<endl;
		}
	    }
	}
      
    }
  
  return ans;
}

int main()
{
  int noCase,cases;
  cin>>cases;
  for(noCase=1;noCase<=cases;noCase++)
    {
      
      
      
      cout<<"Case #"<<noCase<<": "<<Answer()<<endl;
    }
  
}
