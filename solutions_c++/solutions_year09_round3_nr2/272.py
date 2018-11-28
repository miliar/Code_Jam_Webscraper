#include<cmath>
#include<cstdio>
#define PF(a)((a)*(a))
int x[555],y[555],z[555],vx[555],vy[555],vz[555];
int main(){
  int test;
  scanf("%d",&test);
  int testi;
  for(testi=1;testi<=test;++testi){
    int n;
    scanf("%d",&n);
    int i;
    for(i=0;i<n;++i)
      scanf("%d%d%d%d%d%d",x+i,y+i,z+i,vx+i,vy+i,vz+i);
    double mx=0,my=0,mz=0,vmx=0,vmy=0,vmz=0;
    for(i=0;i<n;++i){
      mx+=x[i];
      my+=y[i];
      mz+=z[i];
      vmx+=vx[i];
      vmy+=vy[i];
      vmz+=vz[i];
    }
    mx/=n;
    my/=n;
    mz/=n;
    vmx/=n;
    vmy/=n;
    vmz/=n;
    
    double t=0;
    if(PF(vmx)+PF(vmy)+PF(vmz)>1e-9)
      t=-(mx*vmx+my*vmy+mz*vmz)/(PF(vmx)+PF(vmy)+PF(vmz));
    if(t<0)t=0;
    double d=sqrt(PF(mx+vmx*t)+PF(my+vmy*t)+PF(mz+vmz*t));
    printf("Case #%d: %.8f %.8f\n",testi,d,t);
  }
  return 0;
}