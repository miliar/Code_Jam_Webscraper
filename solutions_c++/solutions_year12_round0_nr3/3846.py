#include <cstdio>
#include <set>

using namespace std;

int ncase, len;

int getlen(int num)
{
    int count = 0;
    while ( num )
    {
        num/=10;
        count++;
    }
    return count;
}

int setlen(int n)
{
    int m = 1;
    for ( int i = 0 ; i < n ; i++ )
        m*=10;
    return m;
}

int change(int num, int m)
{
    int t = setlen(m);
    return num/t+num%t*setlen(len-m);
}

int main()
{
    while ( EOF != scanf("%d", &ncase) )
    {
        for ( int icase = 1 ; icase <= ncase ; icase++ )
        {
            set< pair<int, int> > judge;
            int s, t;
            scanf("%d%d", &s, &t);
            len = getlen(t);
            for ( int i = s; i <= t ; i++ )
            {
                for ( int j = 1 ; j < len ; j++ )
                {
                    int m = change(i,j);
                    if ( m > i && m <= t )
                    {
                        judge.insert(make_pair(m,i));
                    }
                }
            }
            printf("Case #%d: %d\n", icase, judge.size());
        }
    }
    return 0;
}
