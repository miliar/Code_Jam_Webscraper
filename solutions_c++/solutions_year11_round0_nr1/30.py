#include <iostream>

using namespace std;

static inline int max(int a, int b)
{
    return a > b ? a : b;
}

static inline int abs(int x)
{
    return x > 0 ? x : -x;
}

int main()
{
    int cases, n, p, bp, bt, op, ot;
    char l;
    
    cin >> skipws >> cases;
    for (int c=1; c<=cases; ++c)
    {
        cin >> n;
        bp = op = 1;
        bt = ot = 0;
        for (int i=0; i<n; i++)
        {
            cin >> l >> p;
            if (l == 'B')
            {
                bt = max(ot + 1, bt + abs(p - bp) + 1);
                bp = p;
            }
            else
            {
                ot = max(bt + 1, ot + abs(p - op) + 1);
                op = p;
            }
        }
        
        cout << "Case #" << c << ": " << max(bt, ot) << endl;
    }
    return 0;
}
