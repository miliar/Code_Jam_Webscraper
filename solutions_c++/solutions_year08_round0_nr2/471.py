#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <cmath>
#include <queue>

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

int needForStation(VI& dep,VI&arriv,int ta)
{
  queue<int> dat;
  FORE(itx,arriv)
    dat.push(*itx+ta);//when loco will be ready

  int ret=0;
  FORE(itx,dep)
    {
      if(!dat.empty())
	if(dat.front()<=*itx)
	  {dat.pop();continue;}
      ++ret;
    }
  cerr<<endl;
  return ret;
}

void process(istream &source,ostream& dest)
{
  int tatime,a2b,b2a;
  cin>>tatime>>a2b>>b2a;
  cerr<<"we have trains with "<<tatime<<" turnaround time"<<endl;
  cerr<<"they must have "<<a2b<<" trips from a to b and "<<b2a<<" trips from b to a"<<endl;
  
  VI aArriv,aDep,bArriv,bDep;

  FORR(t,0,a2b)
    {
      int hh,mm;
      char delim;
      source>>hh>>delim>>mm;
      int inMinutes=hh*60+mm;
      cerr<<"aDep = "<<hh<<":"<<mm<<" in minutes ="<<inMinutes<<endl;
      aDep.push_back(inMinutes);
      source>>hh>>delim>>mm;
      inMinutes=hh*60+mm;
      cerr<<"bArriv = "<<hh<<":"<<mm<<" in minutes ="<<inMinutes<<endl;
      bArriv.push_back(inMinutes);
    }

  FORR(t,0,b2a)
    {
      int hh,mm;
      char delim;
      source>>hh>>delim>>mm;
      int inMinutes=hh*60+mm;
      cerr<<"bDep = "<<hh<<":"<<mm<<" in minutes ="<<inMinutes<<endl;
      bDep.push_back(inMinutes);
      source>>hh>>delim>>mm;
      inMinutes=hh*60+mm;
      cerr<<"aArriv = "<<hh<<":"<<mm<<" in minutes ="<<inMinutes<<endl;
      aArriv.push_back(inMinutes);
    }

  sort(BE(aDep));
  sort(BE(aArriv));
  sort(BE(bDep));
  sort(BE(bArriv));

  cerr<<"sorted values:"<<endl;
  cerr<<"aArriv:";FORE(itx,aArriv) cerr<<(*itx)<<" ";cerr<<endl;
  cerr<<"aDep:";FORE(itx,aDep) cerr<<(*itx)<<" ";cerr<<endl;
  cerr<<"bArriv:";FORE(itx,bArriv) cerr<<(*itx)<<" ";cerr<<endl;
  cerr<<"bDep:";FORE(itx,bDep) cerr<<(*itx)<<" ";cerr<<endl;

  dest<<needForStation(aDep,aArriv,tatime)<<" "<<needForStation(bDep,bArriv,tatime);
}

int main()
{
  int n;
  cin>>n;
  FORR(t,0,n)
    {
      cerr<<"Begin to process "<<(t+1)<<" case"<<endl;
      cout<<"Case #"<<(t+1)<<": ";
      process(cin,cout);
      cout<<endl;      
    }
  
  return 0;
}
 
