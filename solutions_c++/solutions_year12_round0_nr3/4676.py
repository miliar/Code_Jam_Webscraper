//C:\Users\Stefan Dessens\Desktop\google code jam\contest C\ContestC-build-desktop
#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <set>
using namespace std;

int algorithm(int, int);
int rotate(int);

//globals:
int totalDigits;
int totalDigitsPower;

int main(int argc, char *argv[])
{
    stringstream lineStream;
    string line;
    int totalLines;

    ifstream inputFile;
    inputFile.open ("C:/Users/Stefan Dessens/Desktop/google code jam/contest C/input.txt");
    ofstream outputFile;
    outputFile.open ("C:/Users/Stefan Dessens/Desktop/google code jam/contest C/output.txt");

    getline(inputFile, line);
    istringstream(line) >> totalLines;

    int min, max;
    int result;


    for(int i = 1; i <= totalLines; i++)
    {
        getline(inputFile, line);
        istringstream(line) >> min >> max;
        result = algorithm(min, max);
        cout << "algorithm(" << min << ", " << max << ") --> " << result << endl;
        outputFile << "Case #" << i << ": " << result << endl;

    }

    inputFile.close();
    outputFile.close();
    cout << endl << "done" << endl;
    cin.get();
}

int algorithm(int min, int max)
{
    set<pair<int, int> > pairs;
    totalDigits = log10(min)+1;
    totalDigitsPower = pow(10, totalDigits - 1);
    int totalPairs = 0;

    int temp = min;
    for(int n = min; n <= max; n++)
    {
        temp = n;
        for(int r = 1; r < totalDigits; r++)
        {
            temp = rotate(temp);
            if ((temp > n) && (temp <= max))
            {
                if (pairs.find(pair<int, int>(n, temp)) == pairs.end())
                {
                    pairs.insert(pair<int, int>(n, temp));
                    totalPairs++;

                }

            }
        }
    }
    return totalPairs;
}

int rotate(int in)
{
    int firstDigit = in / totalDigitsPower;
    return (in - firstDigit * totalDigitsPower) * 10 + firstDigit;
}
