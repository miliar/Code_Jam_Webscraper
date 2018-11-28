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
        int R, k, N; // R: run R times, k: hold k person once, N: N groups
        ifs >> R >> k >> N;
        vector<int> personCounts(N);
        for (int j = 0; j < N; ++j)
        {
            ifs >> personCounts[j];
        }
        int totalCost = 0;
        int cursor = 0;
        for (int j = 0; j < R; ++j)
        {
            int groupCount = 0;
            int hold = 0;
            while (hold + personCounts[cursor] <= k && groupCount < N)
            {
                hold += personCounts[cursor];
                totalCost += personCounts[cursor];
                cursor++;
                cursor = cursor % N;
                groupCount ++;
            }
        }
        cout << "Case #" << i+1 << ": " << totalCost << endl;
    }
    ifs.close();
}

int main(int argc, char* argv[])
{
    char* filePath = argv[1];
    processInput(filePath);
}
