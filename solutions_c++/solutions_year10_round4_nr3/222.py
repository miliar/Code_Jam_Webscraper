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

#define PROB "C"
//#define SIZE "test"
//#define SIZE "small"
#define SIZE "large"
#define ATT "1"

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
    SFOR(it,1,N+1)
    {   //read input
        int i,j,k,l,m,R,x1,x2,y1,y2;
        VI vx1,vy1,vx2,vy2;
        fscanf(in,"%d\n",&R);
        FOR(i,R)
        {   fscanf(in,"%d %d %d %d\n",&x1,&y1,&x2,&y2);
            vx1.PB(x1);
            vx2.PB(x2);
            vy1.PB(y1);
            vy2.PB(y2);
        }
        //process
        //find all intersecting pairs
        vector<vector<bool> > inter(R,vector<bool>(R,false));
        FOR(i,R)
        SFOR(j,i+1,R)
        {   if (vx2[i]<=vx1[j]-1 && vy2[i]<=vy1[j]-1) continue;
            if (vx2[j]<=vx1[i]-1 && vy2[j]<=vy1[i]-1) continue;
            if (vx2[i]<vx1[j]-1) continue;
            if (vx2[j]<vx1[i]-1) continue;
            if (vy2[i]<vy1[j]-1) continue;
            if (vy2[j]<vy1[i]-1) continue;
            inter[i][j]=true;
            inter[j][i]=true;
        }

        int ans=0;
        vector<bool> used(R,false);
        VI t;
        int xh,yh,xyl;
        FOR(i,R)
        if (!used[i])
        {   //get the params for this area of rectangles
            xh=vx2[i];
            yh=vy2[i];
            xyl=vx1[i]+vy1[i];
            //check whether there are any intersecting rects - bfs
            used[i]=true;
            t=VI(0);
            t.PB(i);
            j=0;
            while(j<SZ(t))
            {   //inter with t[j]
                FOR(k,R)
                    if (inter[t[j]][k] && !used[k])
                    {   used[k]=true;
                        t.PB(k);
                    }
                xh=max<int>(xh,vx2[t[j]]);
                yh=max<int>(yh,vy2[t[j]]);
                xyl=min<int>(xyl,vx1[t[j]]+vy1[t[j]]);
                j++;
            }
            ans=max<int>(ans,xh+yh-xyl+1);
        }
        //write output
        fprintf(out,"Case #%d: %d\n",it,ans);
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
