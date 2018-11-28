#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <queue>
#include <deque>
#include <set>

using namespace std;

#define mem(i,n) memset(i,n,sizeof(i))
#define fo(i,n) for(i=0;i<(n);i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define sz size()
#define cs c_str()

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

FILE *in=fopen("A-large.in","r");
FILE *out=fopen("A.out","w");

int main()
{
    long long p,i,j,k,N;
    fscanf(in,"%lld",&N);
    fo(p,N)
    {
        long long ret=0,P,K,L,F[1005];
        fscanf(in,"%lld %lld %lld",&P,&K,&L);
        fo(i,L)fscanf(in,"%lld",&F[i]);
        sort(F,F+L);
        k=1;
        int x=0;
        for(i=L-1;i>=0;i--)
        {
            if(x==K)
            {
                x=0;
                k++;
            }
            ret+=k*F[i];
            x++;
        }
        fprintf(out,"Case #%lld: %lld\n",p+1,ret);
    }
    return 0;
}

































