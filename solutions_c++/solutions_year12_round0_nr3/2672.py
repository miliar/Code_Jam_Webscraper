#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int ndigits(int n)
{
    if(n<10) return 1;
    if(n<100) return 2;
    if(n<1000) return 3;
    if(n<10000) return 4;
    if(n<100000) return 5;
    if(n<1000000) return 6;
    if(n<10000000) return 7;
}

int multiplier(int n)
{
    switch(n)
    {
    case 2: return 10;
    case 3: return 100;
    case 4: return 1000;
    case 5: return 10000;
    case 6: return 100000;
    case 7: return 1000000;
    default: return 0;
    }
    return 0;
}

int numrecycled(int A, int B)
{
    int l = ndigits(A);
    int mult = multiplier(l);
    int count = 0;

    int used[6];
    int ucount;

    for(int i=A; i<=B; ++i)
    {
        int candidate = i;
        ucount = 0;
        for(int j=0; j<l-1; ++j)
        {
            int lsd = candidate%10;
            candidate /= 10;
            candidate += lsd * mult;
            if( candidate > i && candidate <= B )
            {
                bool found = false;

                for(int k=0; k<ucount; ++k)
                {
                    if(used[k]==candidate)
                    {
                        found = true;
                    }
                }
                if(!found)
                {
                    used[ucount++] = candidate;
                    count++;
                }
            }
        }
    }
    return count;
}

int main(int argc, char* argv[])
{
    ifstream infile;
    ofstream outfile;
    
//    infile.open( "/Users/Guy/Downloads/C-small-attempt0.in");
    infile.open( "/Users/Guy/Downloads/C-large.in");
//    infile.open( "/gcjam/input.txt");
    outfile.open( "/gcjam/output.txt");

    int ntestcases;
    infile >> ntestcases;
    infile.ignore(1, '\n');

    for(int i=0; i<ntestcases; ++i)
    {
        int A, B;
        infile >> A;
        infile >> B;

        outfile << "Case #" << i+1 << ": " << numrecycled(A, B) << endl;
        cout << "Case #" << i+1 << ": " << numrecycled(A, B) << endl;
    }
	return 0;
}