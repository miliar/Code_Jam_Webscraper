#include <iostream>

using namespace std;

bool possible_percentages(long long N, long long Pd, long long Pg)
{
    if ((Pg == 100 && Pd != 100) || 
        (Pg == 0 && Pd != 0))
        return false;

    long long D, M = min(N, (long long) 100);

    for (long long i = 1; i <= M; i++)
    {
        D = i*Pd;
        if (D % 100 == 0)
            return true;
    }

    return false;
}

int main()
{
    int T;
    long long N, Pd, Pg;
    bool p;

    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cin >> N >> Pd >> Pg;
        p = possible_percentages(N, Pd, Pg);
        
        cout << "Case #" << i+1 << ": ";
        if (p) cout << "Possible" << endl;
        else   cout << "Broken" << endl;
    }

    return 0;
}
