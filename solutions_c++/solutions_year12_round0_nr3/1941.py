/*
ID: dhxav
PROG: recycled_numbers
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <ctime>
#include <cstdlib>
#include <map>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define CONST 10000

int main() {
    ifstream fin ("C-large.in");
    ofstream fout ("C-large.out");

    int T;
    fin >> T;

    forn (i,T)
    {
        int A, B, ans = 0;
        fin >> A >> B;

        int mult = 1, num = 0, temp = A/10;
        bool test;
        vector <int> buf;
        while (temp)
        {
            mult *= 10;
            num++;
            temp /= 10;
        }

        forab (j, A, B)
        {
            temp = j;
            buf.resize(0);
            forn (k,num)
            {
                temp = (temp%10)*mult + (temp/10);
                test = false;
                if (temp>=A && temp<=B && temp>j)
                {
                    test = true;
                    forn (l, buf.size())
                    {
                        if (buf[l]==temp)
                        {
                            test = false;
                            break;
                        }
                    }
                }
                if (test==true)
                {
                    buf.push_back(temp);
                    //fout << j << " " << temp << endl;
                    ans++;
                }
            }
        }

        if (A<10) ans = 0;
        fout << "Case #" << i+1 << ": " << ans << endl;
    }
}


