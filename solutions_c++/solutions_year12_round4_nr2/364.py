#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

vector< pair< pair< int, int>, int> > list;

const int maxN( 1000);
int r[maxN];
int ref[maxN];
int rref[maxN];
pair< int, int> pos[maxN];
int N;

int main()
{
    freopen( "circles.in", "r", stdin);
    freopen( "circles.out", "w", stdout);
    int Tcases;
    scanf("%d", &Tcases);
    for ( int cases = 0; cases < Tcases; cases++)
    {
        int W, L;
        scanf("%d %d %d", &N, &W, &L);
        list.clear();
        list.push_back( make_pair( make_pair( 0, W), L));
        for ( int i = 0; i < N; i++)
        {
            scanf("%d", r + i);
            ref[i] = i;
        }
        for ( int i = 0; i < N; i++)
        {
            for ( int j = i + 1; j < N; j++)
            {
                if ( r[i] < r[j])
                {
                    swap( r[i], r[j]);
                    swap( ref[i], ref[j]);
                }
            }
        }

        for ( int i = 0; i < N; i++)
        {
            rref[ref[i]] = i;
        }
        for ( int i = 0; i < N; i++)
        {
            int cur = -1;
            int len = r[i] << 1;
            for ( int j( 0); j < list.size(); j++)
            {
                if ( ( ( list[j].first.second - list[j].first.first >= len) ||
                      ( list[j].first.first == 0 && list[j].first.second >= r[i]) ||
                      ( list[j].first.second == W && list[j].first.first + r[i] <= W) ||
                      ( list[j].first.first == 0 && list[j].first.second == W))
                    && ( list[j].second >= r[i] || list[j].second == L))
                    {
                        cur = j;
                        break;
                    }
            }
            if ( cur == -1)
            {
                printf("ERROR!\n");
                fflush(stdout);
                exit( 1);
            }
            else
            {
                int a = list[cur].first.first;
                int b = list[cur].first.second;
                int c = list[cur].second;
                list.erase( list.begin() + cur);

                int mid = a + len;
                pos[i].first = a + r[i];
                int left = c - len;
                pos[i].second = c - r[i];
                if ( a == 0)
                {
                    pos[i].first = 0;
                    mid = r[i];
                }
                if ( c == L)
                {
                    pos[i].second = L;
                    left = L - r[i];
                }
                if ( left > 0 && mid > a)
                {
                    list.push_back( make_pair( make_pair( a, min( b, mid)), left));
                }
                if ( mid < b)
                {
                    list.push_back( make_pair( make_pair( mid, b), c));
                }
            }
        }

        printf("Case #%d:", cases + 1);
        for ( int i( 0); i < N; i++)
        {
            printf(" %lf %lf", pos[rref[i]].first + 0.0, pos[rref[i]].second + 0.0);
        }
        printf("\n");
    }

    return 0;
}
