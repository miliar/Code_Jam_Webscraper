#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
char s[1010],ts[1010];
int a[10];
int main()
{
    int i,j,n,nn,ii,k,l,ans,tem;
    scanf("%d",&nn);
    for (ii=1;ii<=nn;ii++) {
        scanf("%d",&k);
        scanf("%s",s);l=strlen(s);
        ans=1000000000;
        for (i=1;i<=k;i++) a[i]=i;
        do {
            tem=1;
            for (i=0;i<l;i+=k) {
                for (j=1;j<=k;j++) ts[i+j-1]=s[i+a[j]-1];
            }
            for (i=1;i<l;i++) if (ts[i]!=ts[i-1]) tem++;
            ans<?=tem;
        } while (next_permutation(a+1,a+k+1));
        printf("Case #%d: %d\n",ii,ans);
    }
}
