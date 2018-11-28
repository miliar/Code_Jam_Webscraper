#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

int T, P, N;
VI M, price;
VVI maxcost;

int main()
{
    ifstream input("B-large.in");
    ofstream output("B-large.out");
    input >> T;
    for (int casenum = 0; casenum < T; casenum++)
    {
        input >> P;
        N = (1 << P);
        M.resize(N);
        for (int i = 0; i < N; i++) input >> M[N-1-i];
        price.resize(N-1);
        for (int i = 0; i < N-1; i++) input >> price[N-2-i];
        maxcost.resize(2*N-1);
        for (int i = 0; i < 2*N-1; i++) maxcost[i].resize(P+1);
        for (int i = 2*N-2; i >= 0; i--)
            for (int j = 0; j <= P; j++)
                if (i >= N-1)
                {
                    maxcost[i][j] = 0;
                    if (j > M[i-N+1]) maxcost[i][j] = -1;
                }
                else
                {
                    maxcost[i][j] = -1;
                    if (j < P && maxcost[2*i+1][j+1] >= 0 && maxcost[2*i+2][j+1] >= 0) 
                        maxcost[i][j] = price[i] + maxcost[2*i+1][j+1] + maxcost[2*i+2][j+1];
                    if (maxcost[2*i+1][j] >= 0 && maxcost[2*i+2][j] >= 0)
                    {
                        int c2 = maxcost[2*i+1][j] + maxcost[2*i+2][j];
                        if (maxcost[i][j] < 0 || (maxcost[i][j] >= 0 && c2 > maxcost[i][j])) maxcost[i][j] = c2;
                    }
                }
        int total = 0;
        //output << "maxcost==" << maxcost[0][0] << endl;
        for (int i = 0; i < N-1; i++) total += price[i];
        output << "Case #" << casenum+1 << ": " << total-maxcost[0][0] << endl;
    }
    input.close();
    output.close();
    return 0;
}
