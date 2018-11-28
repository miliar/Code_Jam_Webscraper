//Data Structure includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>


//Other Includes
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>

#define PB push_back
#define MP make_pair
#define MAXIMUM 18446744073709551615ULL
#define MAX 1010

using namespace std;

typedef long long int LL;
typedef unsigned long long int ULL;
typedef unsigned int UI;
typedef pair<int,int> PII;

int main()
{
        freopen("B-in.txt", "rt", stdin);
      	freopen("B-out.txt", "wt", stdout);

    int t,n,s,p,score,ans;
    scanf("%d",&t);
    for (int tc=1; tc<=t; tc++)
    {
          ans = 0; 
          scanf("%d%d%d",&n,&s,&p);
    
    if (p>1)
    {
          for (int i=0; i<n; i++)
          {
               scanf("%d",&score);
               if (score >= ((3*p) - 2))
               {
                  ++ans;
                  continue;          
               }   
               if (s>0 && (score >= ((3*p) - 4)) && (score < ((3*p) - 2)))
               {
                  ++ans;
                  --s;
                  continue;          
               }
          }      
    }
    else if (p==0)
    {
         for (int i=0; i<n; i++)
          {
               scanf("%d",&score);
          }
         ans += n;     
    }
    else if (p==1)
    {
         for (int i=0; i<n; i++)
          {
               scanf("%d",&score);
               if (score > 0) ++ans;     
          }
    }
    printf("Case #%d: %d\n",tc,ans);
    }
    return 0;    
}
