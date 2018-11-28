#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <sstream>
using namespace std;

int main()
{
  int n,s,q,x,i,j,cntr,y,tmp;
  string query;
  istringstream sin;
  getline(cin,query);
  sin.clear();
  sin.str(query);
  sin>>n;
  for(x=1;x<=n;x++)
    {
      map <string, int> m;
      getline(cin,query);
      sin.clear();
      sin.str(query);
      sin>>s;
      //    cout<<s<<"\n";
      for(i=0;i<s;i++)
	{
	  getline(cin,query);
	  //  cout<<query<<"\n";
	  m[query]=i;
	}
      vector <int> stat(s);
      getline(cin,query);
      sin.clear();
      sin.str(query);
      sin>>q;
      y=0;cntr=0;
      for(i=0;i<q;i++)
	{
	  getline(cin,query);
	  tmp=m[query];
	  if(!(stat[tmp]))
	    {
	      cntr++;
	      stat[tmp]=1;
	      if(cntr==s)
		{
		  //cout<<"switch made at query "<<i+1<<"\n";
		  y++;
		  cntr=1;
		  for(j=0;j<s;j++)
		    stat[j]=0;
		  stat[tmp]=1;
		}
	    }
	}
      cout<<"Case #"<<x<<": "<<y<<"\n";
    }
  return 0;
}
