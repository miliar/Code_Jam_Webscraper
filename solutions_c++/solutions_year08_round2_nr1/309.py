#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long int Int;

int main()
{
    unsigned N;
    
    cin >> N;
    
    for (unsigned i = 0; i < N; ++i)
    {
        Int n, A, B, C, D, x0, y0, M;
        cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
        
        Int cntr[3][3];
        cntr[0][0] = cntr[0][1] = cntr[0][2] = 0;
        cntr[1][0] = cntr[1][1] = cntr[1][2] = 0;
        cntr[2][0] = cntr[2][1] = cntr[2][2] = 0;
        
        ++cntr[x0 % 3][y0 % 3];
        for (unsigned j = 1; j < n; ++j)
        {
            x0 = (A * x0 + B) % M;
            y0 = (C * y0 + D) % M;
            
            ++cntr[x0 % 3][y0 % 3];
        }
        
        Int answer = 0;
        
        for (unsigned j = 0; j < 9; ++j)
        {
            for (unsigned k = j; k < 9; ++k)
            {
                for (unsigned l = k; l < 9; ++l)
                {
                    if ((j / 3 + k / 3 + l / 3) % 3 != 0 || (j % 3 + k % 3 + l % 3) % 3 != 0) continue;
//                    cout << j << ": " << cntr[j / 3][j % 3] << "; " << k << ": " << cntr[k / 3][k % 3] << "; "<< l << ": " << cntr[l / 3][l % 3] << "; ";
                    
                    if (j == k && k == l)
                    {
                        Int base = cntr[j / 3][j % 3];
                        if (base >= 3) answer += base * (base - 1) * (base - 2) / 6;
                    }
                    else if (j == k)
                    {
                        Int base = cntr[j / 3][j % 3];
                        if (base >= 2) answer += base * (base - 1) / 2 * cntr[l / 3][l % 3];
                    }
                    else if (k == l)
                    {
                        Int base = cntr[k / 3][k % 3];
                        if (base >= 2) answer += base * (base - 1) / 2 * cntr[j / 3][j % 3];
                    }
                    else
                    {
                        answer += cntr[j / 3][j % 3] * cntr[k / 3][k % 3] * cntr[l / 3][l % 3];
                    }
//                    cout << answer << endl;
                }
            }
        }
        cout << "Case #" << (i + 1) << ": " << answer << endl;
    }
    return 0;
}

