#include <stdio.h>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int eql(int a,int b)
{
    if (a>0 && b<0) return 0;
    if (a<0 && b>0) return 0;
    return 1;
}


int main()
{
    freopen("ina","r",stdin);
    freopen("outa","w",stdout);
    int t,cas,i,j,n,A[1100],B[1100],d1,d2,d3,d4;
    scanf("%d",&t);
    for (cas=1; cas<=t; cas++)
    {
        scanf("%d",&n);
        for (i=0; i<n; i++) scanf("%d%d",&A[i],&B[i]);
        int count=0;
        for (i=0; i<n; i++)
        {
            for (j=i+1; j<n; j++)
            {
                int mni=min(A[i],B[i]);
                int mxi=max(A[i],B[i]);
                int mnj=min(A[j],B[j]);
                int mxj=max(A[j],B[j]);

                int m1=A[i]-B[i];
                int m2=A[j]-B[j];

                if ((mni>=mnj && mxi<=mxj) || (mnj>=mni && mxj<=mxi)) count++;
                else if (!eql(m1,m2))
                {
                    if ((A[i]>=mnj && A[i]<=mxj && (B[i]<=mnj || B[i]>=mxj))) count++;
                    else if ((B[i]>=mnj && B[i]<=mxj && (A[i]<=mnj || A[i]>=mxj))) count++;
                }
            }
        }
        printf("Case #%d: %d\n",cas,count);
    }

	return 0;
}
