#include <iostream>
#include <fstream>

using namespace std;

struct node
{
    int but;
    int i;
};
ifstream fin("A-small-attempt4.in", ios::in);
ofstream fout("A-small-attempt4.out", ios::out);

int main()
{
    int ans, t, n;
    char r;
    int i, j;
    int pos[2];
    struct node op[2][105];
    int po, pb;
    int step;
    fin >> t;
    for(i = 1; i <= t; ++i)
    {
        fin >> n;
        ans = 0;
        pos[0] = pos[1] = 1;
        po = pb = 0;
        op[0][0].i = op[1][0].i = -1;
        for(j = 0; j < n; ++j)
        {
            fin >> r;
            if(r == 'O')
            {
                fin >> op[0][po].but;
                op[0][po].i = j;
                ++po;
            }
            else
            {
                fin >> op[1][pb].but;
                op[1][pb].i = j;
                ++pb;
            }
        }
        for(po = pb = j = 0; j < n; ++j)
        {
            if(op[0][po].i == j)
            {
                step = op[0][po].but - pos[0];
                if(step < 0)
                    step = -step;
                ++step;
                ans += step;
                if(pos[1] < op[1][pb].but)
                {
                    pos[1] += step;
                    if(pos[1] > op[1][pb].but)
                        pos[1] = op[1][pb].but;
                }
                else if(pos[1] > op[1][pb].but)
                {
                    pos[1] -= step;
                    if(pos[1] < op[1][pb].but)
                        pos[1] = op[1][pb].but;
                }
                pos[0] = op[0][po].but;
                ++po;
            }
            else
            {
                step = op[1][pb].but - pos[1];
                if(step < 0)
                    step = -step;
                ++step;
                ans += step;
                if(pos[0] < op[0][po].but)
                {
                    pos[0] += step;
                    if(pos[0] > op[0][po].but)
                        pos[0] = op[0][po].but;
                }
                else if(pos[0] > op[0][po].but)
                {
                    pos[0] -= step;
                    if(pos[0] < op[0][po].but)
                        pos[0] = op[0][po].but;
                }
                pos[1] = op[1][pb].but;
                ++pb;
            }
        }
        fout << "Case #" << i << ": " << ans << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
