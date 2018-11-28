#include<iostream>
#include<cstdio>
using namespace std;


int tens(int i)
{
    int t,o,ans;
    t=i/10; o=i%10;
    ans= 10*o + t;
    return ans;
}
int hunds(int i)
{
    int h,t,ans;
    h=i/100; t=i%100;
    ans= t*10 + h;
    return ans;

}

int main()
{
   
    int tst,t,  o=0,p=0,q=0,r=0,i=0,j=0;
    int a,b=0,count=0,ans=0;
    //int arr[1001];
    cin>>t;
    for(tst=1;tst<t+1;tst++)
    {
        ans=0;
        int perm,pern;
        cin>>a>>b;
        
        if(b>11)
        {
        if(a>11)
        j=a;
        else
        j=12;
        for(i=j;i<=b;i++)
        {
            if(i<100)
            {
                perm=tens(i);
                if(perm<=b && perm>i) ans++;
               }
               
               
            else if(i<1000)
            {
                perm=hunds(i); pern=hunds(perm);
                if(perm<=b && perm>i)
                ans++;
                if(pern<=b && pern>i)
                ans++;
            }
           

        }
        }
        cout<<"Case #"<<++count<<": "<<ans<<endl;

    }//end of tstcase

}//end
