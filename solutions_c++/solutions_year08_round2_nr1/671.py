#include <iostream>
#include<fstream>
#include<algorithm>
using namespace std;

const int maxN = 100000;

typedef struct TCoord {
        long long x, y;
};
TCoord Verticles[maxN + 1];
long IndexCount[4];

bool CenterAtGridPoint() {
        long X, Y;
        X = (Verticles[IndexCount[1]].x + Verticles[IndexCount[2]].x + 
             Verticles[IndexCount[3]].x);
        Y = (Verticles[IndexCount[1]].y + Verticles[IndexCount[2]].y + 
             Verticles[IndexCount[3]].y);
        if (((X % 3)==0)&&(Y % 3)==0)
                return true;
        else
                return false;
}

bool NextPP() {
        if (IndexCount[3] < Verticles[0].x) {
                IndexCount[3]++;
                return true;
        } else if (IndexCount[2] < Verticles[0].x-1) {
                IndexCount[2]++;
                IndexCount[3] = IndexCount[2]+1;
                return true;
        } else if (IndexCount[1] < Verticles[0].x-2) {
                IndexCount[1]++;
                IndexCount[2] = IndexCount[1]+1;
                IndexCount[3] = IndexCount[2]+1;
                return true;
        } else
                return false;
}

long long CountTrees() {
        long long Ans = 0;
        IndexCount[1] = 1;
        IndexCount[2] = 2;
        IndexCount[3] = 3;
        if (CenterAtGridPoint())
                Ans++;
        while (NextPP()) {
                if (CenterAtGridPoint())
                        Ans++; 
        }
        return Ans;
        
}

int main () {
        ifstream fin("CTriangles.in");
        ofstream fout("CTriangles.out");
        int N;
        fin >> N;
        for (int i = 1; i <= N; i++) {
                long long n, A, B, C, D, x0, y0, M, X, Y;
                fin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
                Verticles[0].x = n;
                Verticles[1].x = x0;
                Verticles[1].y = y0;
                X = x0;
                Y = y0;
                for (long i2 = 2; i2 <= n; i2++) {
                        X = ((A * X) + B) % M;
                        Y = ((C * Y) + D) % M;
                        Verticles[i2].x = X;
                        Verticles[i2].y = Y;
                }
                fout << "Case #" << i << ": " << CountTrees() << endl;
        }
        fin.close();
        fout.close();
        return 0;
}
