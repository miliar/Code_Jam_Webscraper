#include <iostream>
#include <vector>

using namespace std;

int t,n;
int a[1000];

int add(int x,int y)
{
  string g="",h="";
  while (x)
  {
    if (x%2) g=g+"1";
    else
      g=g+"0";
    x/=2;
  }
  h=g;
  x=y;
  g="";
  while (x)
  {
    if (x%2) g=g+"1";
    else
      g=g+"0";
    x/=2;
  }
  cout<<g<<' '<<h<<endl;
  while (h.size()<g.size())
    h=h+"0";
  while (g.size()<h.size())
    g=g+"0";
  //cout<<g<<' '<<h<<endl;
  string z="";
  for (int i=0;i<g.size();i++)
    if (g[i]==h[i])
      z=z+"0";
  else z=z+"1";
  //cout<<z<<endl;
}

string bib(int x)
{
  string g="",h="";
  while (x)
  {
    if (x%2) g=g+"1";
    else
      g=g+"0";
    x/=2;
  }
  return g;
}

string add (string g, string h)
{
  //cout<<g<<' '<<h<<endl;
  while (h.size()<g.size())
    h=h+"0";
  while (g.size()<h.size())
    g=g+"0";
  //cout<<g<<' '<<h<<endl;
  string z="";
  for (int i=0;i<g.size();i++)
    if (g[i]==h[i])
      z=z+"0";
    else z=z+"1";
  //cout<<z<<endl;
  return z;
}

int mmm;

void dfs(string s)
{
 // cout<<s.size()<<' '<<n<<endl;
  if (s.size()==n)
  {
    int as=0,bs=0;
    string ab="0",bb="0";
    for (int i=0;i<n;i++)
    {
      if (s[i]=='0')
      {
        as+=a[i];
        ab=add(ab,bib(a[i]));
      }
      else
      {
        bs+=a[i];
        bb=add(bb,bib(a[i]));
      }
    }
    while (ab.size()<bb.size())
      ab=ab+"0";
    while (ab.size()>bb.size())
      bb=bb+"0";
   // cout<<s<<' '<<as<<' '<<bs<<' '<<ab<<' '<<bb<<endl;
    if (ab==bb)
    {
      if (mmm<as&&bs!=0)
        mmm=as;
      if (mmm<bs&&as!=0)
        mmm=bs;
    }
    return;
  }
  dfs(s+"1");
    dfs(s+"0");
  return;
}


int main()
{
  //add(50,10);
 //int t,n;
  cin>>t;
  for (int i=1;i<=t;i++)
  {
    mmm=-1;
    cin>>n;
    for (int j=0;j<n;j++)
      cin>>a[j];
    
    dfs("");
    
    cout<<"Case #"<<i<<": ";
    if (mmm<0)
      cout<<"NO\n";
    else
      cout<<mmm<<endl;
    
  }
  return 0;
}