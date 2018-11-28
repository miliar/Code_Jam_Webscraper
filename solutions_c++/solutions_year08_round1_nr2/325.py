#include<iostream>
#include<cmath>
#include<math.h>
using namespace std;
#define INF 1<<30
#define N 80
#define M 208

int main()
{
	int t,i,j,k,rr,r,n,m;
	freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\a.out","w",stdout);
	scanf("%d",&t);
	bool flag[M][N][2];
	int mm[20];
	for(rr=0; rr<t; rr++)
	{
	    scanf("%d%d",&n,&m);
	    int T,x,y;
        memset(flag, 0, sizeof(bool)*M*N);
        for(i=0; i<m; i++)
        {
            scanf("%d",&T);
            for(j=0; j<T; j++)
            {
                scanf("%d%d",&x,&y);
                flag[i][x-1][y] = true;
            }
        }
	    
        k = (1<<n);
	    int num=10000,sort[N];
	    bool ok = false;
	    for(i=0; i<k; i++)
        {
            int ii = i, nnum = 0;
            for(j=0; j<n; j++)
            {
                mm[j] = ii%2;
                nnum += mm[j];
                ii /= 2;
            }
            for(j=0; j<m; j++)
            {
                for(r=0; r<n; r++)
                {
                    if(flag[j][r][mm[r]]==true) break;
                }
                if(r>=n) break;
            }
            if(j>=m)
            {
                ok = true;
                if(nnum<num)
                {
                    num = nnum;
                    for(r=0; r<n; r++) sort[r] = mm[r];
                }
            }
        }
	    printf("Case #%d:",rr+1);
	    if(ok==false) printf(" IMPOSSIBLE\n");
	    else
	    {
            for(i=0; i<n; i++) printf(" %d",sort[i]);
            printf("\n");
        }
	}
	return 0;
}
