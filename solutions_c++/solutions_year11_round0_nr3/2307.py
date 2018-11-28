/*
NAME: Saketh Are
PROG: Candy Splitting
LANG: C++
*/

#include<fstream>
using namespace std;

ifstream fin("csplit.in");
ofstream fout("csplit.out");

int T, N, M, S, X, V;

int main()
{
    fin >> T;
    for(int q = 0; q<T; q++){
        X=S=0; fin >> N;
        M = 1000001;
        for(int n=0; n<N; n++){
            fin >> V;
            S+=V;
            M = min(M, V);
            X^=V;
        }
        fout << "Case #" << q+1 << ": ";
        if(X==0) fout << S-M << endl;
        else fout << "NO" << endl;
    }
    return 0;
}
