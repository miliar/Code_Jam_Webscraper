#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdio.h>
#include <time.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <list>
#include <stack>
using namespace std;
 
typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;
 
#define sz size()
#define all(n) n.begin(),n.end()a
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define FOR(n,a,b) for(n=a;n<b;n++)
#define RFOR(n,b,a) for(n=b;n>=a;n--)
#define fo(i,j) for(int i=0;i<j;i++)
 
FILE *in,*out;
int main()
{
    in =stdin;//fopen ("small.in","r");
    out=stdout;//fopen("AMR.out","w");
    int n;
    fscanf (in,"%d",&n);
    for (int i=1 ; i<=n ; i++)
    {
        queue <int> q;
        int r,k,n,sum=0;
        fscanf (in,"%d %d %d",&r,&k,&n);
        for (int j=0 ; j<n ; j++)
        {
            int temp;
            fscanf (in,"%d",&temp);
            q.push(temp);
        }
        for (int j=0 ; j<r ; j++)
        {
            int nw=0,lo=0;
            while (nw<=k)
            {
                  int c=q.front();
                  if (nw+c<=k)
                  {
                     nw+=c;
                     sum+=c;
                     q.pop();
                     if (q.empty())
                     {
                        q.push(c);
                        break;
                     }
                     lo++;
                     if (lo==n)
                     {
                        q.push(c);
                        break;
                     }
                     q.push(c);
                  }
                  else
                      break;
            }
        }
        fprintf (out,"Case #%d: %d\n",i,sum);
    }
    return 0;
}
