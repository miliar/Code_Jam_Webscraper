#include<cstdio>
#include<vector>
using namespace std;
vector <pair <int, int> > V;
int f,s;
void doo (int x)
{
  if (x%3==0)
  {
    f=x/3;
    s=x/3+1;
  }
  if (x%3==1)
  {
    f=x/3+1;
    s=x/3+1;
  }
  if (x%3==2)
  {
    f=x/3+1;
    s=x/3+2;
  }
  if (x==0)
  {
    f=0;
    s=0;
  }
  V.push_back(make_pair (f,s));
}
int main ()
{
  int t;
  scanf ("%d", &t);
  for (int cas=1; cas<=t; cas++)
  {
    int star,lim,n;
    scanf ("%d %d %d",  &n,&lim,&star);
    while (n--)
    {
      int x;
      scanf ("%d", &x);
      doo(x);
    }
    int w=0;
    for (int i=0; i<V.size(); i++)
    {
      int ff=V[i].first;
      int ss=V[i].second;
      if (ff>=star) w++;
      else
	if (ss>=star && lim>0)
	{
	  w++;
	  lim--;
	}
    }
    printf ("Case #%d: %d\n", cas,w);
    V.clear();
  }
return 0;
}
