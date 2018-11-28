#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int A,B;

bool fit(int a,int b)
{
    if(a<=10 || b<=10)return false;
    else if(a>10 && b>10 && a<100 && b<100)
    {
        if(a/10+(a%10)*10==b)return true;
    }
    else if(a>100 && b>100 && a<1000 && b<1000)
    {
        if(a/10+(a%10)*100==b)return true;
        else if(a/100+(a%100)*10==b)return true;
    }
    else if(a>1000 && b>1000)
    {
        if(a/10+(a%10)*1000==b)return true;
        else if(a/100+(a%100)*100==b)return true;
        else if(a/1000+(a%1000)*10==b)return true;
    }
    return false;
}
int calc()
{
    int r=0;
    for(int i=A;i<=B;i++)
      for(int j=i+1;j<=B;j++)
        if(fit(i,j))r++;
    return r;
}

int main()
{
    int t;
    cin>>t;
    int ans;
    for(int iii=1;iii<=t;iii++)
    {
        cin>>A>>B;
        ans=calc();
        cout<<"Case #"<<iii<<": "<<ans<<endl;
    }
    //system("pause");
    return 0;
}
