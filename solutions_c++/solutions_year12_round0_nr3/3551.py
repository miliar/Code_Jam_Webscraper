#include <cstdlib>
#include <iostream>
#include <fstream>
#include "Map.h"
#include <math.h>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream in; ofstream out; in.open("./input.txt"); out.open("./output.txt");    
    int T = 0;
    long long A = 0, B = 0, cur = 0, vcur = 0, countdigits = 0, part = 0, d = 1, d1 = 1, ALL = 0;
    map <long long, long long> g;
    in >> T;
    for(int i = 0; i < T; i++){
        in >> A; in >> B;
        for(int j = A; j <= B; j++){
            cur = j;
            vcur = cur;
            while (vcur > 0) { countdigits++; vcur /= 10; }
            
            for(int k = 1; k < countdigits; k++){
                d = 1; d1 = 1;
                for(int t = 1; t <= k; t++) d *= 10;
                for(int t = 1; t <= countdigits - k; t++) d1 *= 10;
                part = (cur - (cur / d) * d) * d1 + (cur / d);
                
                if ((part > cur) && (part >= A) && (part <= B) && (g[cur] != part) && (g[part] != cur)) {
                    ALL++;
                    g[cur] = part;
                    
                }
            }
            countdigits = 0;
        }
        
        out << "Case #"<< i + 1 <<": " << ALL << endl;
        ALL = 0;
        g.clear();

    }
    in.close(); out.close(); system("PAUSE");
    return EXIT_SUCCESS;
}
