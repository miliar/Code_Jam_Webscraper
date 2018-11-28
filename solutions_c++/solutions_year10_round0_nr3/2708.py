#include <iostream>
#include <queue>

using namespace std;

struct flag_t
{
    int run;
    long long euros;
    int cnt;
};

struct grp_t
{
    int id;
    int sz;
};

int main()
{
    size_t t, T;
    cin >> T;
    for ( t = 0; t < T; ++t )
    {
        int R, k, N;
        cin >> R;
        cin >> k;
        cin >> N;
        flag_t *flag = new flag_t[N];
        queue< grp_t > grp_que;
        int i;
        for ( i = 0; i < N; ++i )
        {
            grp_t grp;
            cin >> grp.sz;
            grp.id = i;
            grp_que.push( grp );
            flag[i].run = -1;
            flag[i].cnt = 0;
        }
        long long total_euros = 0;
        flag[0].run = 0;
        flag[0].euros = 0;
        flag[0].cnt = 1;
        for ( i = 1; i <= R ; ++i )
        {
            int capacity = 0;
            grp_t grp = grp_que.front();

            size_t c = 1;
            while ( c++ <= grp_que.size() )
            {
                if ( capacity + grp.sz <= k )
                {
                    capacity += grp.sz;
                    grp_que.push( grp );
                    grp_que.pop();
                    grp = grp_que.front();
                }
                else
                {
                    break;
                }
            }
            total_euros += capacity;

                if ( flag[grp.id].cnt == 0 )
                {
                    flag[grp.id].run = i;
                    flag[grp.id].euros = total_euros;
                }



                if ( flag[grp.id].cnt == 1 )
                {
                    long long cycle = total_euros - flag[grp.id].euros;
                    total_euros += cycle * ( ( R - i ) / ( i - flag[grp.id].run ) );
                    int rest = ( R - i ) % ( i - flag[grp.id].run );
                    if ( rest )
                    {
                        int j;
                        for ( j = 0; j < rest; ++j )
                        {
                            capacity = 0;
                            c = 1;
                            while ( c++ <= grp_que.size() )
                            {
                                if ( capacity + grp.sz <= k )
                                {
                                    capacity += grp.sz;
                                    //total_euros += grp.sz;
                                    grp_que.push( grp );
                                    grp_que.pop();
                                    grp = grp_que.front();
                                }
                                else
                                {
                                    break;
                                }

                            }
                            total_euros += capacity;
                        }
                    }
                    break;
                }
                ++flag[grp.id].cnt;



        }
        cout << "Case #" << t + 1 << ": " << total_euros << endl;
        delete [] flag;
    }
    return 0;
}
