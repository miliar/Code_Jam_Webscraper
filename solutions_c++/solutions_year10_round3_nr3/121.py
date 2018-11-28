#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

int b[512][512];
int bh[512][512];
map<int, int> result;

int findMax(int i, int j, int m, int n)
{
    int fix = (m - i) > (n - j) ? (n - j) : (m - i);

    for(int size = 2; size <= fix; size++)
    {
        bool out = false;
        int last = b[i][j] == 1 ? 0 : 1;
        for(int hi = i; hi < i + size; hi++)
        {
            for(int hj = j; hj < j + size; hj++)
            {
                if(last == b[hi][hj] || bh[hi][hj] != 0)
                {
                    out = true;
                    break;
                }
                else last = b[hi][hj];
            }
            if(out) break;
            last = b[hi][j];
        }
        if(out) 
        {
            return (size - 1);
        }
        if(size == fix) return fix;
    }
    return 1;
}

void fun(int m, int n)
{
    result.clear();
    while(true)
    {
        bool out = true;
        int max = -1;
        int mini = 0;
        int minj = 0;
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(bh[i][j] == 0)
                {
                    out = false;
                    int t = findMax(i, j, m, n);
                    if(t > max)
                    {
                        max = t;
                        mini = i;
                        minj = j;
                    }
                }
            }
        }
        if(out) break;
        int len = max;
        for(int i = mini; i < mini + len; i++)
        {
            for(int j = minj; j < minj + len; j++) bh[i][j] = 1;
        }
        if(result.count(-max) <= 0) result[-max] = 1;
        else result[-max] += 1;
    }
    cout << result.size() << endl;
    for(map<int, int>::iterator it = result.begin(); it != result.end(); it++) cout << -(it->first) << " " << it->second << endl;
}

int main(int argc, char *argv[])
{
    int T, m, n;
    cin >> T;
    string line;
    for(int ci = 1; ci <= T; ci++)
    {
        cin >> m >> n;
        getline(cin, line);
        for(int i = 0; i < m; i++)
        {
            getline(cin, line);
            for(int j = 0; j < n / 4; j++)
            {
                char t = line.at(j);
                int tn;
                if(t >= 'A' && t <= 'F') tn = 10 + (t - 'A');
                else tn = t - '0';
                b[i][j * 4] = (tn & 8) ? 1 : 0;
                b[i][j * 4 + 1] = (tn & 4) ? 1 : 0;
                b[i][j * 4 + 2] = (tn & 2) ? 1 : 0;
                b[i][j * 4 + 3] = (tn & 1) ? 1 : 0;
                bh[i][j * 4] = bh[i][j * 4 + 1] = bh[i][j * 4 + 2] = bh[i][j * 4 + 3] = 0;
            }
        }
        cout << "Case #" << ci << ": ";
        fun(m, n);
    }
    return 0;
}
