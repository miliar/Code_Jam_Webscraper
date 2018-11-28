#include <vector>
#include <map>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>

using namespace std;

void runCase(ifstream& in)
{
    int numBits;
    int snaps;
    in >> numBits;
    in >> snaps;
    int maxInt = pow(2, numBits);
    int target = maxInt -1;
    int snaps2 = snaps % maxInt;
    cout << ((target == snaps2) ? "ON" : "OFF");
}

int main(int argc, char* argv[])
{
    char filename[256];
    cin.width(256);
    cin >> filename;
    ifstream file(filename);
    int cases;
    file >> cases;
    for (int i = 0; i < cases; i++)
    {
        cout << "Case #" << (i+1) << ": ";
        runCase(file);
        cout << endl;
    }
    return 0;
}
