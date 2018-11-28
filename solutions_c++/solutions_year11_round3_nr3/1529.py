#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

bool isPossible(int64_t note, const vector<int64_t>& others)
{
    bool possible = true;
    for (unsigned long i = 0; i < others.size(); ++i)
    {
        double div = static_cast<double>(others[i]) / static_cast<double>(note);
        double t;
        if (modf(div, &t) != 0)
        {
            double div2 = static_cast<double>(note) / static_cast<double>(others[i]);
            if (modf(div2, &t) != 0)
            {
                possible = false;
                break;
            }
        }
    }
    return possible;
}

void doTestCase(int testCase)
{
    cout << "Case #" << testCase + 1 << ": ";

    int64_t n, l, h;
    vector<int64_t> others;
    cin >> n;
    cin >> l;
    cin >> h;
    
    for (int i = 0; i <n ; ++i)
    {
        int64_t o;
        cin >> o;
        others.push_back(o);
    }
    
    bool possible = false;
    for (int64_t i = l; i <= h; ++i)
    {
        if (isPossible(i, others))
        {
            possible = true;
            cout << i;
            break;
        }
    }
    if (!possible)
        cout << "NO";

    cout << endl;
}

int main(int argc, char* argv[])
{
    int t;
    cin >> t;
    
    for (int i = 0; i < t; ++i)
        doTestCase(i);

    return EXIT_SUCCESS;
}
