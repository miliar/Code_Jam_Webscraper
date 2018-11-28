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
    in =fopen ("small.in","r");
    out=fopen("small.out","w");
    int n;
    fscanf (in,"%d",&n);
    for (int i=1 ; i<=n ; i++)
    {
        int m,k;
        fscanf (in,"%d %d", &m,&k);
        if (k==0)
           fprintf (out,"Case #%d: OFF\n",i);
        else
        {
            if (k%((int)pow(2,m))==((int)pow(2,m)-1))
               fprintf (out,"Case #%d: ON\n",i);
            else
                fprintf (out,"Case #%d: OFF\n",i);
        }
    }
    return 0;
}
