#include <iostream>
#include <sstream>
#include <algorithm>
#include <fstream>

using namespace std;

void SnapperChain()
{
    unsigned int T,N,rem,iter;
    unsigned long long K;
    string STATE;

    fstream input("A-small.in", fstream::in);
    fstream output("A-small.out", fstream::out);

    input >> T;

    for(unsigned int i=0;i<T;i++)
    {
        input >> N >> K;

        iter = 0;
        STATE = "OFF";
        while(K > 0)
        {
            rem = K % 2;
            K = K/2;
            iter++;

            if(rem==0)
            {
                STATE = "OFF";
                break;
            }
            else if(rem==1 && iter==N)
            {
                STATE = "ON";
                break;
            }
            else if(rem==1)
            {
                continue;
            }
        }

        output << "Case #" << i+1 << ": " << STATE << endl;

    }

    input.close();
    output.close();
}