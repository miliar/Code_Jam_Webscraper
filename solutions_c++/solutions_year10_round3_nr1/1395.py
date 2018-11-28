#include <cstdlib>
#include <cstdio>

using namespace std;

bool is_intersect(int A1, int B1, int A2, int B2)
{
     if(A1>A2 && B1<B2 || A2>A1 && B2<B1)
              return true;
     return false;
}
int main(int argc, char *argv[])
{
    freopen("A-large.in","r",stdin);
    
    int T,C;
    
    scanf("%d",&T);
    for(int C=1;C<=T;C++)
    {
            int N;
            scanf("%d",&N);
            
            int A[1001],B[1001];
            for(int i=0;i<N;i++)
                    scanf("%d %d",&A[i],&B[i]);
                    
            int res=0;
            bool check[1001][1001]={false,};
            
            for(int i=0;i<N-1;i++)
            {
                    for(int j=i+1;j<N;j++)
                    {                            
                            if(is_intersect(A[i],B[i],A[j],B[j]) && !check[i][j])
                            {
                                check[i][j]=true;
                                check[j][i]=true;
                                res++;
                            }               
                    }
            }
            
            printf("Case #%d: %d\n",C,res);
    }
    
    return 0;
}
