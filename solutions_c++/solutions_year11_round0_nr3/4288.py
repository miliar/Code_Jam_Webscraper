/* Author = Levan Kasradze */

#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main(int argc, char **argv) {
    ifstream fin("c.in", ios::in);
    ofstream fout("c.out", ios::out);

    int T;
    fin >> T;

    for (int i=1; i<=T; ++i) {
        fout << "Case #" << i << ": ";
        int N;
        fin >> N;
        int C[N];
        int SMAX = 0, SX = 0, SS = 0;

        for (int j=0; j<N; ++j) {
            fin >> C[j];
            SMAX |= C[j];
            SX ^= C[j];
            SS += C[j];
        }

	if (SX != 0) {
		fout << "NO" << endl;
		continue;
	}

        int bit = 31;
        while (bit > 0) {
            --bit;
            if ((SMAX & 1 << bit) != 0)
                break;
        }

        for (int j=0; j<=bit; ++j)
            SMAX |= 1 << j;


        int **Q = new int * [2];

        for (int j = 0; j < 2; j++) {
            Q[j] = new int [SMAX+1];
            for (int k=0; k<=SMAX; ++k)
                Q[j][k] = 0;
        }

        Q[0][C[0]] = C[0];
	int m = 0;
        for (int j=1; j<N; ++j) {
	    m = 1 - m;
	    
            for (int k=0; k<=SMAX; ++k) {
                if (Q[m][k] < Q[1-m][k])
                    Q[m][k] = Q[1-m][k];

                if (C[j] == k && Q[m][k] < C[j])
                    Q[m][k] = C[j];


                if (Q[1-m][k ^ C[j]] > 0 && Q[m][k] < Q[1-m][k ^ C[j]] + C[j])
                    Q[m][k] = Q[1-m][k ^ C[j]] + C[j];
		
		
                /*for (int lv=0; lv<=SMAX; ++lv)
                    cout << Q[1-m][lv] << " ";
                cout << endl;
                for (int lv=0; lv<=SMAX; ++lv)
                    cout << Q[m][lv] << " ";
                cout << endl;
		cout << endl;*/
				
            }
	}

        int cnt = 0;
        for (int k=0; k<=SMAX; ++k)
            if (Q[m][k] != 0 && Q[m][k] != SS && k == (k ^ SX) && cnt < Q[m][k])
                cnt = Q[m][k];

        if (cnt == 0)
            fout << "NO" << endl;
        else
            fout << cnt << endl;

        for (int j = 0; j < 2; j++)
            delete[] Q[j];
        delete[] Q;
        Q = 0;
    }

    fin.close();
    fout.close();
    return 0;
}
