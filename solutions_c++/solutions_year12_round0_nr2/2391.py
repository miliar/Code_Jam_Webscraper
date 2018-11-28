#include <iostream>
using namespace std;

int p,s,g,v,s2,bs;

bool can_goal(int n)
{
  int p = n/3;
  int r = n%3;
  if(p >= g)
    return true;
  if(p+1>=g)
  {
    if(r==0 && p>0 && s>0)
    {
      --s;
      return true;
    }
    else if(r==1 || r==2)
      return true;
    return false;
  }
  if(p+2>=g)
  {
    if(r==2 && s>0)
    {
      --s;
      return true;
    }
    return false;
  }
  return false;
}

int main()
{
  int t;
  cin >> t;
  for(int i=0;i<t;i++)
  {
    cin >> p >> s >> g;
    s2 = bs = 0;
    int c = 0;
    for(int k=0;k<p;k++)
    {
      cin >> v;
      if(can_goal(v))
        c++;
    }
    
    cout << "Case #" << i+1 << ": " << c << endl;
  }
}
