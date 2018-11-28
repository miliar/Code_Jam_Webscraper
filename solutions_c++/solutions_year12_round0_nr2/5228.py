#include<iostream>
#include<fstream>
using namespace std;

int main() {
    ifstream fin("input.in");
    ofstream fout("out.txt");
    int T, N, S, p, y = 0, x = 1, t[30] = {0}, d3 = 0, m3 = 0;
    fin >> T;
    while(x <= T) {
        fin >> N >> S >> p;
        for(int i = 0; i < N; i++)
            fin >> t[i];
        //////////////////////////////////////////
        for(int i = 0; i < N; i++) {
            //d3 = t[i] / 3;
            //m3 = t[i] % 3;
            if( S == 0) {
                if((p-1) < 0 || (p-2) < 0){
                    if(t[i] >= p)
                        y++;
                }
                else if(t[i] >= p + (2*p - 2))
                    y++;
            } else {
                if((p-1) < 0 || (p-2) < 0){
                    if(t[i] >= p)
                        y++;
                }
                else if(t[i] >= p + (2*p - 4))
                    y++;
            }

        }
        //////////////////////////////////////////
        fout << "Case #" << x << ": " << y << endl;
        x++;
        y = 0;
    }
    fout.close();
    return 0;
}
