#include<iostream>
#include<cstdio>
#include<string.h>
#include<math.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("aaaal.out","w",stdout);
    long long t,s,sum,i,j,k,ta[1000],poso,posb,o[1000],b[1000];
    char a[1000];
    cin>>t;
    for(i=0;i<t;i++)
    {
                    long to=0,tb=0;
                    poso=1;
                    posb=1;
                    cin>>s;
                    getchar();
                    for(j=0;j<s;j++)
                    {
                                    scanf("%c%lld",&a[j],&ta[j]);
                                    getchar();
                    }
                    sum=0;
                    long kk=0;
                    k=0;
                    /*for(j=0;j<s;j++)
                    if(a[j]=='O')
                    o[k++]=ta[j];
                    else b[kk++]=ta[j];*/
                    k=kk=0;
                    //for(j=0;j<s;j++)
                   // cout<<"j:"<<j<<" val: "<<ta[j]<<endl;
                   long prev=0;
                    for(j=0;j<s;j++)
                    {
                                    if(a[j]=='O')
                                    {
                                                 if(to>abs(ta[j]-poso))
                                                 {
                                                                       poso=ta[j];
                                                 }
                                                 else
                                                 { 
                                                     if(poso>ta[j])
                                                     poso=poso-to;
                                                     else poso=poso+to;
                                                     //poso=abs(ta[j]-to);
                                                 }
                                                // cout<<"index:"<<j<<" poso:"<<poso<<endl;
                                                 prev=sum;
                                                 sum+=abs(ta[j]-poso)+1;
                                                // cout<<sum<<endl;
                                                 tb+=sum-prev;
                                                 //cout<<"tb: "<<tb<<endl;
                                                 poso=ta[j];
                                                 to=0;
                                    }
                                    else
                                    {
                                        if(tb>abs(ta[j]-posb))
                                                 {
                                                 //to+=abs(ta[j]-posb)+1;
                                                 posb=ta[j];
                                                 }
                                                 else
                                                 {
                                                // cout<<"dhh\n";
                                                  if(posb>ta[j])
                                                  {
                                                 // cout<<"ssss\n";
                                                  posb=posb-tb;
                                                  }
                                                  else posb=posb+tb;
                                                 }
                                                 prev=sum;
                                                // cout<<"index:"<<j<<" posb:"<<posb<<endl;
                                                 sum+=abs(ta[j]-posb)+1;
                                                 to+=sum-prev;
                                                 //cout<<"to: "<<to<<endl;
                                                 posb=ta[j];
                                                 tb=0;
                                    }
                                   // printf("%c : poso : %ld  . posb: %ld\n",a[j],poso,posb);
                    }
                    printf("Case #%lld: %lld\n",i+1,sum);
    }
    return 0;
}
