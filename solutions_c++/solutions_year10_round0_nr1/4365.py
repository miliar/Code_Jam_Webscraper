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
        vector<bool> states(N, false);
        for (int j = 0; j < K; ++j)
        {
            int k = 0;
            while (states[k] && k < N)
            {
                states[k] = false;
                k++;
            }
            states[k] = true;
        }
        bool on = true;
        for (int j = 0; j < N; ++j)
        {
            if (!states[j])
            {
                on = false;
                break;
            }
        }
        cout << "Case #" << i+1 << ": ";
        if (on)
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
