#include <iostream>
#include <vector>
#include <string>
#include <set>

#define FORR(x,a,b) for(int x=a;x<b;++x)
#define FORE(x,a) for(typeof((a).begin()) x=(a).begin(); x!=(a).end(); ++x)
#define BE(a) (a).begin(),(a).end()

using namespace std;

typedef vector<string> VS;
typedef VS::iterator VSIt;

typedef vector<int> VI;
typedef VI::iterator VII;
typedef set<int> SI;
typedef vector<SI> VSI;

int process(istream &source)
{
  string sear,que,skipLine;
  VS eng,quer;

  cerr<<"process begin"<<endl;

  int ny;//number of engines
  cin>>ny;
  getline(cin,skipLine);
  FORR(t,0,ny)
    getline(cin,sear),
    eng.push_back(sear);

  int nx;//number of queries
  cin>>nx;  
  getline(cin,skipLine);
  FORR(t,0,nx)
    getline(cin,que),
    quer.push_back(que);

  cerr<<"engines queries = "<<ny<<" "<<nx<<endl;
  if(nx==0){cerr<<"no querries, no switches"<<endl; return 0;}
  
  VI cur(ny,0),next,infty;

  FORR(t,0,nx-1)
    {
      next=VI(ny,0);
      infty=VI(ny,1);
      FORR(p,0,ny)
	if(eng[p]!=quer[t])
	  FORR(q,0,ny)
	    if(eng[q]!=quer[t+1])
	      {
		int cost=0;
		if(p==q)
		  cost=cur[p];
		else
		  cost=cur[p]+1;
		if(infty[q]==1){next[q]=cost;infty[q]=0;}
		else 
		  if(cost<next[q])
		    next[q]=cost;
	      }
      cerr<<"iteration "<<t+1<<"\t";
      FORR(q,0,ny)if(infty[q]==1) cerr<<"i"; else cerr<<next[q];cerr<<endl;
      cur=next;
    }

  bool flag=true;
  int ret=0;
  FORR(q,0,ny)
    if(infty[q]!=1)
      if(flag)
	{
	  flag=false;
	  ret=cur[q];
	}
      else
	{
	  ret=min(ret,cur[q]);
	}
  cerr<<"number of switches is "<<ret<<endl<<endl;
  return ret;    
}

int main()
{
  int n;
  cin>>n;
  FORR(t,0,n)
    {
      cerr<<"Begin to process "<<(t+1)<<" case"<<endl;
      cout<<"Case #"<<(t+1)<<": "<<process(cin)<<endl;      
    }
  
  return 0;
}
 
