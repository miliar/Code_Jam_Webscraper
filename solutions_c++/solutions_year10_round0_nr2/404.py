#include<string>
#include<vector>
#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;
int gcd(int m,int n)//m>n
{
    int i;
    
    if(n>m){i=n;n=m;m=i;}
    while(n!=0)
    {
       i=m%n;m=n;n=i;
    }
    return m;
}
int gcdmulti(vector<int> t)
{
    int ans;
    int i;
    if(t.size()==1){return t[0];}
    ans=gcd(t[0],t[1]);
    for(i=2;i<t.size();i++)
    {
       if(t[i]%ans!=0){ans=gcd(ans,t[i]);}
    }
    return ans;
}
int MMod(int a,int s)//(-a) mod s
{
    int i;
    if(a%s==0){return 0;}
    else
    {
         return ((a/s)+1)*s-a;
    }
}
int main()
{
    ifstream cin("f1.in");
    ofstream cout("f2.out");
    int i,n,j,t,c;
    cin>>c;
    for(j=1;j<=c;j++)
    {
           cin>>n;
           vector<int>t(n);
           vector<int>tem(n-1);
           cin>>t[0];
           for(i=1;i<n;i++)
           {
               cin>>t[i];
               tem[i-1]=abs(t[i]-t[0]);
           }
           
           int g=gcdmulti(tem);
           int ans=MMod(t[0],g);    
           cout<<"Case #"<<j<<":"<<" "<<ans;
           cout<<endl;
    }

}
