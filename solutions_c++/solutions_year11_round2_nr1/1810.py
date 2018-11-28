#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <string>
#include <math.h>

using namespace std;

#define fori(i,j,k) for(int i=j;i<k;i++)
#define ford(i,j,k) for(int i=j-1;i>=k;i--)
#define i64 __int64
#define ld long double
#define mp make_pair


int main()
{
    int t;
    scanf("%d ",&t);
    fori(h,0,t){
        int n;
        scanf("%d",&n);
        int **a=new int*[n];
        fori(i,0,n){
            scanf("\n");
            a[i]=new int[n];
            fori(j,0,n){
                char p;
                scanf("%c",&p);
                if(p=='.')a[i][j]=-1;
                if(p=='0') a[i][j]=0;
                if(p=='1') a[i][j]=1;
            }
        } 
        printf("Case #%d:\n",h+1);
        fori(i,0,n){
            double r=0;
            int b=0,c=0;
            fori(j,0,n) {
                if(a[i][j]==1) b++,c++;
                if(a[i][j]==0) b++;
            } 
            r+=0.25*((double)c/(double)b);
            
                //printf("%lf ",r);
            fori(l,0,n)
            if(a[i][l]!=-1) {
                int e=0,f=0;
                fori(k,0,n)
                    if(k!=i) {
                        if(a[l][k]==1) e++,f++;
                        if(a[l][k]==0) e++;
                    }
                r+=(0.5/(double)b)*((double)f/(double)e);
                
                
            }
            //printf("%lf ",r);
            fori(j,0,n){
                int v=0;
                fori(l,0,n){
                    if(a[j][l]>=0) v++;
                }
                
                double p=0;
                if(a[i][j]!=-1){
                    fori(l,0,n)
                    if(a[j][l]!=-1) {
                       int e=0,f=0;
                       fori(k,0,n)
                           if(k!=j) {
                               if(a[l][k]==1) e++,f++;
                               if(a[l][k]==0) e++;
                           }
                        p+=((double)f/(double)e)/(double)v;
                        //printf("|%d ",v);
                    }
                    
                }
                r+=(p/(double)b)*0.25;
                //printf("%lf ",r);
            }
            printf("%.9lf\n",r);
        }
        
    }
    
    return 0;
}
