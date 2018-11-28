#include <iostream>
#include <map>

using namespace std;

int d[1100][110];

const int MAX = 100000;

void solve()
{
    map<string, int> inds;
    int N, Q;
    cin >> N >> ws;

    for (int i=0; i < N; i++)
    {
        string s;
        getline(cin, s);
        inds[s] = i;
    }

    for (int i=0; i < 1100; i++)
        for (int j=0; j < 110; j++)
            d[i][j] = MAX;

    cin >> Q >> ws;
    if (Q == 0)
    {
        cout << "0" << endl;
        return;
    }

    string s;
    getline(cin, s);
    int id = inds[s];
    for (int i=0; i < N; i++)
        if (i != id)
            d[0][i] = 0;

    for (int i=1; i < Q; i++)
    {
        getline(cin, s);
        id = inds[s];
//        cerr << id << endl;

        for (int j=0; j < N; j++)
            if (j != id)
                for (int k=0; k < N; k++)
                    d[i][j] = min(d[i-1][k] + (j != k), d[i][j]);
    }

    int res = MAX;
    for (int i=0; i < N; i++)
        res = min(res, d[Q-1][i]);

    cout << res << endl;
}

void run()
{
    int T;
    cin >> T;

    for (int k=1; k <= T; k++)
    {
        cout << "Case #" << k << ": ";
        solve();
    }
}

int main(int nargs, char** args)
{
    string inFile = nargs > 1 ? args[1] : "input.txt";

    freopen(inFile.c_str(), "r", stdin);
    freopen((inFile+".res").c_str(), "w", stdout);

    run();
}
