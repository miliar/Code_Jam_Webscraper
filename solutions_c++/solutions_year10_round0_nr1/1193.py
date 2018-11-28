#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream input;
    ofstream output;
    input.open("Alarge.in");
    output.open("Alarge.out");
    int t, ca = 0, n, k;
    bool p;
    input >> t;
    while (t > 0)
    {
        output << "Case #" << ++ca << ": ";
        input >> n >> k;
        k = k % (1 << n);
        p = true;
        while (n > 0)
        {
            if (k % 2 == 0)
            {
                p = false;
                break;
            } else k /= 2;
            n--;
        }
        if (p) output << "ON" << endl; else output << "OFF" << endl;
        t--;
    }
    input.close();
    output.close();
}
