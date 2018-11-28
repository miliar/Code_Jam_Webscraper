#include <stdio.h>
#include <stdlib.h>
#include<iostream>
#include<fstream>
using namespace std;

int compare (const void * a, const void * b){
  return ( *(int*)a - *(int*)b );
}

int main() {
    ifstream fin("B-small-attempt0.in");
    ofstream fout("out.txt");
    int T, N, S, p, y = 0, x = 1, t[100] = {0}, d3 = 0, m3 = 0;
    fin >> T;
    while(x <= T) {
        fin >> N >> S >> p;
        for(int i = 0; i < N; i++)
            fin >> t[i];
        //////////////////////////////////////////
        qsort (t, N, sizeof(int), compare);
        for(int i = 0; i < N; i++) {
            d3 = t[i] / 3;
            m3 = t[i] % 3;
            if( S > 0 && (p - 2) >= 0) {
                if(t[i] >=  (p + (2 * p - 4))) {
                    y++;
                    S--;
                }
            } else {
                if(t[i] >= (p + (2 * p - 2)))
                    y++;
            }
        }
        //////////////////////////////////////////
        fout << "Case #" << x << ": " << y << endl;
        x++;
        y = 0;
    }
    fout.close();
    system("\"C:\\Users\\lenovo\\Documents\\Visual Studio 2010\\Projects\\CodeJam B\\CodeJam B\\out.txt\"");
    return 0;
}