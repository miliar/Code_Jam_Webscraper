#include <cstdio>
#include <cmath>
#include <stdlib.h>


int main(){
  int i, j, t, c, n;
  double x[5], y[5], r[5], ans, d[5];
  scanf("%d",&c);
  for(t=1;t<=c;t++){
    scanf("%d",&n);
    for(i=0;i<n;i++)
      scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);
    if(n==1)ans=r[0];
    else if(n==2)
      ans=r[0]>r[1]?r[0]:r[1];
    else{
      d[0]=sqrt((x[0]-x[1])*(x[0]-x[1])+(y[0]-y[1])*(y[0]-y[1]))+r[0]+r[1];
      d[1]=sqrt((x[2]-x[1])*(x[2]-x[1])+(y[2]-y[1])*(y[2]-y[1]))+r[2]+r[1];
      d[2]=sqrt((x[0]-x[2])*(x[0]-x[2])+(y[0]-y[2])*(y[0]-y[2]))+r[0]+r[2];
      if(d[0]<d[1]){
	if(d[0]<d[2]){
	  if(d[0]/2.>r[2])ans=d[0]/2.;
	  else ans=r[2];
	}
	else{
	  if(d[2]/2.>r[1])ans=d[2]/2.;
	  else ans=r[1];
	}
      }
      else{
	if(d[1]<d[2]){
	  if(d[1]/2.>r[0])ans=d[1]/2.;
	  else ans=r[0];
	}
	else{
	  if(d[2]/2.>r[1])ans=d[2]/2.;
	  else ans=r[1];
	}
      }
    }
    printf("Case #%d: %lf\n",t,ans);
  }

}
