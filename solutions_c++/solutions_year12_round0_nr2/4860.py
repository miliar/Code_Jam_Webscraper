#include <iostream>
#include <string.h>
#include <fstream>

using namespace std;

int t[200];
int N, p, S; 
int f[200][200];

int maxNumSur(int in){
    int tmp; 
    if ((in + 2) % 3 == 0) tmp = (in + 2) / 3;
    else {
         if ((in + 3) % 3 == 0) tmp = (in + 3) / 3;
         else tmp = (in + 4) / 3;
    }
    if (tmp < 2) return 0;
    if (tmp >= p) return 1;
    else return 0;
}

int maxNumUnSur(int in){
    int tmp; 
    if ((in) % 3 == 0) tmp = (in) / 3;
    else {
         if ((in + 1) % 3 == 0) tmp = (in + 1) / 3;
         else tmp = (in + 2) / 3;
    }
    if (tmp >= p) return 1;
    else return 0;
}

int doit(){
    int i, j;
    f[0][0] = 0;
    
    for (i = 1; i <= N; i++){
        for (j = 0; j <= i; j++){
            int m1, m2;
            m1 = f[i - 1][j] + maxNumUnSur(t[i]);
            if (j == 0) m2 = -1000;
            else m2 = f[i - 1][j - 1] + maxNumSur(t[i]);
            f[i][j] = (m1 > m2)? m1 : m2;
        }
    }
       
    return f[N][S];
} 

int main(int argc, char *argv[])
{
    ifstream fin("B-large.in");
    ofstream fout("output.txt");

    int T;
    fin >> T;
    int i;
    for (i = 0; i < T; i++){
        fin >> N >> S >> p;
        int j;
        for (j = 1; j <= N; j++) fin >> t[j];
        
        fout << "Case #" << i + 1 << ": " << doit() << endl;
    }

    system("PAUSE");
    return EXIT_SUCCESS;
}
