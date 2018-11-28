#include <stdio.h>
#define MAX 1500
int main()
{
    int freq[MAX]={0},n,k,l,p,sum,t;
    scanf ("%d",&n);
    for (int i=0;i<n;i++)
    {
        scanf("%d %d %d",&p,&k,&l);
        sum=0;
        for (int j=0;j<l;j++)
        scanf("%d",&freq[j]);
        for (int j=0;j<l;j++) for (int k=j;k<l;k++) 
        if (freq[j]>freq[k]){t=freq[j];freq[j]=freq[k];freq[k]=t;}
        for (int j=l-1;j+1;j--)
        {
            //printf("%d ",freq[j]);
        sum+=freq[j]*((l-j-1)/k + 1);
        }
        printf("Case #%d: %d\n",i+1,sum);
    }
    return 0;
}
