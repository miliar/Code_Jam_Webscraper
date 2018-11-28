#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cerrno>

#include <string>

#include <vector>
#include <map>
#include <algorithm>

using namespace std;

#define CHECK(A, B) if( (A) == (B) ) { printf("error: %s at line %d\n", strerror(errno), __LINE__); }

int 		gi(void) { int a; scanf("%d",&a); return a; }
float		gf(void) { double a; scanf("%lf", &a); return a; }
char 		gc(void) { char a; scanf("%c", &a); return a; }
string		gs(void) { char buf[1024]; scanf("%s", buf); return string(buf); }


int main(int argc, char **argv)
{
	FILE *inf, *ouf;
	
	inf = freopen("input.txt", "r", stdin);
	ouf = freopen("output.txt", "w", stdout);
	
	CHECK(inf, NULL);
	
	int n = gi();
	
	for(int i = 0; i < n; i++)
	{
	  int t = gi();
	  int s = gi();
	  int p = gi();
	  
	  int almost = 0;
	  
	  int res = 0;
	  
	  vector<int> vi;
	  vector<int> vj;
	  
	  for(int j = 0; j < t; j++)
	  {
	    int ti = gi();
	    
	    if(0 == ti%3)
	    {
	      vi.push_back(ti/3);
	    }
	    else
	    {
	      vi.push_back((ti+(3-(ti%3)))/3);
	    }
	    
	    vj.push_back(ti);
	  }
	  
	  for(int j = 0; j < vi.size(); j++)
	  {
	    if(vi[j] >= p)
	    {
	      res++;
	    }       
	  }
	  
	  for(int j = 0; j < vi.size(); j++)
	  {
	    if(vj[j] != 0)
	    {
	      if(0 == ( (vj[j]-vi[j])%2) && (0 != vj[j]%vi[j]))
	      {
		continue;
	      }
	    }
	    
	    if(vj[j] >= p && 1 == (p - vi[j]) )
	    {
	      almost++;
	    }
	  }
	  
	  if(almost >= s)
	  {
	    res += s;
	  }
	  else
	  {
	    res += almost;
	  }
	  
	  printf("Case #%d: %d\n", (i+1), res); 
	}
	
	return 0;
}
