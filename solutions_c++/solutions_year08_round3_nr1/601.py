#include<stdio.h>
#include<iostream>
using namespace std;
int main(void)
{
    FILE *fin  = fopen ("A-small-attempt0.in", "r");
    FILE *fout = fopen ("A-small-attempt0.out", "w");
    
    int n,p,k,l,a[1200],ans;
    fscanf(fin,"%d",&n);
    for(int nn=1;nn<=n;nn++){
        fscanf(fin,"%d%d%d",&p,&k,&l);
        for(int i=0;i<l;i++)
            fscanf(fin,"%d",&a[i]);
        sort(a,a+l);
        ans=0;
        for(int i=0;i<l;i++){
            ans+=a[l-1-i]*(i/k+1);
        }    
        fprintf(fout,"Case #%d: %d\n",nn,ans);
    }    
    system("pause");
    return 0;
}     
