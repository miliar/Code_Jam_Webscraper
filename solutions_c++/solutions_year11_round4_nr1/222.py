#include<iostream>
using namespace std;


int T;
struct Seg
{
       double b , e , speed;
} S[1024];
bool cmp(Seg A,Seg B)
{
     if (A.speed<B.speed) return true; else return false;
}
double Solve()
{
       double x,s,r,t;
       int N;
       cin>>x>>s>>r>>t>>N;
       for (int i=1;i<=N;++i)
       {
           cin>>S[i].b>>S[i].e>>S[i].speed;
           S[i].speed+=s;
           x-=S[i].e-S[i].b;
       }
       S[0].b=0;S[0].e=x;S[0].speed=s;
       r=r-s;
       sort(S,S+N+1,cmp);     
       double ans=0;
       for (int i=0;i<=N;++i)
       {
               if ((r+S[i].speed)*t>S[i].e-S[i].b)
               {
                   ans+=(S[i].e-S[i].b)/(r+S[i].speed);
                   t-=(S[i].e-S[i].b)/(r+S[i].speed);
               } else
               {
                     ans+=t+(S[i].e-S[i].b-t*(r+S[i].speed))/S[i].speed;
                     t=0;
               }           
       }  
       return ans;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    scanf("%d",&T);
    for (int i=1;i<=T;++i)
    {
        printf("Case #%d: %.8f\n",i,Solve());
    }
    return 0;
} 
