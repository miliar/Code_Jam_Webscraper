#include <fstream>
#include <cassert>
#include <algorithm>

using namespace std;

unsigned int patrick_add(unsigned int a, unsigned int b)
{
    return (a | b) ^ (a & b);
}

bool back_cmp(unsigned int a, unsigned int b) { return a > b; }

int main()
{
    const char ifname[] = "C-large.in";
    const char ofname[] = "C-large.out";
    const int MAX_N = 1000;
    int T, t;
    int N, i, j;
    unsigned int C[MAX_N];
    unsigned int c;
    unsigned long int sum = 0;


    //assert(patrick_add(12, 5) == 9);
    //assert(patrick_add(5, 4) == 1);
    //assert(patrick_add(7, 9) == 14);
    //assert(patrick_add(50, 10) == 56);

    ifstream inf(ifname);
    ofstream ouf(ofname);


    inf >> T;

    for (t = 0; t < T; t++)
    {
        inf >> N;
        c = 0;
        for (i = 0; i < N; i++) {
            inf >> C[i];
            c = patrick_add(c, C[i]);
        }

        ouf << "Case #" << t + 1<< ": ";
        if (c) {
            ouf << "NO";
        } else {
            sort(C, C + N, back_cmp);

            sum = 0;
            for (i = 0; i < N - 1; i++)
            {
                sum += C[i];
            }
            ouf << sum;
        }
        ouf << endl;
    }

    
    inf.close();
    ouf.close();
    return 0;
}