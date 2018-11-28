#include <iostream>
#include <fstream>

using namespace std;

int power_ten[10] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};

int main()
{
    ifstream in("rn.in");
    int T;
    in >> T;
    ofstream out("rn.out");
    for(int i = 0, a, b; i < T; ++i)
    {
        in >> a >> b;
        int count = 0;
        int prev_a = -1, prev_b = -1;
        for(int j = a; j < b; ++j)
        {
            int no_digits = 0;
            int x = j;
            while(x)
            {
                ++no_digits;
                x = x/10;
            }
            for(int k = 1; k < no_digits; ++k)
            {
                int y = (j%power_ten[k])*(power_ten[no_digits - k]) + j/power_ten[k];
                if(j < y && y <= b && (j != prev_a || y != prev_b))
                {
                    prev_a = j;
                    prev_b = y;
                    ++count;
                }
            }
        }
        out << "Case #" << i+1 << ": " << count << "\n";
    }
    in.close();
    out.close();
    return 0;
}
