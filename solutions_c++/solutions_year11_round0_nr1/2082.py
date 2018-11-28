#include<iostream>
using namespace std;
int main()
{
    int t,ot,op,bt,bp,a,i,j,pre,n;
    char ch;
    
    cin>>t;
    for(i=0;i<t;i++)
    {
                    ot=0;
                    bt=0;
                    op=1;
                    bp=1;
                    cin>>a;
                    
                    for(j=0;j<a;j++)
                    {
                                    cin>>ch>>n;
                                    if(ch=='O')
                                    {
                                               if(pre==0)
                                               {
                                                         if(n>op)ot=ot+(n-op)+1;
                                                         else ot=ot+(op-n)+1;
                                                         op=n;
                                               }
                                               else
                                               {
                                                   if(n>op)ot=ot+(n-op);
                                                   else ot=ot+(op-n);
                                                   if(ot<bt)ot=bt;
                                                   ot++;
                                                   op=n;
                                               }
                                               
                                              pre=0;                        
                                    }
                                    else
                                    {
                                         if(pre==1)
                                               {
                                                         if(n>bp)bt=bt+(n-bp)+1;
                                                         else bt=bt+(bp-n)+1;
                                                         bp=n;
                                               }
                                               else
                                               {
                                                   if(n>bp)bt=bt+(n-bp);
                                                   else bt=bt+(bp-n);
                                                   if(bt<ot)bt=ot;
                                                   bt++;
                                                   bp=n;
                                               }
                                               pre=1;
                                    }
                                   
                    }
                     if(bt>ot)cout<<"Case #"<<(i+1)<<": "<<bt<<endl;
                     else cout<<"Case #"<<(i+1)<<": "<<ot<<endl;
                   
    }
    return 0;
}
                                    
                                    
                                           
