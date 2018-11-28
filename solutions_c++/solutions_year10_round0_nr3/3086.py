#include <iostream>

using namespace std;
typedef unsigned long u32;
typedef unsigned long long u64;

int main()
{
    u32 t;
    cin >> t;

    for(u32 i = 0; i < t; ++i)
    {
        u64 result = 0;
        u64 r, k, n;
        cin >> r >> k >> n;

        u64* queue = new u64[n];
        for(u32 j = 0; j < n; ++j)
            cin >> queue[j];

        u64 prevSum = 0, sum = 0;
        for(u32 j = 0; j < n; ++j)
        {
            prevSum = sum;
            sum += queue[j];

            if(sum < prevSum)// Check for integer looping
                break;
        }

        if(sum >= prevSum && sum <= k)
            result = r * sum;
        else
        {
            u32 pos = 0;
            while(r)
            {
                u32 prevPos = (pos ? pos - 1 : n - 1);
                u64 space = k;
                while(queue[pos] <= space && pos != prevPos)
                {
                    space -= queue[pos];
                    pos = (pos + 1) % n;
                }
                result += k - space;
                --r;
            }
        }

        delete queue;

        cout << "Case #" << (i + 1) << ": " << result << endl;
    }

    return 0;
}
