#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

#define FORR(x,a,b) for(int x=a;x<b;++x)
#define FORE(x,a) for(typeof((a).begin()) x=(a).begin(); x!=(a).end(); ++x)
#define BE(a) (a).begin(),(a).end()

typedef long long LL;

typedef vector<int> VI;

void process(void)
{
  LL n,a,b,c,d,x0,y0,m;
  cin>>n>>a>>b>>c>>d>>x0>>y0>>m;
  VI x(n),y(n);
  x[0]=x0;y[0]=y0;
  FORR(t,1,n)
    {
      x[t]=(a*x[t-1]+b)%m;
      y[t]=(c*y[t-1]+d)%m;
    }

  LL p,q,r,ret=0;
  FORR(p,0,n)
    FORR(q,p+1,n)
    FORR(r,q+1,n)
    if((x[p]+x[q]+x[r])%3==0 && (y[p]+y[r]+y[q])%3==0)
      {
	//cerr<<p<<" "<<q<<" "<<r<<" "<<x[p]<<" "<<x[q]<<" "<<x[r]<<" "<<y[p]<<" "<<y[q]<<" "<<y[r]<<endl;
	++ret;
      }

  cout<<ret;
}

int main()
{
  int n;
  cin>>n;
  FORR(t,0,n)
    {
      cout<<"Case #"<<(t+1)<<": ";
      cerr<<"case "<<(t+1)<<endl;
      process();
      cout<<endl;
    }
}
