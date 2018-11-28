#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>

using namespace std;

int d_cost, i_cost, diff, n, tt;
int p[101];
int i_num[256][256];
int S[101][256];
int L[101][256];

int main()
{
    ifstream input("B-large.in");
    ofstream output("B-large.out");
    
    input >> tt;
    for (int casenum = 0; casenum < tt; casenum++)
    {
        input >> d_cost >> i_cost >> diff >> n;
        for (int i = 0; i < n; i++) input >> p[i];
        
        for (int i = 0; i < 256; i++)
            for (int j = 0; j < 256; j++)
                if (i == j)
                    i_num[i][j] = 0;
                else if (diff != 0)
                {
                    i_num[i][j] = (abs(i-j)-1)/diff;
                    i_num[i][j] *= i_cost;
                }
                else
                    i_num[i][j] = 10000000;

        for (int v = 0; v < 256; v++)
        {
            S[0][v] = abs(v-p[0]);
            L[0][v] = S[0][v];
        }
        
        int ans = d_cost*(n-1);
        for (int m = 1; m < n; m++)
            for (int v = 0; v < 256; v++)
            {
                S[m][v] = d_cost*m;
                for (int u = 0; u < 256; u++)
                {
                    int cur = L[m-1][u] + d_cost*(m-1) + i_num[u][v];
                    if (cur < S[m][v]) S[m][v] = cur;
                }
                S[m][v] += abs(v-p[m]);
                
                int cur = S[m][v] + d_cost*(n-1-m);
                if (cur < ans) ans = cur;
                
                cur = S[m][v] - d_cost*m;
                L[m][v] = ((cur < L[m-1][v]) ? cur : L[m-1][v]);
            }
        
        output << "Case #" << casenum+1 << ": " << ans << endl;
    }
    
    input.close();
    output.close();
    return 0;
}
