#include <iostream>
#include <stdlib.h>

using namespace std;

bool canReach(int N, int *d, int *l, int D);

int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    for(int counter = 1; counter <= T; counter++)
    {
        int N;
        cin >> N;

        int *d = new int[N];
        int *l = new int[N];
        for(int n = 0; n < N; n++)
        {
            cin >> d[n] >> l[n];
        }

        int D;
        cin >> D;


        cout << "Case #" << counter << ": ";

        if(canReach(N, d, l, D))
        {
            cout << "YES";
        }
        else
        {
            cout << "NO";
        }

        cout << "\n";


        delete[] d;
        delete[] l;
    }
}

bool canReach(int N, int * d, int *l, int D)
{
    bool *reach = new bool[N];
    int *usable = new int[N];
    for(int n = 0; n < N; n ++)
    {
        usable[n] = 0;
    }
    usable[0] = d[0];

    int next = 1;
    for(int n = 0; n < N; n++)
    {
        for(; next < N && d[next] <= d[n] + usable[n]; next++)
        {
            usable[next] = min(l[next], d[next] - d[n]);
        }
    }

    bool success = false;
    for(int n = 0; n < N; n++)
    {
        if(d[n] + usable[n] >= D)
        {
            success = true;
            break;
        }
    }

    delete[] reach;
    delete[] usable;

    return success;

}
