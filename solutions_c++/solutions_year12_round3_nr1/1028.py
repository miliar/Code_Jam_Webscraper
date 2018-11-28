#include <cstdio>
#include <vector>

using namespace std;

int N;
int a[1000][10];
int m[1000];
bool v[1000];

bool f(int n)
{
    if(v[n])
        return true;
    v[n] = true;
    for(int i=0; i<m[n]; i++)
        if( f(a[n][i]) )
            return true;
    return false;
}

bool d()
{
    for(int i=0; i<N; i++)
    {
        for(int x=0; x<N; x++)
            v[x] = false;
        if( f(i) )
            return true;
    }
    return false;
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++)
    {
        scanf("%d", &N);
        for(int i=0; i<N; i++)
        {
            scanf("%d", &m[i]);
            for(int j=0; j<m[i]; j++)
            {
                scanf("%d", &a[i][j]);
                a[i][j]--;
            }
        }
        printf("Case #%d: %s\n", t, d() ? "Yes" : "No");
    }

    return 0;
}