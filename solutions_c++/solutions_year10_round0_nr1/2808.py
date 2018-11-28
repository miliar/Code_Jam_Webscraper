#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

long long int Ks[35] = { 1, 3, 7, 15, 31, 63, 127, 255,           //Ks[n]=2*Ks[n-1]+1
               511, 1023, 2047, 4095, 8191, 16383,
               32767, 65535, 131071, 262143, 524287,
               1048575, 2097151, 4194303, 8388607,
               16777215, 33554431, 67108863, 134217727,
               268435455, 536870911, 1073741823 };

int T, N, K;


int main()
{
    ifstream sisend("A-large.in");
    ofstream valjund("A-large.out");

    sisend >> T;

    for(int u = 1; u<=T; u++)
    {
        sisend >> N >> K;
        int temp=0;
        while(1)
        {
            temp++;
            if(K==(temp*(Ks[N-1]+1)-1))
            {
                valjund << "Case #" << u << ": ON\n";
                break;
            }
            if(K<(temp*(Ks[N-1]+1)-1))
            {
                valjund << "Case #" << u << ": OFF\n";
                break;
            }
        }
    }

    return 0;
}
