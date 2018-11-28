#include<iostream>
#include<cstring>
using namespace std;

int a[1001][1001],b[1001];

int main()
{
    freopen("A122.in","r",stdin);
    freopen("A1o.txt","w",stdout);
    
    int t,x=0;
    cin>>t;
    while(t--)
    {
         memset(a,0,sizeof(a));
         int n,i,j,k,l,flag=0;
         cin>>n;
         for(i=0;i<n;i++)
         {
              cin>>j;
              for(k=0;k<j;k++)
              {
                      cin>>l;
                      a[l-1][i]=1;
              }
         }
         cout<<"Case #"<<++x<<": ";
         for(k=0;k<n;k++)
         for(i=0;i<n;i++)
         for(j=0;j<n;j++)
         {
            if(a[i][k] && a[k][j])
            a[i][j]++;
            if(a[i][j]>1) {flag=1; goto X;}
         }
         
         X:
         if(flag)    cout<<"Yes\n";
         else cout<<"No\n";
    }
}                           
                         
                                                 
