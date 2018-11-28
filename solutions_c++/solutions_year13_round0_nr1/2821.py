#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>

#define FOR(i,n) for (int i = 0 ; i< n;i++)
#define FORI(i,s,e) for (int i = s ; i<= e;i++)
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define RALL(x) x.rbegin(),x.rend()
#define SZ(x) x.size()
#define FZ(x) memset(x,0,sizeof(x))


using namespace std;

int dpx;
int dpo;
int dpt;

int dsx;
int dso;
int dst;

int lx[4];
int lo[4];
int lt[4];

int cx[4];
int co[4];
int ct[4];

int main()
{
    FILE* f = fopen("tic.in","r");
    FILE* fout = fopen("tic.out","w");
    int n,t;
    fscanf(f,"%d\n",&t);

    FOR(i,t)
    {
        char tabl[5][5];
        FOR(x,4)
            fscanf(f,"%s\n",tabl[x]);
        fscanf(f,"\n");
        bool done = false;

        fprintf(fout,"Case #%d: ",i+1);
        int nx = 0;
        int no = 0;
        int nt = 0;
        bool ep=false;


        FOR(x,4)
        {

        lx[x] = 0;
        lo[x] = 0;
        cx[x] = 0;
        co[x] = 0;

        }
        dpx=0;
        dpo=0;
        dsx=0;
        dso=0;

        FOR(x,4)
        FOR(y,4)
        {
            ep |= (tabl[x][y]=='.');
            if (x==y)
            {
                dpx+=(tabl[x][y] == 'X');
                dpo+=(tabl[x][y] == 'O');
                dpx+=(tabl[x][y] == 'T');
                dpo+=(tabl[x][y] == 'T');
            }
            if (x==3-y)
            {
                dsx+=(tabl[x][y] == 'X');
                dso+=(tabl[x][y] == 'O');
                dsx+=(tabl[x][y] == 'T');
                dso+=(tabl[x][y] == 'T');
            }

            lx[x]+=(tabl[x][y] == 'X');
            lo[x]+=(tabl[x][y] == 'O');
            lx[x]+=(tabl[x][y] == 'T');
            lo[x]+=(tabl[x][y] == 'T');

            cx[y]+=(tabl[x][y] == 'X');
            co[y]+=(tabl[x][y] == 'O');
            cx[y]+=(tabl[x][y] == 'T');
            co[y]+=(tabl[x][y] == 'T');
        }


        bool fnd = false;
        FOR(x,4)
        if (lo[x] == 4)
        {
            fprintf(fout,"O won\n");
            fnd = true;
            break;

        }
        else
        if (lx[x] == 4)
        {
            fprintf(fout,"X won\n");
            fnd = true;
            break;
        }
        else
        if (co[x] == 4)
        {
            fprintf(fout,"O won\n");
            fnd = true;
            break;
        }
        else
        if (cx[x] == 4)
        {
            fprintf(fout,"X won\n");
            fnd = true;
            break;
        }

        if (fnd)
            continue;

        if (dpx==4)
        {
            fprintf(fout,"X won\n");
            continue;
        }
        else
        if (dsx==4)
        {
            fprintf(fout,"X won\n");
            continue;
        }

        if (dpo==4)
        {
            fprintf(fout,"O won\n");
            continue;
        }
        else
        if (dso==4)
        {
            fprintf(fout,"O won\n");
            continue;
        }

        if (ep)
        {
            fprintf(fout,"Game has not completed\n");
            continue;
        }

        fprintf(fout,"Draw\n");
    }
    fclose(fout);
}
