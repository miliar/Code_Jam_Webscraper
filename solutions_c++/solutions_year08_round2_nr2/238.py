#include <iostream>

using namespace std;

const int MAXP = 1000;
int Sieve[MAXP + 1] = { 0 };
int CP = 0;

int genSieve()
{
    int c = 0;
    for (int i = 2; i <= MAXP; i++)
        if (!Sieve[i])
        {
            for (int j = 2; i*j <= MAXP; j++)
                Sieve[i*j] = 1;
            Sieve[c++] = i;
        }
    return c;
}

bool share(int a, int b, int p)
{
    int i = 0;
    while (i < CP && Sieve[i] < p)
        i++;
    if (i == CP)
    {
        cout << "Oops!" << endl;
        return false;
    }
    for (; i < CP && Sieve[i] <= a && Sieve[i] <= b; i++)
        if (((a % Sieve[i]) == 0) && ((b % Sieve[i]) == 0))
            return true;
    
    return false;
}

int main()
{
    CP = genSieve();
    int C = 0;
    cin >> C;
    const int MAX = 1000;
    for (int c = 1; c <= C; c++)
    {
        int A, B, P;
        cin >> A >> B >> P;
        int N = B - A + 1;
        int sets[MAX] = { 0 };
        for (int i = 0; i < N; i++)
            sets[i] = i;
        for (int i = 0; i < N; i++)
        {
            for (int j = i + 1; j < N; j++)
            {
                if (!share(A + i, A + j, P))
                    continue;
                sets[i] = sets[j] = sets[i] < sets[j] ? sets[i] : sets[j];
            }
        }
        
        bool seenset[MAX] = { false };
        for (int i = 0; i < N; i++)
            seenset[sets[i]] = true;
        int count = 0;
        for (int i = 0; i < N; i++)
            if (seenset[i])
                count++;

        cout << "Case #" << c << ": " << count << endl;
    }
    
    return 0;
}
