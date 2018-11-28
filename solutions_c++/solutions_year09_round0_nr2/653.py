//---------------------------------------------------------------------------

#include <clx.h>
#pragma hdrstop

#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <stdio.h>
#include <stdarg.h>
#include <stddef.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

#define VS vector<string>
#define VI vector<int>
#define SS stringstream
#define PB push_back
#define SZ(a) (int)a.size()
#define FOR(i,m) for(i=0;i<m;++i)
#define SFOR(i,s,m) for(i=s;i<m;++i)
#define DEB(x) cout<<#x<<" = "<<(x)<<endl;

#define PROB "B"
//#define SIZE "test"
//#define SIZE "small"
#define SIZE "large"
#define ATT "0"

//---------------------------------------------------------------------------

#pragma argsused
int main(int argc, char* argv[])
{
    FILE *in, *out;
    int N,it;
    string name=PROB+string("-")+SIZE;
    if (string(SIZE)==string("small"))
        name+=string("-attempt")+ATT;
    in = fopen((name+".in").c_str(),"rt");
    out = fopen((name+".out").c_str(),"wt");
    fscanf(in,"%d\n",&N);
    int dr[] = {-1, 0, 0, 1};
    int dc[] = { 0,-1, 1, 0};
    int i,j,k,l,W,H,r,c,mina,dir;
    SFOR(it,1,N+1)
    {   //read input
        fscanf(in,"%d %d",&H,&W);
        vector<VI > map = vector<VI >(H, VI(W));
        FOR(i,H)
        FOR(j,W)
            fscanf(in,"%d",&(map[i][j]));
        //process
        VS basin = VS(H, string(W,'?'));
        char next='a';
        FOR(i,H)
        FOR(j,W)
        if (basin[i][j]=='?')
        {   //move from this cell to sink, marking with '*'
            r=i;
            c=j;
            basin[i][j]='*';
            while (true)
            {   mina=map[r][c];
                dir=-1;
                FOR(k,4)
                    if (r+dr[k]>=0 && r+dr[k]<H && c+dc[k]>=0 && c+dc[k]<W && map[r+dr[k]][c+dc[k]]<mina)
                    {   mina=map[r+dr[k]][c+dc[k]];
                        dir=k;
                    }
                if (dir==-1)    //sink
                    break;
                //flow
                r+=dr[dir];
                c+=dc[dir];
                if (basin[r][c]=='?')
                    basin[r][c]='*';
                else
                {   //relabel all '*' with this char
                    FOR(k,H)
                    FOR(l,W)
                        if (basin[k][l]=='*')
                            basin[k][l]=basin[r][c];
                    //and break
                    break;
                }
            }
            if (basin[r][c]=='*')
            {   //relabel all '*' with next
                FOR(k,H)
                FOR(l,W)
                    if (basin[k][l]=='*')
                        basin[k][l]=next;
                next++;
            }
        }

        //write output
        fprintf(out,"Case #%d:\n",it);
        FOR(i,H)
        {   FOR(j,W)
                fprintf(out,"%c ",basin[i][j]);
            fprintf(out,"\n");
        }
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
