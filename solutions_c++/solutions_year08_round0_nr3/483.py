#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<cmath>

#define PI 3.14159265359
#define STEP 32768LL
#define STEPS (STEP*4)


using namespace std;

int main(){
  int N,n=0;
  cin >> N;
  while(n++<N){
    double f,R,t,r,g;
    cin>>f>>R>>t>>r>>g;
    double total = PI*R*R/4;
    double used = 0;
    //    used+=total-PI*(R-t)*(R-t)/4;
    double R2 = R-t-f;
    double R22 = R2*R2;
    double x0,y0;
    double sqsize = (g-2*f)*(g-2*f);
    //    cout<<sqsize<<endl;
    if (g<2*f) sqsize = 0;
    for (double x = f+r;x<R2;x+=g+2*r){
      for (double y = f+r;x*x+y*y<R22;y+=g+2*r){
	//       	cout<<x<<' '<<y<<' ';
	x0=x+g-2*f;
	y0=y+g-2*f;
	//	cout<<x0<<' '<<y0<<' ';
	if (x0*x0+y0*y0<R22){
	  used+=sqsize;
	  //	  cout<<"++ "<<sqsize<<endl;
	}
	else{
	  //	  continue;
	  double stepsize = (g-2*f)/(STEPS+1);
	  long long inside=0;
	  for (int i=0;i<STEPS;i++){
	    long long cur = 0;
	    for (int j=1;j<20;j++){
	      x0=x+stepsize*(i+0.5);
	      y0=y+stepsize*(cur+STEPS/(1<<j)+0.5);
	      if (x0*x0+y0*y0<R22){
		cur+=STEPS>>j;
		inside+=STEPS>>j;
	      }
	    }
	  }
	  //       	  cout<<"+  "<<(sqsize*inside)/(STEPS*STEPS)<<endl;
	  used+=(sqsize*inside)/(STEPS*STEPS);
	}
      }
    }
    double result = 1-used/total;
    //    cout<<used<<' '<<total<<endl;
    printf("Case #%d: %.6f\n",n,result); 
    //    cout<<"Case #"<<n<<" "<<result<<endl;
  }
}
