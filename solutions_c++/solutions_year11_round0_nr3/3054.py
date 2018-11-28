#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

struct val
{
    int xor_value;
    int real_value;

    bool operator < (const val & v) const
    {
        return real_value < v.real_value;
    }
};

int main()
{
    int T, N;
    cin >> T;
    
    for (int i = 0; i < T; i++)
    {
        cin >> N;
        vector<int> candies;
        set<val> possibilities;
        int max_xor = 0;
        int max_real = 0;
        for (int j = 0; j < N; j++)
        {
            int v;
            cin >> v;
            candies.push_back(v);
            max_xor ^= v;
            max_real += v;
        }

        int best = -1;

        val init;
        init.xor_value = 0;
        init.real_value = 0;
        possibilities.insert(init);
        for (size_t j = 0; j < candies.size(); j++)
        {
            set<val> temp = possibilities;
            for (set<val>::reverse_iterator itr = temp.rbegin();
                 itr != temp.rend(); itr++)
            {
                val c;
                c.xor_value = itr->xor_value^candies[j];
                c.real_value = itr->real_value+candies[j];
                temp.insert(c);

                if ((c.xor_value^max_xor) == c.xor_value && 
                    (best == -1 || c.real_value > best) &&
                    c.real_value != max_real)
                    best = c.real_value;
            }
            possibilities = temp;
        }

        cout << "Case #" << i+1 << ": ";
        if (best == -1)
            cout << "NO" << endl;
        else
            cout << best << endl;
    }

    return 0;
}
