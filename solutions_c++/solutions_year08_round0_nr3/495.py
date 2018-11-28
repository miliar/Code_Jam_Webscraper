#include<iostream>
#include<cmath>
using namespace std;
double area,arwh,inR;
double integr(double x){
     return inR*inR*0.5*asin(x/inR)+2*x*sqrt(inR*inR-x*x);
}
main(){
     double f,R,t,r,g;
     double ws,wt,xs,xt,ys,yt,zs,zt;
     int T,TT,i,md;
     freopen("C-small.in","r",stdin);
     freopen("C-small.out","w",stdout);
     scanf("%d",&T);
     for(TT=1;TT<=T;TT++){
          scanf("%lf",&f);
          scanf("%lf",&R);
          scanf("%lf",&t); t += f;
          scanf("%lf",&r); r += f;
          scanf("%lf",&g); g -= 2*f;
          inR = R-t;
          if(inR<=0.0||g<=0.0){
               printf("Case #%d: 1.000000\n",TT);
               continue;
          }
          area = M_PI*(R*R-(R-t)*(R-t))*0.25;
          arwh = M_PI*R*R*0.25;
          xs = 0.0;
          xt = r;
          md = 1;
          while(xs<inR){
               //printf("[%d][%lf]\n",TT,xs);
               if(md==1){
                    area += integr(xt)-integr(xs);
                    md = 2;
                    xs = xt;
                    xt += g;
               }else{
                    ys = 0.0;
                    yt = r;
                    while(ys<sqrt(inR*inR-xs*xs)){
                         zs = sqrt(inR*inR-ys*ys);
                         zt = sqrt(inR*inR-yt*yt);
                         ws = max(xs,min(xt,zt));
                         wt = min(xt,max(xs,zs));
                         area += (ws-xs)*(yt-ys);
                         area += integr(wt)-integr(ws)-(wt-ws)*ys;
                         ys = yt + g;
                         yt = ys + 2*r;
                    }
                    md = 1;
                    xs = xt;
                    xt += 2*r;
               }
          }
          printf("Case #%d: %lf\n",TT,area/arwh);
          fflush(stdout);
     }
     return 0;
}
