#include <iostream>
#include <set>
#include <stdio.h>

using namespace std;

int main()
{
  int T, t;
  int M, m;
  int N, n;
  string a;
  
  set<string> s;
  set<string>::iterator it;
  
  cin>>T;  
  for (t=0; t<T; ++t)
  { 
    int c = 0;
    cin>>N>>M;
    for (n=0; n<N; ++n)
    {
      cin>>a;
      s.insert(a);          
    }
    
    for (m=0; m<M; ++m)
    {
      cin>>a;
      while ((it = s.find(a)) == s.end())
      {
        int p = a.find_last_of("/");
        if (p < 0)
          break;
        ++c;
        s.insert(a);
        a.erase(p);
      }
      
      a.clear();
    }

    s.clear();
    cout<<"Case #"<<t+1<<": "<<c<<endl;
    
  }
  return 0;

}
