#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;


#define DEBUGGING false

#define doubt if (DEBUGGING) cerr

#define foo(x) doubt << #x << ": " << x << endl;
#define loopfoo(x) for (int i2 = 0; i2 < x.size(); i2++) \
                          doubt << #x << "[" << i2 << "]: " << x[i2] << endl;
#define looploopfoo(x) for (int i2 = 0; i2 < x.size(); i2++) { \
                           for (int j2 = 0; j2 < x[i2].size(); j2++) \
                               doubt << '\t' << #x << "[" << i2 << "][" \
                                     << j2 << "]: " << x[i2][j2]; \
                           doubt << endl; }


int main(int argc, char** argv)
{
    int T;
    cin >> T;

    for (int caseNum = 1; caseNum <= T; caseNum++)
    {
        int N;
        cin >> N;
        foo(N);

        vector< pair<int, bool> > b(N);
        vector< pair<int, bool> > o(N);

        for (int i = 0; i < N; i++)
        {
            char c;
            int button;
            cin >> c >> button;
            foo(c);
            foo(button);
            if (c == 'B')
            {
                b[i].first = button;
                b[i].second = true;
                o[i].first = -1;
                o[i].second = false;
            }
            else if (c == 'O')
            {
                b[i].first = -1;
                b[i].second = false;
                o[i].first = button;
                o[i].second = true;
            }
            else
            {
                cout << "ASDFASDFASDFASDFASFD" << endl;
                throw(1);
            }
        }

        for (int i = N-2; i >= 0; i--)
        {
            if (b[i].first == -1 && b[i+1].first != -1)
                b[i].first = b[i+1].first;
            if (o[i].first == -1 && o[i+1].first != -1)
                o[i].first = o[i+1].first;
        }

        int bp = 1, op = 1;
        int time;
        int curr = 0;
        for (time = 0; curr < N; time++)
        {
            bool bcanpush = false;
            bool ocanpush = false;
            if (bp < b[curr].first)
                bp++;
            else if (bp > b[curr].first)
                bp--;
            else if (b[curr].second)
                bcanpush = true;
            if (op < o[curr].first)
                op++;
            else if (op > o[curr].first)
                op--;
            else if (o[curr].second)
                ocanpush = true;
            if (ocanpush || bcanpush)
                curr++;
        }
        cout << "Case #" << caseNum << ": " << time << endl;
    }

    return 0;
}
