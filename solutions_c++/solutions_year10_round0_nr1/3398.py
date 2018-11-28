#include <iostream>
#include <fstream>
#include <cstdlib> // for exit function
// This program reads values from the file 'example.dat'
// and echoes them to the display until a negative value
// is read.

#include <string>

using namespace std;

unsigned long long generateMask(unsigned long long snappers)
{
    unsigned long long res = 1;
    unsigned long long i;
    for (i = 0; i < snappers; i++)
    {
        res *= 2;
    }

    res--;

    return res;
}

void check(unsigned long long n,unsigned long long k)
{
    unsigned long long mask = generateMask(n);
    if ((k & mask) == mask)
        printf("ON\n");
    else
        printf("OFF\n");
}

int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s file.in\n", argv[0]);
        return -1;
    }

    ifstream indata; // indata is like cin
    indata.open(argv[1]); // opens the file

    if(!indata) { // file couldn't be opened
        cerr << "Error: file could not be opened" << endl;
        exit(1);
    }

    int x;
    indata >> x;
    int i;
    for (i = 1; i <= x; i++)
    {
        unsigned long long n, k;
        indata >> n >> k;

        printf("Case #%d: ",i);
        check(n,k);
    }

    indata.close();

    return 0;
}
