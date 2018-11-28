#include<stdio.h>
#include<iostream>
using namespace std;
struct train
{
   int dep,arr;
};
bool fun1(train a,train b)
{
   return a.arr<b.arr;
}
bool fun2(train a,train b)
{
   return a.dep<b.dep;
}
int main()
{
   int t,l=0;
   cin>>t;
   while(t--)
  {
   l++;
  int n,a,b,i,ans1=0,ans2=0,j,k,hr1,min1,hr2,min2;
    cin>>n;
    cin>>a>>b;
    train ta[a+1],tb[b+1];
    for(i=0;i<a;i++)
    {
      scanf("%d:%d %d:%d",&hr1,&min1,&hr2,&min2);
      ta[i].dep=hr1*60+min1;
      ta[i].arr=hr2*60+min2;
    }
   for(i=0;i<b;i++)
    {
      scanf("%d:%d %d:%d",&hr1,&min1,&hr2,&min2);
      tb[i].dep=hr1*60+min1;
      tb[i].arr=hr2*60+min2;
    }
    if(a==0 || b==0)
    {
      cout<<"Case #"<<l<<": "<<a<<" "<<b<<endl;
      continue;
    }
    sort(ta,ta+a,fun2);
    sort(tb,tb+b,fun1);

    j=0;
    for(i=0;i<a;i++)
    {
       if(j<b && ta[i].dep>=(tb[j].arr+n))
       {
         j++;
       }
       else
         ans1++;
    }

    sort(tb,tb+b,fun2);
    sort(ta,ta+a,fun1);

    j=0;
    for(i=0;i<b;i++)
    {
       if(j<a && tb[i].dep>=(ta[j].arr+n))
       {
         j++;
       }
       else
         ans2++;
    }
    cout<<"Case #"<<l<<": "<<ans1<<" "<<ans2<<endl;
  }

}



       