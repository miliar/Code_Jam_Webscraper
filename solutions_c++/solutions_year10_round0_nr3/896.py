#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int g[1000];
int next[1000];
int euro[1000];

int main()
{
    ifstream in("C.in");
    ofstream out("C.out");
    
    int T;
    in >> T;
    
    for (int tc = 1; tc <= T; ++tc)
    {
        int R, k, N;
        in >> R >> k >> N;
        
        for (int i = 0; i < N; ++i)
        {
            in >> g[i];
        }
        for (int i = 0; i < N; ++i)
        {
            int vacancy = k;
            int j = 0;
            while (j < N && vacancy >= g[(i+j)%N])
            {
                vacancy -= g[(i+j)%N];
                j++;
            }
            next[i] = (i+j)%N;
            euro[i] = k - vacancy;
        }
        
        long long totalEuro = 0;
        int nextGroup = 0;
        for (int i = 0; i < R; ++i)
        {
            totalEuro += euro[nextGroup];
            nextGroup = next[nextGroup];
        }
        out << "Case #" << tc << ": ";
        out << totalEuro << endl;
    }
    
    in.close();
    out.close();
    return 0;
}
