#include <cstdlib>
#include <iostream>
#include <fstream>
#include "Map.h"
#include <math.h>

using namespace std;

int getm(int x, int d){
    return (x % d == 0) ? x / d : x / d + 1;
}

int main(int argc, char *argv[])
{
    ifstream in; ofstream out; in.open("./input.txt"); out.open("./output.txt");
    int T = 0; in >> T;
    int N = 0, S = 0, p = 0, tp = 0,
    n1 = 0, n2 = 0, n3 = 0, ALL = 0;
    
    for(int i = 0; i < T; i++){
        in >> N; in >> S; in >> p;
        for(int j = 0; j < N; j++){
            in >> tp;

            n1 = getm(tp, 3);
            n2 = getm(tp - n1, 2);
            n3 = tp - n1 - n2;

            if (n1 >= p){
                if (n1 - n3 <= 2) { ALL++; }

            } else {
                if ((n2 == n1) && (S > 0) && (n2 > 0) && (n1 + 1 >= p))
                    if (n1 - n3 <= 2) {
                        ALL++; S--; n1++; n2--;
                    }
            }
        }

        out << "Case #" << i + 1 << ": " << ALL << "\n";
        ALL = 0;
    }
    in.close(); out.close(); system("PAUSE");
    return EXIT_SUCCESS;
}
