#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int T, N, K;

int main()
{
    ifstream input("A.in");
    ofstream output("A.out");
    input >> T;
    for (int c = 0; c < T; c++)
    {
        input >> N >> K;
        int M = (1 << N);
        K %= M;
        output << "Case #" << c+1 << ": ";
        if (K == M-1)
            output << "ON" << endl;
        else
            output << "OFF" << endl;
    }
    input.close();
    output.close();
    return 0;
}
