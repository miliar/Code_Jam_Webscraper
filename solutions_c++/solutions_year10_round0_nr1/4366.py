/*
NAME: Saketh Are
PROG: Snapper Chain
LANG: C++
*/

#include<iostream>
#include<fstream>
#include<queue>
#include<string>
#include<bitset>
#include<stdlib.h>
#include<cmath>

using namespace std;

ifstream fin("snapper.in");
ofstream fout("snapper.out");

int T, N, K;
bool snappers[32];

int main()
{
    fin >> T;
    for(int q = 0; q<T; q++)
    {
            fin >> N >> K;
            for(int c = 0; c<32; c++)
                    snappers[c] = false;
            for(int s = 0; s<K; s++)
            {
                    for(int c = 0; c<N; c++)
                    {
                            snappers[c] = !snappers[c];
                            if(snappers[c])
                                   break;
                    }
            }
            bool on = true;
            for(int c = 0; c<N; c++)
                    if(!snappers[c])
                    {
                                    on = false;
                                    break;
                    }
            fout << "Case #" << q+1 << ": " << (on?"ON\n":"OFF\n");
    }
    return 0;
}
