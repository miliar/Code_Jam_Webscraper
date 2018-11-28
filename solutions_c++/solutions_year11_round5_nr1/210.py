#include <stdio.h>
#include <math.h>
#define MAXN 200

const double eps=1e-9;

class Coor {
   public:
      double x,y;
      void input() {
         scanf("%lf%lf",&x,&y);
      }
};

int ln,un,cut;
double wid,area;
Coor lp[MAXN],up[MAXN];

inline double abs(double x) { return x>=0.0?x:0.0-x; }
inline double min(double a,double b) { return a<b?a:b; }
inline double max(double a,double b) { return a>b?a:b; }
inline double cross(Coor a,Coor b) { return a.x*b.y-a.y*b.x; }

inline void pre() {
   int i;
   area=0.0;
   for(i=0;i<ln-1;i++)
      area+=cross(lp[i],lp[i+1]);
   area+=cross(lp[ln-1],up[un-1]);
   for(i=un-1;i>0;i--)
      area+=cross(up[i],up[i-1]);
   area+=cross(up[0],lp[0]);
   area*=0.5;
}

inline void solve() {
   int ci,li,ui;
   double goal,cur,add,lslp,uslp,tslp;
   double front,dx,tl,bl,sol,cc;
   pre();
   //printf("<%.4lf>\n",area);
   li=ui=0;
   lslp=uslp=0.0;
   cur=0.0;
   for(ci=1;ci<cut;ci++) {
      goal=area*ci/cut;
      while(1) {
         if(lp[li].x<=up[ui].x) {
            front=min(lp[li+1].x,up[ui].x);
            dx=front-lp[li].x;
            bl=up[ui].y-uslp*(up[ui].x-lp[li].x)-lp[li].y;
            tslp=(lp[li+1].y-lp[li].y)/(lp[li+1].x-lp[li].x);
            tl=bl+(uslp-tslp)*dx;
            add=(bl+tl)*dx/2;
            if(cur+add>=goal) {
               //printf("[%d %d %.4lf]\n",li,ui,add);
               //printf("<%.3lf %.3lf %.3lf %.3lf>\n",cur,goal,bl,tslp-lslp);
               cc=uslp-tslp;
               if(abs(cc)>eps) sol=(-bl+sqrt(bl*bl+2*cc*(goal-cur)))/cc;
               else sol=(goal-cur)/bl;
               sol+=lp[li].x;
               break;
            }
            lslp=tslp;
            cur+=add;
            li++;
         } else {
            front=min(lp[li].x,up[ui+1].x);
            dx=front-up[ui].x;
            bl=up[ui].y-(lp[li].y-lslp*(lp[li].x-up[ui].x));
            tslp=(up[ui+1].y-up[ui].y)/(up[ui+1].x-up[ui].x);
            tl=bl+(tslp-lslp)*dx;
            add=(bl+tl)*dx/2;
            if(cur+add>=goal) {
              // printf("[%d %d %.4lf]\n",li,ui,add);
               //printf("<%.3lf %.3lf %.3lf %.3lf>\n",cur,goal,bl,tslp-lslp);
               cc=tslp-lslp;
               if(abs(cc)>eps) sol=(-bl+sqrt(bl*bl+2*cc*(goal-cur)))/cc;
               else sol=(goal-cur)/bl;
               sol+=up[ui].x;
               break;
            }
            uslp=tslp;
            cur+=add;
            ui++;
         }
      }
      printf("%.9lf\n",sol);
   }
}

int main(void)
{
   int t,i,casenum=1;
   scanf("%d",&t);
   while(t--) {
      scanf("%lf%d%d%d",&wid,&ln,&un,&cut);
      for(i=0;i<ln;i++)
         lp[i].input();
      for(i=0;i<un;i++)
         up[i].input();
      printf("Case #%d:\n",casenum++);
      solve();
   }
   return 0;
}
