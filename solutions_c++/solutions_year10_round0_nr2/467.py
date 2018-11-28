#include <stdlib.h>
#include <time.h>
#include <fstream>
#include <iostream>

using namespace std;

int gcd(int a, int b);

int main(int argc, char* argv[])
{
    fstream fIn, fOut;
    fIn.open("B-small-attempt0.in", fstream::in);
    fOut.open("Output.txt", fstream::out);

    int caseNum = 0;
    fIn >> caseNum;
    
    for(int i = 0; i < caseNum; i++)
    {
        int n = 0;
        fIn >> n;
        int t[1000];
        int diff[1000];
        int g;

        for(int j = 0; j < n; j++)
        {
            fIn >> t[j];
        }
        for(int j = 0; j < n - 1; j++)
        {
            diff[j] = abs(t[j] - t[j + 1]);
        }
        g = 0;
        for(int j = 0; j < n - 1; j++)
        {
            g = gcd(g, diff[j]);
        }
        //cout << g << endl;

        int add = g - (t[0] % g);
        if(add == g)
            add = 0;

        fOut << "Case #" << i + 1 << ": " << add << endl;

    }

    fIn.close();
    fOut.close();

    return 0;
}

int gcd(int a, int b)
{
    if(a < b)
    {
        int t = a;
        a = b;
        b = t;
    }

    if(b == 0)
        return a;
    else
        return gcd(b, a % b);
}