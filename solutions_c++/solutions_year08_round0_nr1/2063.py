#include <iostream>
#include <map>
#include <vector>
#define MAX 123

using namespace std;

int main(int argc, char *argv[]){

  int n, s, q, c = 1;
  string name;
  map <string, int> m;
  vector <int> used;
  scanf("%d",&n);
  
  while(n--)
    {
      int num_switches = 0;

      scanf("%d\n",&s);
      m.clear();
      
      for(int i = 0; i < s; i++)
	{
	  getline(cin, name);
	  m[name] = i;
	  // cout << "[" << name << "]" << endl;
	}	
      
      used.clear(); used.resize(s);
      int num_used = 0;
      scanf("%d\n",&q);
      
      for(int i = 0; i < q; i++)
	{
	  getline(cin, name);
	  
	  if(m.find(name) != m.end())
	    {
	      if(used[m[name]] == 0)
		{
		  used[(m[name])] = 1;
		  num_used++;
		}
	      
	      if(num_used == s)
		{
		  num_switches++;
		  used.clear(); used.resize(s);
		  num_used = 1;
		  used[(m[name])] = 1;
		}
	    }
	  
	  // 	  if(m.find(name) != m.end()) 
	  // 	    printf("achei: %d\n",m[name]);
	  // 	  else printf("nao achou\n");
	  // 	  cout << "[" << name << "]" << endl;
	}	

      
      printf("Case #%d: %d\n",c++, num_switches);
    }
  
  return 0;
}
