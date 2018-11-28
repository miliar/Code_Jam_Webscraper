#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <cstdlib>
using namespace std;
const char TEXT[] = "welcome to code jam";
#define MAX sizeof(TEXT)
int M[256][MAX] = { };
int C[MAX] = { };
int main()
{
    for (int i = 0; i < MAX; ++i) { 
        int j = 0;
        for (; M[TEXT[i]][j]; ++j);
        M[TEXT[i]][j] = i + 1;
    }
    string input;
    getline(cin, input);
    int N = atoi(input.c_str());
    for (unsigned i = 1; i <= N; ++i) {
        getline(cin, input);
        for (int i = 0; i < MAX; ++i)
            C[i] = 0;
        for (int i = 0; i < input.length(); ++i) {
            for (int j = MAX; j--;) {
                int L = M[input[i]][j];
                if (!L) continue;
                if (L == 1) ++C[L];
                else C[L] += C[L - 1];
                C[L] %= 10000;
            }
        }
        cout << "Case #" << i << ": " << setfill('0') << setw(4) << C[MAX - 1] << "\n";
    }
}
