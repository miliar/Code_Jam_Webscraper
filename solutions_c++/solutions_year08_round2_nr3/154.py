#include <iostream>
#include <vector>

using namespace std;

int K, N;
int d[100];

vector<int> build_deck()
{
    vector<int> res(K, -1);
    vector<int> p(K);

    for (int i=0; i < p.size(); i++)
        p[i] = i;

    int j = 0;
    for (int i=1; i <= K; i++)
    {
        res[p[j]] = i;
        j = j%p.size();
        p.erase(p.begin() + j);
        if (p.size())
            j = (j + i)%p.size();
    }


    return res;
}

void solve()
{
    vector<int> deck = build_deck();

    for (int i=0; i < N; i++)
        cout << " " << deck[d[i]-1];
}


int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);

    int T;
    cin >> T;

    for (int i=1; i <= T; i++)
    {
        cin >> K >> N;
        for (int j=0; j < N; j++)
            cin >> d[j];

        cout << "Case #" << i << ":";
        solve();
        cout << endl;
    }
}
