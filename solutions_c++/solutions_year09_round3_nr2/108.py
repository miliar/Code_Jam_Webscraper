#include<iostream>
#include<vector>
#include<string>
#include<cmath>
using namespace std;
int main()
{ int T;
  cin>>T;
  for(int t=0;t<T;t++)
  { int N;
    cin>>N;
    long long X=0,Y=0,Z=0,VX=0,VY=0,VZ=0;
    for(int j=0;j<N;j++)
    { int x,y,z,vx,vy,vz;
      cin>>x>>y>>z>>vx>>vy>>vz;
      //cout<<z<<" "<<Z<<"\n";
      X+=x;
      Y+=y;
      Z+=z;
      VX+=vx;
      VY+=vy;
      VZ+=vz;
    }
    //cout<<X<<" "<<Y<<" "<<Z<<" "<<VX<<" "<<VY<<" "<<VZ<<"\n";
    long double tim=0;
    if(X*VX+Y*VY+Z*VZ>=0)
    tim=0;
    else
    tim=-(X*VX+Y*VY+Z*VZ)*1.0/(VX*VX+VY*VY+VZ*VZ);
    long double dist=(X+tim*VX)*(X+tim*VX)+(Y+tim*VY)*(Y+tim*VY)+(Z+tim*VZ)*(Z+tim*VZ);
    dist=sqrt(dist);
    dist/=N;
    cout<<"Case #"<<t+1<<": "<<dist<<" "<<tim<<"\n";
  }
}
    
