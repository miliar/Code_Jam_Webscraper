#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main ()
{
    int T, N, M, casos = 0;
    string tmp;
    cin >> T;
    while (T--)
    {
        cin >> N >> M;
        map <string, bool> E;
        for (int i = 0; i < N; i++)
        {
            cin >> tmp;
            E[tmp] = 1;
            for (int j = tmp.size() - 1; j > 0; j--)
            {
                if (tmp[j] == '/')
                {
                    E[string(tmp.begin(), tmp.begin()+j)] = 1;
                }
            }
        }
        int counter = 0;
        for (int i = 0; i < M; i++)
        {
            cin >> tmp;
            if (E.count(tmp) == 0)
            {
                counter++;
                E[tmp] = 1;
            }

            for (int j = tmp.size() - 1; j > 0; j--)
            {
                if (tmp[j] == '/')
                {
                    if (E.count(string(tmp.begin(), tmp.begin()+j)) == 0)
                    {
                        counter++;
                        E[string(tmp.begin(), tmp.begin()+j)] = 1;
                    }
                }
            }
        }
        casos++;
        cout << "Case #" << casos << ": " << counter << endl;
    }

    return 0;
}
