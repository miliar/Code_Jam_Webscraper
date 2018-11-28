#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

struct trip {
    int x, y, z;
    trip(int _x, int _y, int _z):x(_x),y(_y),z(_z){}
};

vector<trip> vec[30];
int f[110][110];
int n, s, p;
void pre_work(  )
{
    for ( int i = 0; i <= 10; i++ )
        for ( int j = i; j<= min( 10, i+2 ); j++ )
            for ( int k = j; k<= min( 10, j+2 ) && k <= i + 2; k++ )
            {
                vec[ i + j + k].push_back(trip(i, j, k));
            }
}
int Surp(int score)
{
    for (int i = 0; i < vec[score].size(); i++)
    {
        if ( vec[score][i].z - vec[score][i].x == 2  ) return 1;
    }
    return 0;
}
int noSurp(int score)
{
    for (int i = 0; i < vec[score].size(); i++)
    {
        if ( vec[score][i].z - vec[score][i].x < 2  ) return 1;
    }
    return 0;
}
int sbigger(int score, int p)
{
    for (int i = 0; i < vec[score].size(); i++)
    {
        if ( vec[score][i].z >= p  && vec[score][i].z - vec[score][i].x >= 2  ) return 1;
    }
    return 0;
}
int nsbigger(int score, int p)
{
    for (int i = 0; i < vec[score].size(); i++)
    {
        if ( vec[score][i].z >= p  &&  vec[score][i].z - vec[score][i].x < 2  ) return 1;
    }
    return 0;
}

int main()
{
    int cs, score;
    pre_work();
    scanf( "%d", &cs );
    
    for ( int t = 1; t <= cs; t++ )
    //int t = 1;
    {
        scanf( "%d%d%d", &n, &s, &p );    
        memset(f, 0, sizeof( f ));
        for ( int i = 1; i <= n; i++ )
        {
            scanf( "%d", &score );
            for ( int j = 0; j <= min(i, s); j++)
            {
                if (Surp(score) && j) f[i][j] = f[i-1][j-1] + sbigger(score, p);
                if (noSurp(score) && i-1 >= j) f[i][j] = max( f[i][j], f[i-1][j] +  nsbigger(score, p));
            }
        }
        int ans = f[n][s]; 
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
