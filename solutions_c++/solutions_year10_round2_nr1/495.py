#include <set>
#include <string>
#include <cstdio>

using namespace std;

int main(void)
{
  int t, c = 1, n, m, add, i, j;
  char p[128];
  string s;
  set<string> dk;
  
  scanf("%d", &t);
  
  while(c <= t)
  {
    add = 0;
    dk.clear();
    
    scanf("%d %d", &n, &m);
    
    for(i = 0; i < n; i++)
    {
      scanf(" %s", p);
      
      s.erase();
      s.push_back('/');
      
      for(j = 1; p[j] != 0; j++)
      {
	if(p[j] == '/')
	{
	  dk.insert(s);
	}
	s.push_back(p[j]);
      }
      dk.insert(s);
    }

    for(i = 0; i < m; i++)
    {
      scanf(" %s", p);
      
      s.erase();
      s.push_back('/');
      
      for(j = 1; p[j] != 0; j++)
      {
	if(p[j] == '/')
	{
	  if(dk.find(s) == dk.end())
	  {
	    add++;
	    dk.insert(s);
	  }
	}
	s.push_back(p[j]);
      }
      
      if(dk.find(s) == dk.end())
      {
	add++;
	dk.insert(s);
      }      
      
    }
    
    
    printf("Case #%d: %d\n", c++, add);
  }
  
  
  
  
  
  
  return 0;
}