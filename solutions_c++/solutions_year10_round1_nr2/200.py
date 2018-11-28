#include <cstdio>
#include <cstdlib>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,D,I,M,N,a[256];
    scanf("%d",&T);
    for (int i=0;i<T;++i)
    {
        scanf("%d %d %d %d",&D,&I,&M,&N);
        for (int j=0;j<N;++j)
            scanf("%d",&a[j]);
        int mem[2][256]={};
        fprintf(stderr,"%d\n",i+1);
        for (int x=0;x<N;++x)
        {
            for (int y=0;y<256;++y)
            {
                int res = mem[x%2][y]+D;
                for (int z=0;z<256;++z)
                {
                    if (abs(y-z)<=M)
                    {
                        if (mem[x%2][z]+abs(z-a[x])<res)
                            res = mem[x%2][z]+abs(z-a[x]);
                    }
                    else
                    {
                        if (M!=0 && mem[x%2][z]+((abs(y-z)-1)/M)*I+abs(z-a[x])<res)
                            res = mem[x%2][z]+((abs(y-z)-1)/M)*I+abs(z-a[x]);
                    }
                }
                mem[1-x%2][y]=res;
            }
        }
    
        int res=mem[N%2][0];
        for (int j=1;j<256;++j)
            if (mem[N%2][j]<res)
                res = mem[N%2][j];
        printf("Case #%d: %d\n",i+1,res);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}

