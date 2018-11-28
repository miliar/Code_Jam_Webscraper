#include <vector>
#include <fstream>
#include <iostream>
using namespace std;

void processInput(const char* filePath)
{
    ifstream ifs;
    ifs.open(filePath);
    int T;
    ifs >> T;
    for (int i = 0; i < T; ++i)
    {
        int N, K;
        ifs >> N >> K;
        // number of 1 at the end
        int numberOf1 = 0;
        while (K & 0x1)
        {
            K = K >> 1;
            numberOf1 ++;
        }
        cout << "Case #" << i+1 << ": ";
        if (numberOf1 >= N)
        {
            cout << "ON" << endl;
        }
        else
        {
            cout << "OFF" << endl;
        }
    }
    ifs.close();
}

int main(int argc, char* argv[])
{
    char* filePath = argv[1];
    processInput(filePath);
}
