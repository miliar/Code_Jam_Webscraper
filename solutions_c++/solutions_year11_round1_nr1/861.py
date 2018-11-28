#include <iostream>
#include <vector>

using namespace std;

int isPossible(uint64_t n, uint64_t pd)
{
    if (pd == 0)
        return true;
    if (n == 0)
        return false;
    for (int i = 1; i <= n; ++i)
    {
        for (int j = 1; j <= i; ++j)
        {
            if ((static_cast<double>(j) * 100)/ static_cast<double>(i) == static_cast<double>(pd))
                return true;
        }
    }
    return false;
};

void doTestCase(int testCase)
{
    uint64_t n, pd, pg;
    cin >> n;
    cin >> pd;
    cin >> pg;
    
    bool possible = false;
    
    if (pg == 0 && pd > 0)
        possible = false;
    else if (pg == 100 && pd < 100)
        possible = false;
    else
        possible = isPossible(n, pd);
    
    cout << "Case #" << testCase + 1 << ": " << (possible ? "Possible" : "Broken") << endl;
}

int main(int argc, char* argv[])
{
    int t;
    cin >> t;
    
    for (int i = 0; i < t; ++i)
        doTestCase(i);

    return EXIT_SUCCESS;
}
