#include<iostream>
#include<map>
#include<math.h>
using namespace std;
map<int,double> bs;
int main()
{
    double keeper[100000];
    double probs[100000];
    int enter,a,b,test;
    cin>>test;
    int t=0;
    while(++t<=test)
    {
    double allcorrect[10000];
    allcorrect[0]=1;
    cin>>a>>b;
    enter=b+2;
    keeper[0]=b+1;
    for(int i=1;i<=a;i++)
    {
            cin>>probs[i];
            allcorrect[i]=probs[i]*allcorrect[i-1];
    }
    for(int i=1;i<=a;i++)
    {
            keeper[i]=(b-i+1)*allcorrect[i]+(2*b-i+2)*(1-allcorrect[i]);
    }
    for(int i=1;i<=a;i++)
    {
            bs[i]=keeper[a-i]+1;
    }
    double small=enter<keeper[a]?enter:keeper[a];
    for(int i=1;i<=a;i++)
    {
            small=bs[i]<small?bs[i]:small;
    }
    if(t!=test)
   printf("Case #%d: %.6f\n",t,small);
   else
   printf("Case #%d: %.6f",t,small);
    }
    return 0;
}
    
    
    
