#include <iostream>
using namespace std;

int main()
{
    int apart2[32];
    int best[32][2];
    memset(apart2, 0, sizeof(apart2));
    memset(best, 0, sizeof(best));
    for ( int i=0 ; i<=10 ; ++i )
    {
        for ( int j=0 ; j<=10 ; ++j )
        {
            for ( int k=0 ; k<=10 ; ++k )
            {
                int d1 = abs(i - j);
                int d2 = abs(j - k);
                int d3 = abs(i - k);
                int maxv = max(i, max(j, k));
                int sum = i + j + k;
                if ( d1 <= 2 && d2 <= 2 && d3 <= 2 )
                {
                    if ( d1 == 2 || d2 == 2 || d3 == 2 )
                    {
                        apart2[sum] = 1;
                        best[sum][1] = max(best[sum][1], maxv);
                    }
                    else
                    {
                        best[sum][0] = max(best[sum][0], maxv);
                    }
                }
            }
        }
    }

    int T;
    cin >> T;
    for ( int t=1 ; t<=T ; ++t )
    {
        int N, S, q;
        cin >> N >> S >> q;

        int score[N+2];
        for ( int i=0 ; i<N ; ++i ) 
        {
            cin >> score[i];
        }
        sort(score, score+N);

        int res = 0;
        int used[N+2];
        int two_apart = 0;
        memset(used, 0, sizeof(used));
        for ( int i=0 ; i<N ; ++i )
        {
            if ( two_apart < S && apart2[score[i]] && best[score[i]][1] >= q )
            {
                used[i] = 1;
                two_apart++;
                ++res;
            }
        }

        for ( int i=0 ; i<N ; ++i )
        {
            if ( !used[i] )
            {
                int be = 0;
                if ( two_apart < S )
                {
                    if ( apart2[score[i]] )
                    {
                        two_apart++;
                        be = best[score[i]][1];
                    }
                    else
                    {
                        be = best[score[i]][0];
                    }
                }
                else 
                {
                    be = best[score[i]][0];
                }
                if ( be >= q ) 
                {
                    ++res;
                }
            }
        }
        if ( two_apart < S ) res = 0;
        printf("Case #%d: %d\n", t, res);
    }
    return 0;
}
