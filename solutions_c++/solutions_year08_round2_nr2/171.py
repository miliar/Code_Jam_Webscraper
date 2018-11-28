#include <iostream>
#include <vector>
#include <set>

using namespace std;

int A, B, P;

int groups[2000];

void recolor_group(int from, int to)
{
    for (int i=A; i <= B; i++)
        if (groups[i] == from)
            groups[i] = to;
}

vector<int> factor(int i)
{
    vector<int> res;

    for (int j=2; i != 1; j++)
        if (i%j == 0)
        {
            res.push_back(j);
            while (i%j == 0)
                i/=j;
        }

    return res;
}

bool is_prime(int i)
{
    for (int j=2; j < i; j++)
        if (i%j == 0)
            return false;

    return true;
}

int solve()
{
    for (int i=0; i <= B; i++)
        groups[i] = i;

    for (int i=P; i <= B; i++)
        if (is_prime(i))
        {
            int j = i;
            while (j <= B)
            {
                recolor_group(groups[j], groups[i]);
                j += i;
            }
        }


    set<int> res;
    for (int i=A; i <= B; i++)
        res.insert(groups[i]);

    return res.size();
}

int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);

    int T;

    cin >> T;
    for (int i=1; i <= T; i++)
    {
        cin >> A >> B >> P;

        cout << "Case #" << i << ": " << solve() << endl;
    }
}
