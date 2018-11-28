#include<string>
#include<vector>
#include<iostream>
#include<iomanip>
#include<math.h>
#include<functional>
#include<fstream>
using namespace std;
int gcdt(int a,int b)//0=lose,1=win
{
    int tem;

    if(a<b){tem=a;a=b;b=tem;}

    if(a==b){return 0;}
    if(a%b==0){return 1;}
    if(a>=2*b){return 1;}
    else{return 1-gcdt(b,a%b);}
}
int main()
{
    ifstream cin("f1.in");
    ofstream cout("f2.out");

    int n;
    cin>>n;
    for(int k=1;k<=n;k++)
    {
            int a1,b1,a2,b2;
            cin>>a1>>a2>>b1>>b2;
            int ans=0;
            for(int i=a1;i<=a2;i++)
            {
               for(int j=b1;j<=b2;j++)
               {
                  if(gcdt(i,j)==1){ans++;}
               }
            }
            cout<<"Case #"<<k<<": "<<ans<<endl;
    }
}
