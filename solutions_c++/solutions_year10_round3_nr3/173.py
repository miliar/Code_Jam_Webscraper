#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int checkifok(vector<string> &bark, int x, int y, int sz)
{
    if(y + sz > bark.size() || x + sz > bark[0].size())
        return 0;

    for(int i = x; i < x + sz; ++i)
    {
        if(i > x)
            if(bark[y][i - 1] == bark[y][i])
                return 0;

        for(int j = y; j < y + sz; ++j)
        {
            if(j > y)
                if(bark[j - 1][i] == bark[j][i])
                    return 0;

            if(bark[j][i] == '-')
                return 0;
        }
    }

    return 1;
}

void nullify(vector<string> &bark, int x, int y, int sz)
{
    for(int i = x; i < x + sz; ++i)
    {
        for(int j = y; j < y + sz; ++j)
        {
            bark[j][i] = '-';
        }
    }
}

int main( int argc, char* argv[] )
{
    FILE *fr = fopen("C-small.in", "r");
    FILE *fw = fopen("C-small.out", "w");

    int T;
    fscanf(fr, "%d", &T);
    for(int t = 0; t < T; ++t)
    {
        int M, N;
        fscanf(fr, "%d %d", &M, &N);

        char buf[1024];
        vector< string > bark(M);

        N >>= 2;
        for(int i = 0; i < M; ++i)
        {
            string s;
            fscanf(fr, "%s", buf);
            for(int j = 0; j < N; ++j)
            {          
                if(buf[j] >= '0' && buf[j] <= '9')
                    buf[j] -= '0';
                else
                    buf[j] = buf[j] - 'A' + 10;

                int p = 0x08;

                while(p)
                {
                    if((buf[j] & p) != 0)
                        s += '1';
                    else 
                        s += '0';

                    p >>= 1;
                }
            }

            bark[i] = s;
        }

        int W = N << 2, H = M;

        map<int, int> ans;

        for(int ss = min(W, H); ss >= 1; --ss)
        {
            for(int y = 0; y < H; ++y)
            {
                for(int x = 0; x < W; ++x)
                {
                    if(checkifok(bark, x, y, ss))
                    {

                        int q = ans[ss];
                        ans[ss] = q + 1;

                        nullify(bark, x, y, ss);
                    }
                }
            }
        }

        vector< pair< int, int> > ww;
        for(map<int, int> ::iterator it = ans.begin(); it != ans.end(); ++it)
        {
            ww.push_back(pair<int, int>(it->first, it->second));
        }

        sort(ww.rbegin(), ww.rend());

        fprintf(fw, "Case #%d: %d\n", t + 1, ww.size());
        for(int i = 0; i < ww.size(); ++i)
        {
            fprintf(fw, "%d %d\n", ww[i].first, ww[i].second);
        }
    }

    fclose(fr);
    fclose(fw);

    return 0;
}