#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;

long v[2000001],save[2000001];

int func(int A,int B,int p)
{
    int i,j,k,num,n,flag,count=0;
    if(p==1) return 0;
    for(i=A; i<=B; i++)
    {
        memset(save,0, sizeof(save));
        save[i]=1;
        for(j=1; j<p; j++)
        {
            int r=i,x=0;
            n=num=0;
            while(r)
            {
                v[x]=r%10;
                num++;
                r/=10;
                x++;    
            }  
            for(k=j-1; k>=0; k--)
            {
                n= n*10 + v[k];        
            } 
            for(k=num-1; k>=j; k--)
            {
                n = n*10 + v[k];    
            } 
            if(n>A && n<=B && n!=i && n>i && save[n]==0) 
            {
                save[n]=1;
                count++;
            }   
        }        
    }
    return count;        
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("outputC.txt","w",stdout);
    int T,A,B,i;
    scanf("%d",&T);
    for(i=1; i<=T; i++)
    {
        scanf("%d%d",&A,&B);
        int x = log10(A) + 1;
        int res;
        res = func(A,B,x);  
        printf("Case #%d: %d\n",i,res);  
    }
    return 0;    
}
