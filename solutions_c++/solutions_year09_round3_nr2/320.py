#include<iostream>
#include<cmath>

#define sq(x) ((x)*(x))
#define EPS 0.00000001

using namespace std;

double norm(double x,double y,double z)
{
  return sqrt(sq(x)+sq(y)+sq(z));
}

int main(){

  int T;
  cin>>T;
  for(int test=1;test<=T;test++){
    
    int N;
    cin>>N;

    double x=0,y=0,z=0;
    double vx=0,vy=0,vz=0;

    for(int i=0;i<N;i++){
      double tx,ty,tz,tvx,tvy,tvz;
      cin>>tx>>ty>>tz>>tvx>>tvy>>tvz;
      x+=tx;y+=ty;z+=tz;
      vx+=tvx;vy+=tvy;vz+=tvz;
    }
    
    x/=N;y/=N;z/=N;
    vx/=N;vy/=N;vz/=N;

    if(norm(vx,vy,vz)<EPS){
      printf("Case #%d: %0.8f %0.8f\n",test,norm(x,y,z),0.0);
      continue;
    }
    //pt is the pt where normal intersects

    //pt 3
    double x1,y1,z1;
    x1=x+vx;
    y1=y+vy;
    z1=z+vz;
    
    if(norm(x1,y1,z1)<EPS){
      printf("Case #%d: %0.8f %0.8f\n",test,0.0,1.0);
      continue;
    }

    double v1x,v1y,v1z;

    double nv;
    v1x=vx;v1y=vy;v1z=vz;
    nv=norm(vx,vy,vz);
    vx/=nv;vy/=nv;vz/=nv;

    double a1,a2,a3,b1,b2,b3;
    
    a1=-x1;a2=-y1;a3=-z1; //pt 3 to origion
    b1=x-x1;b2=y-y1;b3=z-z1;

    double c1,c2,c3;

    c1=a2*b3-a3*b2;
    c2=a3*b1-a1*b3;
    c3=a1*b2-a2*b1;

    double dot=0;
    dot=a1*b1+a2*b2+a3*b3;
    
    double na,nb,nc;

    na=norm(a1,a2,a3);
    nb=norm(b1,b2,b3);
    nc=norm(c1,c2,c3);
    
    double sth=nc/(na*nb);
    double proj=dot/nb;
    double cost=dot/(nb*na);

    double ptx=x1-proj*vx;
    double pty=y1-proj*vy;
    double ptz=z1-proj*vz;

    double timex,timey,timez,time;
    timex=(ptx-x)/v1x;
    timey=(pty-y)/v1y;
    timez=(ptz-z)/v1z;
    if(v1x>0)time=(ptx-x)/v1x;
    else if(v1y>0)time=(pty-y)/v1y;
    else time=(ptz-z)/v1z;
    //cout<<"Time : "<<timex<<" "<<timey<<" "<<timez<<endl;
    if(timex<=0){
      //cout<<"Inside"<<endl;
      printf("Case #%d: %0.8f %0.8f\n",test,norm(x,y,z),0.0);
    }
    else {
      //cout<<"Inside "<<sth<<" "<<sqrt(1-sq(cost))<<" "<<cost<<endl;
      printf("Case #%d: %0.8f %0.8f\n",test,norm(x1,y1,z1)*sth,timex);
    }
  }

}
