#include<iostream>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<cstring>
#include<string>
#include<sstream>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<cassert>
using namespace std;

typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef pair<int,int> pi;

#define INF 1000000000
#define MAXN 1030

int a[MAXN];
int ret;

void solve( int a1 , int b1 )
{
 if( a1 == b1 )
   return;
 bool flag = false;
 for(int i = a1 ; i <= b1 ; i++)
   if( a[i] > 0 )
   {
      flag = true;
      break;
   }
 if( flag == false )
   return;
 
 ret++;
 for(int i = a1 ; i <= b1 ; i++)
   if( a[i] > 0 )
     a[i]--;
  
  solve( a1 , (a1+b1) / 2 );
  solve( (a1+b1) / 2 + 1 , b1 );
}

int main()
{
  int t;
  scanf("%d",&t);
  for(int cas = 1 ; cas <= t ; cas++)
  {
    ret = 0;
    int p;
    cin>>p;
    for(int i = 0 ; i < (1<<p) ; i++)
    {
      cin>>a[i];
      a[i] = p - a[i];
    }
    int x;
    for(int i = 1 ; i < (1<<p) ; i++)
      cin>>x;
    solve(0 , (1<<p) - 1 );
      
    printf("Case #%d: %d\n",cas,ret);   
     
  }
  return 0;  
}