#include<stdio.h>
#include<iostream>
using namespace std;
int main(void)
{
    FILE *fin  = fopen ("A-small-attempt1.in", "r");
    FILE *fout = fopen ("A-small-attempt1.out", "w");
    
    int t,n,a[10],b[10],ans;
    fscanf(fin,"%d",&t);
    for(int tt=1;tt<=t;tt++){
        fscanf(fin,"%d",&n);
        for(int i=0;i<n;i++)
            fscanf(fin,"%d",&a[i]);
        for(int i=0;i<n;i++)
            fscanf(fin,"%d",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        ans=0;
        for(int i=0;i<n;i++){
            ans+=a[i]*b[n-1-i];
        }    
        fprintf(fout,"Case #%d: %d\n",tt,ans);
    }    
    return 0;
}     
