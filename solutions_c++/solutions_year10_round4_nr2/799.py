#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

int p2(int n)
{
    int re = 1;
    while(n--) re <<= 1;
    return re;
}
int con[1025];
int m[1025];
int main(int argc, char *argv[])
{
    int T, P;
    cin >> T;
    for(int ci = 1; ci <= T; ci++)
    {
        cin >> P;
        int n = p2(P);
        for(int i = 0; i < n; i++)
        {
            cin >> con[i];
        }
        int num = 0;
        while(true)
        {
            int rn = n / 2;
            if(rn == 0) break;
            for(int i = 0; i < rn; i++)
            {
                cin >> m[i];
            }
            for(int i = 0; i < rn; i++)
            {
                int f = i * 2;
                int s = f + 1;
                if(con[f] > con[s])
                {
                    con[i] = con[s] - 1;
                }
                else
                {
                    con[i] = con[f] - 1;
                }
                if(con[i] < 0) num += m[i];
            }
            n = rn;
        }
        cout << "Case #" << ci << ": " << num << endl;
    }
    return 0;
}
