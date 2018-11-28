#include <iostream>
#include <string>
#include <sstream>

using namespace std;

bool test(int num, int base);

int main()
{
    int t;
    int b[10];
    int bnum;
    int testb;
    char buf[101];
    string input;
    istringstream reinput;
    cin >> t;
    cin.getline(buf, 100);
    for (int i = 1; i <= t; i++)
    {
        cin.getline(buf, 100);
        string s = buf;
        reinput.clear();
        reinput.str(s);
        bnum = 0;
        while (reinput >> b[bnum])
            ++bnum;

        for (int ans = 2; 1; ans++)
        {
            for (testb = 0; testb < bnum; testb++)
            {
                //cout << "test (" << ans << ", " << b[testb] << ") = " << test(ans, b[testb]) << endl;
                if (!test(ans, b[testb]))
                    break;
            }
            // pass all
            if (testb == bnum) 
            {
                cout << "Case #" << i << ": " << ans << endl;
                break;
            }
        }
    }
    return 0;
}

int calc(int num, int base)
{
    int t = 0;
    while (num >= base)
    {
        t += (num % base) * (num % base);
        num /= base;
    }
    t += num * num;
    return t;
}

bool test(int num, int base)
{
    int num1 = num;
    if (base == 2) return true;
    while (num != 1)
    {
        num = calc(num, base);
        if (num == 1) return true;
        num1 = calc(num1, base);
        if (num1 == 1) return true;
        num1 = calc(num1, base);
        if (num1 == 1) return true;
        if (num == num1) return false;
    }
    // only ET can get here
    return true;
}

