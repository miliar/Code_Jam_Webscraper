#include<iostream>
#include <vector>
using namespace std;

int gcd(int a, int b)
{
    if(a < b)
        return gcd(b, a);

    if(b == 0)
        return a;
    else
        return gcd(b, a % b);
}

int main()
{
    int T;
    cin >> T;

    for(int caseIndex = 0; caseIndex < T; caseIndex ++)
    {
        int N, L, H;
        cin >> N >> L >> H;

        vector<int> freqs;
        vector<int>(N).swap(freqs);

        for(int i = 0; i < N; i ++)
            cin >> freqs[i];

        bool found = false;
        int theF = -1;
        for(int i = L; i <= H && !found; i ++)
        {
            int match = 0;
            for(int j = 0; j < N && !found; j ++)
            {
                int g = gcd(freqs[j], i);
                if(g == freqs[j] || g == i)
                    match ++;
            }

            if(match == N)
            {
                found = true;
                theF = i;
            }
        }

        cout << "Case #" << caseIndex + 1 << ": ";
        if(found == false)
            cout << "NO";
        else
            cout << theF;
        cout << endl;
    }
}
