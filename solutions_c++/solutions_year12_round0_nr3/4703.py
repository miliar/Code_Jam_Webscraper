#include<iostream>
using namespace std;
int digit(int num)
{
    int count=0;
    while(num!=0)
    {
        count++;
        num/=10;
    }
    return count;
}
int reverse(int temp,int factor,int fac)
{
    //if(temp%10==0) return temp;
    temp=(temp/(factor))+((temp%(factor))*fac);
    return temp;
}
int main()
{
   // freopen("inp.txt","r",stdin);
   // freopen("out.txt","w",stdout);
    int test,i,j,k,a,b,pair,temp,t,temp2,factor,fac;
    cin>>test;
    for(i=0;i<test;i++)
    {
        cin>>a>>b;
        pair=0;
        temp=a;
        while(temp<12) temp++;
        if(temp==12 && b>=12){ pair++;temp++;}
        while(temp<=b)
        {
            fac=1;factor=10;
            for(j=0;j<digit(temp)-1;j++)
            fac=fac*10;
            t=reverse(temp,factor,fac);
            while(t!=temp)
            {
                if(t>temp && t<=b)
                pair++;
             //   if(t%10==0) break;
                factor*=10;fac/=10;
             //   cout<<"t: "<<t<<endl;
                t=reverse(temp,factor,fac);

            }
            temp++;
        //    t=reverse(temp)
        }
        cout<<"Case #"<<i+1<<": "<<pair<<endl;
    }
    return 0;
}

