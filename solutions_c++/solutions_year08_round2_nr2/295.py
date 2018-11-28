#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

typedef long long int Int;

const unsigned D = 2000000;

bool isPrime(Int p)
{
    if (p == 2) return true;
    if (p < 2 || p % 2 == 0) return false;

    for (Int q = 3; q * q <= p; q += 2)
    {
//    cout << q;
        if (p % q == 0) return false;
    }
    return true;
}

int main()
{

    unsigned *divs = new unsigned[D];
    
//    cout << "H"; 

    unsigned N;
//    fstream cin("example.in");
    cin >> N;
    
    for (unsigned i = 0; i < N; ++i)
    {
//    cout << 1;
        
        unsigned c = 0;
    
        Int A, B, P;
        cin >> A >> B >> P;
    
        fill(divs, divs + (B - A + 1), 0);
        for (Int p = P; p <= B - A; ++p)
        {
            if (!isPrime(p)) continue;
            ++c;
            
            set<unsigned> s;
            for (Int t = A / p * p; t <= B; t += p)
            {
                if (t < A) continue;
                if (divs[t - A] != 0)
                {
                    s.insert(divs[t - A]);
                }
                divs[t - A] = c;
            }

            for (Int j = 0; j <= B - A; ++j)
            {
                if (divs[j] != 0 && divs[j] != c && s.find(divs[j]) != s.end())
                {
                    divs[j] = c;
                }
            }
        }
        set<unsigned> ans;
        unsigned addon = 0;
        for (Int j = 0; j <= B - A; ++j)
        {
            if (divs[j] != 0)
            {
                ans.insert(divs[j]);
            }
            else ++addon;
        }
        cout << "Case #" << (i + 1) << ": " << ans.size() + addon << endl;
    }

    return 0;
}

