#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main()
{
  cout<<setiosflags(ios::fixed)<<setprecision(10);
  
  int cases;cin>>cases;
  for (int c=1;c<=cases;c++){
    double f,R,t,r,g;
    cin>>f>>R>>t>>r>>g;

    double OR=R;

    r+=f;
    g-=2*f;
    R-=t+f;

    double ans=1;

    if (!(g<=0&&R<=0)){
      //cout<<"* "<<r<<" "<<g<<" "<<endl;

      const int cnt=1000000;
      const double d=OR/cnt;

      double circle=0;
      double hit=0;

      double span=2*r+g;

      for (double x=d/2;x<OR;x+=d){
	double oy=sqrt(OR*OR-x*x);
	double ly=sqrt(R*R-x*x);

	if (x>=R){
	  circle+=oy;
	  hit+=oy;
	  continue;
	}

	double ox=x-floor(x/span)*span;
	if (!(ox>=r&&ox<span-r)){
	  circle+=oy;
	  hit+=oy;
	  continue;
	}

	for (double y=0;;){
	  if (y+r>=ly){
	    circle+=ly-y;
	    hit+=ly-y;
	    break;
	  }
	  circle+=r;
	  hit+=r;
	  y+=r;
	  if (y+g>=ly){
	    circle+=ly-y;
	    break;
	  }
	  circle+=g;
	  y+=g;
	  if (y+r>=ly){
	    circle+=ly-y;
	    hit+=ly-y;
	    break;
	  }
	  circle+=r;
	  hit+=r;
	  y+=r;
	}

	circle+=oy-ly;
	hit+=oy-ly;
      }

      //cout<<hit<<", "<<circle<<endl;

      ans=hit/circle;
    }

    cout<<"Case #"<<c<<": "<<ans<<endl;
  }
  return 0;
}
