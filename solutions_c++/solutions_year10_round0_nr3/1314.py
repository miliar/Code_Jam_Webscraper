#include <iostream>
#include <fstream>
using namespace std;

typedef struct
{
    long value;
    long cnt;
    long sumvalue;
    bool flag;
}Queue;

int main()
{
    ifstream cin("C-large.in");
	ofstream cout("C-large.out");

    int T;
    int cnt = 1;
    cin >> T;
    while(T--)
    {
        long long sum = 0;
        long R, K, N;

        Queue g[1000];

        cin >> R >> K >> N ;
        for(int i = 0; i < N; i++)
        {
            cin >> g[i].value;
            g[i].cnt = 0;
            g[i].sumvalue = 0;
            g[i].flag = false;
        }

        for(int i = 0; i < N; i++)
        {
            long long tempsum = 0;
            long long tempcnt = 0;
            int j = i;
            while(1)
            {
                if( tempsum + g[j].value > K || tempcnt >= N) break;
                tempsum += g[j].value;
                tempcnt++;
                j++;
                j %= N;
            }
            g[i].cnt = tempcnt;
            g[i].sumvalue = tempsum;
        }

        int pos = 0;
        while(1)
        {
            if( g[pos].flag ) break;
            g[pos].flag = true;
            pos += g[pos].cnt;
            pos %= N;
        }

        long long sum1 = 0;
        long long sum2 = 0;
        long long cnt1 = 0;
        long long cnt2 = 0;
        int k = 0;
        while(1)
        {
            if( k == pos ) break;
            sum1 += g[k].sumvalue;
            cnt1++;
            k += g[k].cnt;
            k %= N;
        }

        int i = pos;
        sum2 += g[i].sumvalue;
        cnt2++;
        i += g[i].cnt;
        i %= N;
        while(1)
        {
            if( i == pos ) break;
            sum2 += g[i].sumvalue;
            cnt2++;
            i += g[i].cnt;
            i %= N;
        }

        if( R > cnt1 )
            sum += (R - cnt1)  / cnt2 * sum2;
        int ii = 0;
        long long tempcnt = (R - cnt1) % cnt2 + cnt1;
        while( tempcnt-- )
        {
            sum += g[ii].sumvalue;
            ii += g[ii].cnt;
            ii %= N;
        }

        cout << "Case #" << cnt++ << ": " ;
        cout << sum << endl;
    }
    cin.close();
    cin.close();
    return 0;
}
