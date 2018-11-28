#include<iostream>
#include<bitset>
#include<vector>

using namespace std;

int main()
{

    int T;
    cin >> T;
    for(int i = 0; i < T; i ++)
    {
        unsigned long long C;
        cin >> C;

        unsigned long long minele = -1; 
        unsigned long long sum = 0;
        bitset<65> counts;

        for(unsigned long long j = 0; j < C; j ++)
        {
            unsigned long long num, tmp;
            cin >> num;
            if(num == 0)
                continue;

            sum += num;

            if(j == 0)
                minele = num;
            else if(num < minele)
                minele = num;

            tmp = num;
            int k = 0;
            while(tmp != 0)
            {
                if((tmp & 0x1) == 1)
                    counts.flip(k);

                tmp >>= 1;
                k ++;
            }
        }

        cout << "Case #" << i + 1 << ": ";

        if(sum == 0 || counts.none())
            cout << sum - minele << endl;
        else
            cout << "NO" << endl;

    }
    return 0;
}
