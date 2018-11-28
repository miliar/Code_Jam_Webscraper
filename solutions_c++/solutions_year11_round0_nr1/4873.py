#include<iostream>
#include<vector>
using namespace std;
#define pb push_back
int main()
{
    int t,count=0;
    cin>>t;
    while(t--)
    {
       count++;
       int i,n,t,tb,to,po,pb,ct,nt,v[1000]={0};
       char c[1000]={0};
       cin>>n;
       for(i=0;i<n;i++)
         cin>>c[i]>>v[i];
       t=0;to=0;tb=0;ct=0,po=1,pb=1;
       for(i=0;i<n;i++)
       {
           if(!i) {
                    if(c[i]=='O') {ct=abs(v[i]-po)+1;
                                   tb=ct;
                                   po=v[i];
                                   to=0;
                                   t+=ct;
                                  // cout<<"ct:"<<ct<<endl;
                                  }
                     else        { ct=abs(v[i]-pb)+1;
                                   to=ct;
                                   pb=v[i];
                                   tb=0;
                                   t+=ct;
                                   //cout<<"ct:"<<ct<<endl;
                                  }  
                   }
         else  {
                   if(c[i]=='O') {ct=abs(v[i]-po)+1;
                                  if(to>=ct) {to-=ct;t+=1;nt=1;}//cout<<"ct:"<<1<<endl;}
                                  else {t+=ct-to;nt=ct-to;}//cout<<"ct:"<<ct-to<<endl;}
                                  po=v[i];
                                  if(c[i-1]=='O') tb+=nt;
                                  else tb=nt;
                                  to=0;
                                  }
                                  
                      else   {     ct=abs(v[i]-pb)+1;
                                  if(tb>=ct) {tb-=ct;t+=1;nt=1;}//cout<<"ct:"<<1<<endl;}
                                  else {t+=ct-tb;nt=ct-tb;}//cout<<"ct:"<<ct-tb<<endl;}
                                  pb=v[i];
                                  if(c[i-1]=='B') to+=nt;
                                  else to=nt;
                                  tb=0;
                                  }     
             }
            
       }
     cout<<"Case #"<<count<<": "<<t<<endl;
    }
       return 0;
}             
