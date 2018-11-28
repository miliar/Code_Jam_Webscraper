#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<map>
#include<cmath>
using namespace std;

#define mpair make_pair
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

struct ss{
       int b,e,v;
}

hashing[1009];

bool cmpair(ss a,ss b)
{
       if(a.v < b.v)return true;
       return false;
}
int main()
{
       int T;
       cin>>T;
       for(int tc=1;tc<=T;tc++)
       {
               int x,s,r,t1,n;
               int bi,ei,vi;
               double fin_result=0.0;
               scanf("%d%d%d%d%d",&x,&s,&r,&t1,&n);
               
               memset(hashing,0,sizeof(hashing));
               for(int i=0;i<n;i++)
               {
                       scanf("%d%d%d",&bi,&ei,&vi);
                       hashing[i].b=bi,hashing[i].e=ei,hashing[i].v=vi;
               }
               sort(hashing,hashing+n,cmpair);
               
               double i=0.0,t=(double)t1;
               double y=(double)x;
               for(int ii=0;ii<n;ii++)
               {
                       y=y-(hashing[ii].e-hashing[ii].b);
               }
               //cout<<y<<"\n";
               double tt=(double)y/(r);
               int flag=((int)floor(tt-t) >=0);
               //cout<<flag<<"\n";
               if(flag)
               {
                       fin_result+=t;
                       y=y-(t*r);
                       t=0.0;
               }
               else
               {
                       t-=tt;
                       fin_result+=tt;
                       y=0.0;
               }
               //printf("Case #%d: %.10lf\n",tc,fin_result);
               //cout<<t<<"\n";
               fin_result=fin_result+y/(double)s;
               //cout<<fin_result<<"\n";
               double distnce=0.0;

               for(int ii=0;ii<n;ii++)
               {
                               double tt=(double)(hashing[ii].e-hashing[ii].b)/(r+hashing[ii].v);
                                       int flag=((int)floor(tt-t) >=0);
                               if(flag)
                               {
                                       fin_result+=t;
                                       distnce=(hashing[ii].e-hashing[ii].b);
                                       distnce=distnce-(t*(r+hashing[ii].v));
                                       fin_result+=distnce/(hashing[ii].v+s);
                                       t=0.0;
                                       //cout<<fin_result<<" "<<distnce<<"\n";
                               }
                               else
                               {
                                       t-=tt;
                                       fin_result+=tt;
                               }
                               
                       
               }
               //if(tc==29)cout<<x<<" "<<s<<" "<<r<<" "<<t<<" "<<n<<"\n";
               printf("Case #%d: %.10lf\n",tc,fin_result);
       }
       return 0;
}


