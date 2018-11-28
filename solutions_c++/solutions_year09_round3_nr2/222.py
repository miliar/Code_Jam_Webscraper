#include <iostream>
#include <sstream>
#include <fstream>
#include <conio.h>
#include <vector>
#include <math.h>
#include <iomanip>
//#include<>
using namespace std;

bool zero(double a)
{
  return ((a<0.00000001)&&(a>-0.00000001));    
};

int main(int argc, char *argv[])
{
   
    ifstream in;
    ofstream out;
    in.open("B-large(3).in",ios::in);
    out.open("ap.out",ios::out);
    int N,T,t,m,n,i,j,p,q;
    double x[500], y[500], z[500], vx[500],vy[500],vz[500];
    double xt, yt,zt,vxt,vyt,vzt,av,ad,at;
    in >> T;
    for (t=1;t<=T;t++)
    {
		in>>N;
		xt=0;		yt=0;		zt=0;		vxt=0;		vyt=0;		vzt=0;
		for (i=0;i<N;i++) 
		{
			in>>x[i]>>y[i]>>z[i]>>vx[i]>>vy[i]>>vz[i];
			xt+=x[i]; yt+=y[i]; zt+=z[i];
			vxt+=vx[i]; vyt+=vy[i]; vzt+=vz[i];
		};
		xt/=N; yt/=N; zt/=N; vxt/=N; vyt/=N; vzt/=N;
		av=vxt*vxt+vyt*vyt+vzt*vzt;
		if (zero(av))
		{
			ad=sqrt(xt*xt+yt*yt+zt*zt);
			at=0;
		}
		else
		{
			at=-(xt*vxt+yt*vyt+zt*vzt)/av;
			if (at<0) at=0;
			ad=sqrt((xt+vxt*at)*(xt+vxt*at)+
					(yt+vyt*at)*(yt+vyt*at)+
					(zt+vzt*at)*(zt+vzt*at));
			
			
		};
		out<<"Case #"<<t<<": "<<setiosflags(ios::fixed) << setprecision(7)<<ad<<" "<<setiosflags(ios::fixed) << setprecision(7)<<at<<"\n";
    };
    
    
    
    in.close();
    out.close();
    return EXIT_SUCCESS;
   
}
