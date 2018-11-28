#include <iostream>

using namespace std;

#include <fstream>
int main()
{
    ifstream infile("q2.in");
    ofstream outfile("q2.out");
    unsigned short T;
    char str[202];
    infile >> T;
    unsigned short N;
    unsigned short S;
    signed short p;

    signed long t;
    for (short test=0;test<T;test++)
    {
        infile >> N >> S >> p;
        unsigned short num = 0;
        int n=0;
        while (n<N)
        {
            infile >> t;
            if (t%3 == 0)
            {
                if (t / 3 >= p)
                    num++;
                else if ((t / 3 == p-1) && (S>0) && (t/3>0))
                {
                    S--;
                    num++;
                }
            }
            else if (t%3 == 1)
            {
                if ((t/3 >= p-1) )
                    num++;
            }
            else
            {
                if (t / 3 >= p-1)
                    num++;
                else if ((t / 3 == p-2) && (S>0))
                {
                    S--;
                    num++;
                }
            }
            n++;
        }
        outfile<<"Case #" << (test+1) << ": "<< num << "\n";
    }
    infile.close();
    outfile.close();
    return 0;
}
