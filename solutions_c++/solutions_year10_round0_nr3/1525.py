#include <iostream>
#include <queue>
using namespace std;
#define invalid -1

long long G[1009], H[1009];
int W[1009];

int main()
{
    int x=1, T, R, k, N, i, day, beg, rest;
    long long Total, Sum;

    freopen("C_input.txt","r",stdin);
    freopen("C_output.txt","w",stdout);

    cin>>T;
    while(T--)
    {
        queue <int> wQ, rQ;

        cin >> R >> k >> N;
        for(i=0;i<N;i++)
        {
            cin >> G[i];
            W[i] = invalid;
            wQ.push(i);
        }

        Total=0;
        for( day=0; day<R && W[wQ.front()]==invalid; day++)
        {
            Sum=0;
            while( !wQ.empty() && (Sum+G[wQ.front()]<=k) )
            {
                Sum+=G[wQ.front()];
                rQ.push(wQ.front());
                wQ.pop();
            }

            W[rQ.front()]=day;
            while( !rQ.empty() )
            {
                wQ.push(rQ.front());
                rQ.pop();
            }

            H[day]=Sum;
            Total+=Sum;
        }

        beg = W[wQ.front()];
        rest = (R-day) % (day-beg);
        Sum = 0;
        for( i=beg; i<day; i++)
        {
            Sum += H[i];
            if( i < beg+rest )
                Total += H[i];
        }

        Total += ( (R-day) / (day-beg) ) * Sum;

        cout<<"Case #"<<x++<<": "<<Total<<endl;
    }
    return 0;
}
