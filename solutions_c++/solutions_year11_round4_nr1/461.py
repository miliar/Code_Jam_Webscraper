#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

#define LOOP(i,a,b) for((i)=(a);(i)<(b);++(i))
#define FOR(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define SZ(v) ((int)((v).size()))
#define PB push_back
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;

struct WW
{
    int b,e,s;
    WW() { b = e = s = 0; }
    WW(int _b, int _e, int _s) : b(_b), e(_e), s(_s) {}
};

bool WWcomp(WW a, WW b)
{
    return(a.s < b.s);
}

int main() {
    ios_base::sync_with_stdio(false);
    ofstream fout("a2.out");
    ifstream fin("a2.in");

    int t;
    fin >> t;
    FOR(tt,t)
    {
        int x,speed,runspeed,runtime,n;
        fin >> x >> speed >> runspeed >> runtime >> n;
        vector<WW> wws(n);
        FOR(i,n)
        {
            fin >> wws[i].b >> wws[i].e >> wws[i].s;
        }

        FOR(i,n) if(i) { if(wws[i-1].e < wws[i].b) wws.PB(WW(wws[i-1].e,wws[i].b,0)); }
        if(wws[0].b>0) wws.PB(WW(0,wws[0].b,0));
        if(wws[n-1].e<x) wws.PB(WW(wws[n-1].e,x,0));

        sort(wws.begin(),wws.end(),WWcomp);
        n = SZ(wws);
        double res = 0.0;
        double timeleft = (double)runtime;
        FOR(i,n)
        {
            if(timeleft <= 0.0)
            {
                res += ((double)(wws[i].e - wws[i].b)) / ((double)(wws[i].s+speed));
            }
            else
            {
                double tmptime = ((double)(wws[i].e - wws[i].b)) / ((double)(wws[i].s+runspeed));
                if(tmptime <= timeleft)
                {
                    res += tmptime;
                    timeleft -= tmptime;
                }
                else
                {
                    res += timeleft;
                    double distleft = ((double)(wws[i].e - wws[i].b)) - ((timeleft)*((double)(wws[i].s+runspeed)));
                    timeleft = -1.0;
                    res += (distleft) / ((double)(wws[i].s+speed));
                }
            }
        }

        fout.precision(12);
        fout << "Case #" << tt+1 << ": " << res << '\n';
    }

    fout.close();
    fin.close();
    return 0;
}
