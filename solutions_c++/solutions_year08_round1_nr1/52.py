#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;
const int MaxN=800;
int T,t,N,i;
long long ans;
long long x[MaxN],y[MaxN];
FILE *In=fopen("A-large.in","r");
FILE *Out=fopen("A-lagre.out","w");
int main()
{
    fscanf(In,"%d",&T);
    for(t=1;t<=T;t++)
    {
    fscanf(In,"%d",&N);
    for(i=0;i<N;i++)
        fscanf(In,"%I64d",&x[i]);
    for(i=0;i<N;i++)
        fscanf(In,"%I64d",&y[i]);
    sort(x,x+N);
    sort(y,y+N);
    ans=0;
    for(i=0;i<N;i++)
        ans+=x[i]*y[N-i-1];
    fprintf(Out,"Case #%d: %I64d\n",t,ans);
    }
    return 0;
}
