#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
#ifdef DEBUG
    ifstream fin("C-small-attempt0.in");
    streambuf *backup = cin.rdbuf(fin.rdbuf());
#endif
    int ncases, low, high;
    cin >> ncases;
    for (int t = 1; t <= ncases; ++t)
    {
        cin >> low >> high;
        int countpairs = 0;
        for (int i = low; i <= high; ++i)
        {
            char buf[20];
            int len = sprintf(buf, "%d", i);
            for (int k = 1; k < len; ++k)
            {
                char m = buf[len - 1];
                for (int j = len - 2; j >= 0; --j)
                    buf[j + 1] = buf[j];
                buf[0] = m;
                int recynum = atoi(buf);
                if (recynum >= low && recynum <= high && recynum > i)
                {
                    ++countpairs;
                        //cout << i << " " << recynum << endl;
                }
            }
        }
        cout << "Case #" << t << ": " << countpairs << endl;
    }
    
#ifdef DEBUG
    cin.rdbuf(backup);
    fin.close();
#endif
    return 0;
}
