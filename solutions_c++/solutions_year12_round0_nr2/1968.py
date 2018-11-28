#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
#include<cstdlib>
#include<cmath>
using namespace std;
#define fr(i,n) for(long i=0;i<n;i++)

long noof(bool * arr,long n)
{
     long ret=0;
     fr(i,n) if(arr[i]) ret++;
     return ret;
}
long only(bool * arr,bool * bs,long n)
{
     long ret=0;
     fr(i,n) if(arr[i] && !bs[i]) ret++;
     return ret;
}
int main()
{
    //freopen("ip.in","r",stdin);
    //freopen ("op.txt","w",stdout);
    long i,j,cas=1,x,t,n,ss,p,k,pos[3],score[200];
    bool s[200],bs[200],ns[200],taken[200];
    cin>>t;
    while(t--)
    {
              cin>>n>>ss>>p;
              fr(i,n) {
                       cin>>score[i];
                       s[i]=false;
                       bs[i]=false;
                       ns[i]=false;
                       taken[i]=false;
                       }
              
              fr(x,n)
              {
                    //cout<<"Score for plyer "<<x<<" ("<<score[x]<<")\n";
              for(i=p;i<=10;i++)
              {
                                 
                                pos[0]=i;
                                for(j=i-2;j<=i+2;j++)
                                {
                                                     pos[1]=j;
                                                     
                                                     for(k=i-2;k<=i+2;k++)
                                                     {
                                                      if(abs(j-k)<=2) pos[2]=k;
                                                       else continue;
                                                       if(pos[0]<=10 && pos[0]>=0 && pos[1]<=10 && pos[1]>=0 && pos[2]<=10 && pos[2]>=0 && pos[0]+pos[1]+pos[2]==score[x] && abs(pos[0]-pos[1])<=2 && abs(pos[0]-pos[2])<=2 && abs(pos[2]-pos[1])<=2)
                                                       {
                                                        if(abs(pos[0]-pos[1])==2 || abs(pos[0]-pos[2])==2 || abs(pos[2]-pos[1])==2) 
                                                        {
                                                                                 s[x]=true;
                                                           //                      cout<<"Sp :"<<pos[0]<<" "<<pos[1]<<" "<<pos[2]<<endl;
                                                                                 }
                                                        else {
                                                             ns[x]=true;
                                                         //    cout<<"Non..Sp :"<<pos[0]<<" "<<pos[1]<<" "<<pos[2]<<endl;
                                                             }           
                                                       }
                                                     }
                                }
              }
                                                                      if(s[x] && ns[x]) bs[x]=true;
              }
             /* fr(x,n)
              {
                      if(s[x]) cout<<1<<" ";
                      else cout<<0<<" ";
              }
              cout<<endl;
              fr(x,n)
              {
                      if(bs[x]) cout<<1<<" ";
                      else cout<<0<<" ";
              }
              cout<<endl;
              fr(x,n)
              {
                      if(ns[x]) cout<<1<<" ";
                      else cout<<0<<" ";
              }
              cout<<endl;
              */long res=0;
              for(i=0;i<n;i++) {
                               if(ns[i] && !s[i]) {
                                        res++;
                                        taken[i]=true;
                                        }
                               else if(s[i] && !bs[i] && ss>0)
                               {
                                    res++;
                                    taken[i]=true;
                                    ss--;
                               }
                               }
              for(i=0;i<n;i++) if(bs[i]) res++;
              printf("Case #%ld: %ld\n",cas++,res);
    }
    return 0;
}
