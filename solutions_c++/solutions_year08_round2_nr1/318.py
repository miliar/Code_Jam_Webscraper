#include <map>
#include <list>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

typedef long long LL;

LL v[6],mxy[ 3 ][ 3 ];
LL n,a,b,c,d,x,y,m,res;
bool done[ 3 ][ 3 ][ 3 ][ 3 ][ 3 ][ 3 ];


inline LL diff()
{
    if( !(v[0]==v[2] && v[1]==v[3]) && !(v[2]==v[4] && v[3]==v[5]) )
    {
       LL ret = mxy[v[0]][v[1]]*mxy[v[2]][v[3]]*mxy[v[4]][v[5]];
       return ret;
    }
    return 0;
}

inline LL same()
{
    if( (v[0]==v[2] && v[1]==v[3]) && (v[2]==v[4] && v[3]==v[5]) )
    {
      if(mxy[v[0]][v[1]]>=2)
      {
       LL ret = mxy[v[0]][v[1]]*(mxy[v[0]][v[1]]-1)*(mxy[v[0]][v[1]]-2);
       ret /= 6;
       return ret;
      }
    }
    return 0;
}

inline LL nsame(LL p,LL q, LL r)
{
    if( (v[p]==v[q] && v[p+1]==v[q+1]) && !(v[q]==v[r] && v[q+1]==v[r+1]) )
    {
      if( mxy[v[p]][v[p+1]]>=1)
      {
       LL ret = mxy[v[p]][v[p+1]]*(mxy[v[p]][v[p+1]]-1)*mxy[v[r]][v[r+1]];
       ret >>= 1;
       return ret;
      }
    }
    return 0;
}

inline bool ok()
{
    return !((v[0]+v[2]+v[4])%3) && !((v[1]+v[3]+v[5])%3);
}

void perm()
{
    done[ v[0] ][ v[1] ][ v[2] ][ v[3] ][ v[4] ][ v[5] ] = 1;
    done[ v[0] ][ v[1] ][ v[4] ][ v[5] ][ v[2] ][ v[3] ] = 1;
    done[ v[2] ][ v[3] ][ v[0] ][ v[1] ][ v[4] ][ v[5] ] = 1;
    done[ v[2] ][ v[3] ][ v[4] ][ v[5] ][ v[0] ][ v[1] ] = 1;
    done[ v[4] ][ v[5] ][ v[2] ][ v[3] ][ v[0] ][ v[1] ] = 1;
    done[ v[4] ][ v[5] ][ v[0] ][ v[1] ][ v[2] ][ v[3] ] = 1;
    return;
}

void solve()
{

    for(v[0]=0;v[0]<3;v[0]++)
     for(v[1]=0;v[1]<3;v[1]++)
      for(v[2]=0;v[2]<3;v[2]++)
       for(v[3]=0;v[3]<3;v[3]++)
        for(v[4]=0;v[4]<3;v[4]++)
         for(v[5]=0;v[5]<3;v[5]++)
         {
          if(ok()&&!done[v[0]][v[1]][v[2]][v[3]][v[4]][v[5]])
          {
            res += diff();
            res += same();
            res += nsame(0,2,4);
            res += nsame(0,4,2);
            res += nsame(2,4,0);
            perm();
          }
         }

    return ;
}

int main()
{
    freopen("ain.txt","r", stdin);
    freopen("aout.txt","w", stdout);
    LL N;

    scanf("%lld", &N);

    for(LL t = 1;t<=N;t++)
    {
        scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &n,&a,&b,&c,&d,&x,&y,&m);
        memset(mxy,0,sizeof mxy);
        memset(done,0,sizeof done);
        mxy[ x%3 ][ y%3 ]++;

        //printf("%lld %lld %lld %lld %lld %lld %lld %lld\n", n,a,b,c,d,x,y,m);

        for(LL i = 1; i < n ; i++)
        {
            x = ((a*x)+b)%m;
            y = ((c*y)+d)%m;
            mxy[ x%3 ][ y%3 ]++;
            //printf("%lld %lld \n",x,y);
        }

        res = 0;

        /*for(int i=0;i<3;i++)
        {
            for(int j=0;j<3; j++)
             printf("%lld ", mxy[i][j]);
            printf("\n");
        }*/

        solve();

        printf("Case #%lld: %lld\n",t, res);
    }

    return 0;
}
