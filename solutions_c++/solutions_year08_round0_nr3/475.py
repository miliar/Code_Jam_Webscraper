#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <cmath>

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

double process(istream &source)
{
  double f,R,t,r,g;
  cin>>f>>R>>t>>r>>g;
  cerr<<"We now have case with f R t r g = "<<f<<" "<<R<<" "<<t<<" "<<r<<" "<<g<<endl;

  t+=f;
  r+=f;
  g-=2*f;
  if(g<0) return 1.0;

  int n=5000000;
  
  double rin=R-t,Snorm=M_PI*R*R/4,my=rin,dy=my/n;
  double slen=0;
  for(double y=0;y<my;y+=dy)
    {      
      double gy=sqrt(rin*rin-y*y);
      double sy=y-int(y/(g+2*r))*(g+2*r);
      if(sy>=r && sy<=(r+g))
	{
	  double g1=int(gy/(2*r+g))*(2*r+g);
	  slen+=g1*g/(2*r+g);
	  double ost=gy-g1;
	  if (ost>r) if(ost<r+g) slen+=ost-r; else slen+=g; 
	}
    }

  double SflyEscape=slen*dy;  
  double prob=(Snorm-SflyEscape)/Snorm;

  prob=prob<0?0:prob;
  cerr<<"prob="<<prob<<endl;

  return prob;    
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
 
