#include <vector>
#include <set>
#include <map>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <queue>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;i++)
#define FO(i,j,n) for(int i=j;i<n;i++)
#define FOX(i,x) for(int i=0;i<x.size();i++)
#define VI vector<int>
#define VB vector<bool>
#define VVI vector<vector <int> >
#define VS vector<string>
#define S(x) sort(x.begin(),x.end());
#define R(x) reverse(x.begin(),x.end());
#define PII pair<int,int>
#define X first
#define Y second
#define PB push_back
#define MP make_pair

typedef long long ll;
typedef long double ld;

int main()
{
  int t;
  cin>>t;
  int cnt=1;
  while(t--)
    {
      int n,m;
      cin>>n>>m;
      VVI inp;
      VI done(n,-1);
      bool good=true;
      FOR(i,m)
	{
	  int c;
	  cin>>c;
	  VI temp(2*c);
	  FOR(j,c)
	    {
	      cin>>temp[2*j]>>temp[2*j+1];
	      temp[2*j]--;
	    }
	  inp.PB(temp);
	}
      bool change=true;
      while(change)
	{
	  change=false;
	  FOR(i,m)
	    {
	      if(inp[i].size()==2)
		{
		  if(done[inp[i][0]]==-1)
		    {
		      done[inp[i][0]]=inp[i][1];
		      change=true;
		      FOR(j,m)
			{
			  if(inp[j].size()==2)
			    continue;
			  for(int k=0;k<inp[j].size();k+=2)
			    {
			      if(inp[j][k]==inp[i][0])
				{
				  if(inp[j][k+1]==done[inp[i][0]])
				    inp[j].clear();
				  else
				    {
				      inp[j].erase(inp[j].begin()+k);
				      inp[j].erase(inp[j].begin()+k);
				    }
				  break;
				}
			    }
			}
		      inp[i].clear();
		    }
		  else
		    {
		      if(done[inp[i][0]]!=inp[i][1])
			{
			  good=false;
			  break;
			}
		    }
		}
	    }
	}
      FOR(i,n)
	if(done[i]==-1)
	  done[i]=0;
      FOR(i,m)
	{
	  bool found=(inp[i].size()==0);
	  for(int j=0;j<inp[i].size();j+=2)
	    if(done[inp[i][j]]==inp[i][j+1])
	      {
		found=true;
		break;
	      }
	  if(!found)
	    {
	      good=false;
	      break;
	    }
	}
      cout<<"Case #"<<cnt++<<": ";
      if(!good)
	cout<<"IMPOSSIBLE"<<endl;
      else
	{
	  FOR(i,n-1)
	    cout<<done[i]<<" ";
	  cout<<done[n-1]<<endl;
	}
    }
  return 0;
}
