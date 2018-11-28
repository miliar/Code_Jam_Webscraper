#include<iostream>
using namespace std;
int a,b;
int F[1002],mat[100];

int solve()
{
    int res=0;
    for (int i=0;i<b;i++)
    {
            F[mat[i]]=0;
            for(int j=mat[i]+1;j<a&&F[j]==1;j++)
            res++;
            for(int j=mat[i]-1;j>=0&&F[j]==1;j--)
            res++;
    }
    return res;
}    
    
int main()
{
    freopen("C1.in","r",stdin);
    freopen("C1.out","w",stdout);
    int T,N;
    scanf("%d",&T);
    for(int j=1;j<=T;j++)
    {
        scanf("%d%d",&a,&b);
        for(int i=0;i<b;i++)
        {
            scanf("%d",&N);
            mat[i]=N-1;
        }
        for(int i=0;i<a;i++)
        F[i]=1;
        int min=-1;
        do{
                          
                    int l=solve();
                    if(min==-1 || min>l)
                    min=l;
                    for (int i=0;i<a;i++)
                        F[i]=1;
        }while (next_permutation(mat,mat+b));
        printf("Case #%d: %d\n",j,min);
    }
}        
