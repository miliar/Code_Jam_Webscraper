#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    ifstream in("A.in");
    ofstream out("A.out");
    
    int T, k;
    int diamond[51][51];
    in >> T;
    
    for (int tc = 1; tc <= T; ++tc)
    {
        in >> k;
        
        for (int i = 1; i < k; ++i)
        {
            for (int j = 1; j <= i; ++j)
            {
                in >> diamond[i-j][j-1];
            }
        }
        for (int i = k; i < 2*k; ++i)
        {
            for (int j = 1; j <= 2*k - i; ++j)
            {
                in >> diamond[k-j][i+j-k-1];
            }
        }
        
        int minSize = 9*k;
        
        for (int ci = -k; ci < 2*k; ++ci)
        {
            for (int cj = -k; cj < 2*k; ++cj)
            {
                bool match1 = true;
                bool match2 = true;
                int testSize1 = max(max(2*ci+1,2*(k-ci)-1), max(2*cj+1,2*(k-cj)-1));
                int testSize2 = max(max(2*ci+2,2*(k-ci)-2), max(2*cj+2,2*(k-cj)-2));
                
                if (minSize <= testSize1 && minSize <= testSize2)
                    continue;
                
                for (int i = 0; (match1 || match2) && i < k; ++i)
                {
                    for (int j = 0; j < k; ++j)
                    {
                        int ri1 = ci + j - cj;
                        int rj1 = cj + i - ci;
                        int ri2 = - j + ci + cj;
                        int rj2 = - i + ci + cj;
                        int ri3 = ri2 + 1;
                        int rj3 = rj2 + 1;
                        
                        if (0 <= ri1 && ri1 < k && 0 <= rj1 && rj1 < k && diamond[i][j] != diamond[ri1][rj1])
                        {
                            match1 = false;
                            match2 = false;
                        }
                        if (0 <= ri2 && ri2 < k && 0 <= rj2 && rj2 < k && diamond[i][j] != diamond[ri2][rj2])
                            match1 = false;
                        if (0 <= ri3 && ri3 < k && 0 <= rj3 && rj3 < k && diamond[i][j] != diamond[ri3][rj3])
                            match2 = false;
                        //out << "checking " << ci << cj << i << j << match1 << match2 << endl;
                    }
                }
                if (match1)
                    minSize = min(minSize, testSize1);
                if (match2)
                    minSize = min(minSize, testSize2);
                //if (match1 || match2)
                    //out << "debug " << ci << cj << testSize1 << testSize2 << endl;
            }
        }
        
        /*for (int i = 0; i < k; ++i)
        {
            for (int j = 0; j < k; ++j)
                out << diamond[i][j];
            out << endl;
        }*/
        
        out << "Case #" << tc << ": " << (minSize*minSize - k*k) << endl;
    }
    
    in.close();
    out.close();
    return 0;
}
