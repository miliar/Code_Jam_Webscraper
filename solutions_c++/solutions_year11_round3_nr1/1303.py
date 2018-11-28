#include<iostream>
#include<cmath>
#include<algorithm>
#include<limits>
#include<vector>
#include<bitset>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<map>

using namespace std;

#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,FROM,n) for(int i=FROM;i<n;i++)
#define FORR(i,n) for(int i=n;i>=0;i--)
#define ll long long int
#define llu long long unsigned int


int t,n,m;

int ni()
{
    int temp;
    scanf("%d",&temp);
    return temp;
}

ll nl()
{
    ll temp;
    scanf("%lld",&temp);
    return temp;
}

llu nlu()
{
    llu temp;
    scanf("%llu",&temp);
    return temp;
}

float nf()
{
    float temp;
    scanf("%f",&temp);
    return temp;
}
/*
bool myfunction( const node& i, const node& j )    //use it to sort vectors
{
    if( i.x < j.x ) return false;
    if( j.x < i.x ) return true;
    return j.c < i.c;
}
*/
char s[51],ans[51][51];
int pos,a[50][50];

void build(int x,int y)
{
    if(x==n-1 || y==m-1 || a[x+1][y]!=0 || a[x][y+1]!=0 || a[x+1][y+1]!=0)
    {
        pos=0;
        //cout<<"here"<<endl;
        return;
    }
    ans[x][y]='/';
    ans[x+1][y]='\\';
    ans[x][y+1]='\\';
    ans[x+1][y+1]='/';
    a[x][y]=2;
    a[x+1][y]=2;
    a[x][y+1]=2;
    a[x+1][y+1]=2;
}

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   scanf("%d",&t);
   for(int prob=0;prob<t;prob++)
   {
       pos=1;
       n=ni();
       m=ni();
       REP(i,n)
       {
           scanf("%s",s);
           //cout<<s<<endl;
           REP(j,m)
           {
               if(s[j]=='#')
               a[i][j]=0;
               else
               a[i][j]=1;
               ans[i][j]=s[j];
           }
       }
       REP(i,n)
       {
           REP(j,m)
           {
               if(a[i][j]==0)
               {
                   build(i,j);
                   if(pos==0)
                   break;
               }
           }
           if(pos==0)
           break;
       }
       printf("Case #%d:\n",prob+1);
       if(pos==0)
       printf("Impossible\n");
       else
       {
           REP(i,n)
           {
               ans[i][m]='\0';
               printf("%s\n",ans[i]);
           }
       }
   }


   //system("pause");
   return 0;

}
