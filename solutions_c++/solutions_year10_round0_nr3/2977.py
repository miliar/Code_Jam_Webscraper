#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

int main()
{
    ifstream cin("C-small-attempt0.in");
	ofstream cout("C-small-attempt0.out");

    int T;
    int cnt = 1;
    cin >> T;
    while(T--)
    {
        long long sum = 0;
        long R, K;
        int N;

        queue<long> g;

        long tempg;
        cin >> R >> K >> N ;
        for(int i = 0; i < N; i++)
        {
            cin >> tempg;
            g.push(tempg);
        }
        long tempsum;
        int tempcnt;
        while(R--)
        {
            tempsum = 0;
            tempcnt = 0;
            while(1)
            {
                tempg = g.front();
                if( tempsum + tempg > K || tempcnt >= N) break;

                tempsum += tempg;
                g.pop();
                g.push(tempg);
                tempcnt++;
            }
            sum += tempsum;
        }
        cout << "Case #" << cnt++ << ": " ;
        cout << sum << endl;
    }
    cin.close();
    cin.close();
    return 0;
}
