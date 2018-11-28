#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

int compare (const void * a, const void * b)
{
    return ( *(int*)b - *(int*)a );
}

int main()
{
    // N S P nnnnnnnnn
    ifstream in;
    ofstream out;

    in.open("B-small-attempt1.in");
    out.open("output.txt");

    int C;
    in >> C;
    for (int index = 0; index< C; index++) {
        int N , S , P;
        in >> N >> S >> P;

        int * T = new int[N];

        for (int var = 0; var < N; ++var) {
            in >> T[var];
        }

        qsort(T,N,sizeof(int),compare);

        for (int v = 0; v < N; ++v) {
            cout<< T[v]<<" ";
        }
        cout << endl;
        int count = 0;

        if (P == 0) {out<<"Case #"<<index+1<<": " <<N << endl;}
        else{
            for (int i = 0; i < N; ++i) {
                if((T[i]< ((P*3) - 4)) || (P>0 && T[i]==0)){ // rejected.
                    break;
                }
                if((T[i]< ((P*3) - 2))){ // needs surprise.
                    if (S < 1) break; // no surprises left.
                    S--;
                    count++;
                }
                if(T[i] > ((P*3) -3)) count++;
            }
        out<<"Case #"<<index+1<<": " <<count << endl;}
    }

    //    qsort();
    return 0;
}


