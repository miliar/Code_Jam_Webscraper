#include<stdio.h>
#include<vector>
#include<bitset>
#include<utility>
#include<string>
#include<string.h>
#include<algorithm>
#include<set>
#include<map>
#include<math.h>
#include<iostream>
#include<conio.h>
using namespace std;

#define max(a,b) (a>=b?a:b)
#define min(a,b) (a<=b?a:b)
#define all(X) (X.begin(),X.end())
#define allr(X) (X.rbegin(),X.rend())
#define mp make_pair
#define pb push_back
#define disp(X,Y) for(int ab=0;ab<Y;ab++){cout<<X[ab]<<endl;}

int t=1,tests,i,j,N,L,H,flag;
vector<long long> a;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-0.out","w",stdout);
    scanf("%d",&tests);
    while(t<=tests)
    {
         scanf("%d %d %d",&N,&L,&H);
         a.clear();
         for(i=0;i<N;i++)
         {
             long long temp;
             cin>>temp;
             a.pb(temp);
         }
         flag=1;
         for(i=L;i<=H;i++)
         {
             flag=1;
             for(j=0;j<N && flag==1;j++)
             {
                 if(i>a[j])
                 {
                     if(i%a[j]!=0)
                     {flag=0;}
                 }
                 else if(i<a[j])
                 {
                     if(a[j]%i!=0)
                     {flag=0;}
                 }
             }
             if(flag==1)
             {break;}             
         }
         printf("Case #%d: ",t);
         if(flag==0)
         {cout<<"NO\n";}                  
         else
         {cout<<i<<endl;}   
         
         t++;
    }
    getch();
}
