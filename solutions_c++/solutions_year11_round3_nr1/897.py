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

int t=1,tests,i,j,R,C,flag;
vector<string> a;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large-0.out","w",stdout);
    scanf("%d",&tests);
    while(t<=tests)
    {
         scanf("%d %d",&R,&C);
         a.clear();
         for(i=0;i<R;i++)
         {
             string temp;
             cin>>temp;
             a.pb(temp);
         }
         flag=1;
         for(i=0;i<R && flag==1;i++)
         {
            for(j=0;j<C && flag==1;j++)
            {
                 if(a[i][j]=='#')
                 {
                     if(i+1<R && j+1<C)
                     {
                         if(a[i][j+1]=='#' && a[i+1][j]=='#' && a[i+1][j+1]=='#')
                         {
                             a[i][j]='/';
                             a[i][j+1]='\\';
                             a[i+1][j]='\\';
                             a[i+1][j+1]='/';
                         }
                         else
                         {flag=0;}
                     }
                     else
                     {
                         flag=0;
                     }
                 }
            }
         }
         printf("Case #%d:\n",t);
         if(flag==0)
         {cout<<"Impossible\n";}
         else
         {
             for(i=0;i<R;i++)
             {
                cout<<a[i]<<endl;
             }
         }        
                   
         t++;
    }
    getch();
}
