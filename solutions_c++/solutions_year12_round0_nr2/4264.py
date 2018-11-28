#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;



int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.in ","w",stdout);
    int t,q=1;
    cin>>t;
    while(t--)
    {
        int n,s,p,x,countp=0,counts=0,z=0;
        int a[100]= {0};
        cin>>n>>s>>p;
        for(int i=0; i<n; i++)
        {
            cin>>x;
         if(x>=(p*3)-2)
         countp++;
         else if(x==((p*3)-3)&&x!=0||x==((p*3)-4)&&x!=0)
         {
             if(s>0)
                 {
                     countp++;
                     s--;
                 }
         }
     }
     if(p==0)
     countp=n;

     cout<<"Case #"<<q<<": "<<countp<<endl;
     q++;
    }
}
