/*
NAME: Saketh Are
PROG: Roller Coaster
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

ifstream fin("coaster.in");
ofstream fout("coaster.out");

int T, R, N, K;
int groups[1005];

int main()
{
    fin >> T;
    for(int q = 0; q<T; q++)
    {
            fin >> R >> K >> N;
            for(int c = 0; c<N; c++)
            {
                    int size;
                    fin >> size;
                    groups[c] = size;
            }
            long long E = 0, L = 0, O = 0;
            for(int run = 0; run<R; run++)
            {
                    int S = 0;
                    while(true)
                    {
                               int add = groups[L%N];
                               if(S+add<=K)
                               {
                                           S+=add;
                                           L++;
                                           if((L%N)==(O%N))
                                                       break;
                               }
                               else
                                   break;
                    }
                    O = L;
                    E+=S;
            }
            fout << "Case #" << q+1 << ": " << E << "\n";
    }
    return 0;
}
