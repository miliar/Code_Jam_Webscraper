#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int T,N,S,p;
int t[200];

int main()
{
    ifstream fin("B_in.txt");
    ofstream fout("B_out.txt");

    fin >> T;
    for(int cnt = 1;cnt <= T;++cnt)
    {
        fin >> N >> S >> p;
        for(int j = 0;j < N;++j)
            fin >> t[j];
        int M1 = 3*p - 2;
        int M2 = 3*p - 4;
        if(M1 < p)
            M1 = p;
        if(M2 < p)
            M2 = p;
        int x1 = 0;
        int x2 = 0;
        for(int j = 0;j < N;++j)
        {
            if(t[j] >= M1)
                ++x1;
            else if(t[j] >= M2)
                ++x2;
        }
        int ans = x1;
        if(x2 <= S)
            ans += x2;
        else
            ans += S    ;
        fout << "Case #" << cnt << ": " << ans << endl;
    }
    return 0;
}
