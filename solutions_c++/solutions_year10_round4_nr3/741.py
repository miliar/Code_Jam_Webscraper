#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <vector>
#include <cstring>

using namespace std;

int x1[1000], x2[1000], y1[1000], y2[1000];
int b[103][103];
int main(int argc, char *argv[])
{
    int T, r;
    cin >> T;
    for(int ci = 1; ci <= T; ci++)
    {
        cin >> r;
        memset(b, 0, sizeof(b));
        for(int i = 0; i < r; i++)
        {
            cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];
            if(x1[i] > x2[i]) swap(x1[i], x2[i]);
            if(y1[i] > y2[i]) swap(y1[i], y2[i]);
            for(int x = x1[i]; x <= x2[i]; x++)
            {
                for(int y = y1[i]; y <= y2[i]; y++)
                {
                    b[x][y] = 1;
                }
            }
        }
        int num = 0;
        while(true)
        {
            bool out = true;
        for(int i = 102; i > 0; i--)
        {
            for(int j = 102; j >= 0; j--)
            {
                if(b[i][j])
                {
                    if(b[i - 1][j] == 0 && b[i][j - 1] == 0) b[i][j] = 0;
                    out = false;
                }
                else
                if(b[i - 1][j] == 1 && b[i][j - 1] == 1) 
                {
                    b[i][j] = 1;
                }
            }
        }
        if(out) break;
        num++;
        }
        cout << "Case #" << ci << ": " << num << endl;
    }
    return 0;
}
