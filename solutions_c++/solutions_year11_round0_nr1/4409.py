#include <iostream>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main()
{
  int t, tc, n, op, poso, posb, to, tb;
  char c;
  
  cin>>t;
  
  for(tc=1;tc<=t;tc++)
  {
    poso = posb = 1;
    to = tb = 0;
    
    cin>>n;
    while(n--)
    {
      cin>>c>>op;
      
      if(c=='O')
      {
        if(tb>to)
        {
          poso += op>poso?min(abs(op-poso),tb-to):-min(abs(op-poso),tb-to);
          to = tb;
        }
        to += abs(op-poso);
        poso = op;
        to++;
      }
      else
      {
        if(to>tb)
        {
          posb += op>posb?min(abs(op-posb),to-tb):-min(abs(op-posb),to-tb);
          tb = to;
        }
        tb += abs(op-posb);
        posb=op;
        tb++;
      }
    }
    
   cout<<"Case #"<<tc<<": "<<max(to,tb)<<endl;
  }
}
