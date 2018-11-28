#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

const int maxN = 800;

typedef long long TVectorArr[maxN + 1];

long long MinScallarProd(TVectorArr a, TVectorArr b, int N) {
        sort(a+1, a+N+1);
        sort(b+1, b+N+1);
        reverse(b+1, b+N+1);
        TVectorArr Rez;
        long long Sum = 0;
        for(int i = 1; i <= N; i++) {
                Rez[i] = a[i]*b[i];
        }
        for(int i = 1; i <= N; i++) {
                Sum += Rez[i];
        }
        return Sum;
}

int main () {
        TVectorArr Vector1, Vector2;
        ifstream fin("msp.in");
        ofstream fout("msp.out");
        int T, n;
        fin >> T;
        for(int i = 1; i <= T; i++) {
                fin >> n;
                for(int u = 1; u <= n ; u++) 
                        fin >> Vector1[u];
                for(int u = 1; u <= n ; u++) 
                        fin >> Vector2[u];
                fout << "Case #" << i << ": " << MinScallarProd(Vector1, Vector2, n) << endl;
        }
        fin.close();
        fout.close();
        return 0;
}
