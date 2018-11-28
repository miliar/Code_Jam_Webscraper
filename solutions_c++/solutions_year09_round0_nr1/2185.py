#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;i++)
#define FOX(i,x) for(int i=0;i<x.size();i++)
#define PB push_back

vector<string> tok(string a)
{
  vector<string> ret;
  bool in=false;
  string temp;
  FOX(i,a)
    {
      if(a[i]!='(')
	{
	  if(!in)
	    ret.PB(a.substr(i,1));
	  else
	    {
	      if(a[i]==')')
		{
		  in=false;
		  ret.PB(temp);
		  temp="";
		}
	      else
		temp+=a[i];
	    }
	}
      else
	in=true;
    }
  return ret;
}

vector<string> inp;
int n,l,d;

bool match(char a, string b)
{
  FOX(i,b)
    if(b[i]==a)
      return true;
  return false;
}

int ret(vector<string> a)
{
  int res=0;
  FOR(i,d)
    {
      bool good=true;
      FOR(j,l)
	{
	  if(!match(inp[i][j],a[j]))
	    {
	      good=false;
	      break;
	    }
	}
      if(good)
	res++;
    }
  return res;
}

int main()
{
  cin>>l>>d>>n;
  inp.clear();
  FOR(i,d)
    {
      string temp;
      cin>>temp;
      inp.PB(temp);
    }
  FOR(i,n)
    {
      string a;
      cin>>a;
      printf("Case #%d: %d\n",i+1, ret(tok(a)));
    }
  return 0;
}
