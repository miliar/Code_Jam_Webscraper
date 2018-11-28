#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;
#define forn(i,n) for(i=0;i<(n);i++)

int conv(string st)
{
    return 600 * (st[0] - '0') + 60 * (st[1] - '0') + 10 * (st[3] - '0') + (st[4] - '0');
}

int main()
{
    int n;
    int na, nb, ta, tb, i, r;
    int t;
    string inp;
    vector<int> sa, sb, la, lb, resa, resb, times;
    ifstream text("B-large.in");
    ofstream res("B-large.out");
    text >> inp;
    n = atoi(inp.c_str());
    while(n > 0)
    {
        text >> inp;
        t = atoi(inp.c_str());
        getline(text,inp,' ');
        na = atoi(inp.c_str());
        getline(text,inp);
        nb = atoi(inp.c_str());
        sa.resize(0);
        la.resize(0);
        sb.resize(0);
        lb.resize(0);
        while(na > 0)
        {
            getline(text,inp,' ');
            sa.push_back(conv(inp));
            getline(text,inp);
            la.push_back(conv(inp) + t);
            na--;
        }
        while(nb > 0)
        {
            getline(text,inp,' ');
            sb.push_back(conv(inp));
            getline(text,inp);
            lb.push_back(conv(inp) + t);
            nb--;
        }
        ta = 0;
        tb = 0;
 /*       forn(i,sa.size())
        {
            times.push_back(sa[i]);
            times.push_back(la[i]);
        }
        forn(i,sb.size())
        {
            times.push_back(sb[i]);
            times.push_back(lb[i]);
        }
        sort(times.begin(),times.end());
        unique(times.begin(),times.end());*/
        r = 0;
        forn(i,3600/*times.size()*/)
        {
            ta = ta + count(sa.begin(), sa.end(), i) - count(lb.begin(), lb.end(), i);
            if(ta > 0)
            {
                r += ta;
                ta = 0;
            }
        }
        resa.push_back(r);
        r = 0;
        forn(i,3600)
        {
            tb = tb + count(sb.begin(), sb.end(), i) - count(la.begin(), la.end(), i);
            if(tb > 0)
            {
                r += tb;
                tb = 0;
            }
        }
        resb.push_back(r);
        n--;
    }
    forn(i,resa.size())
    {
        res << "Case #" << i+1 << ": " << resa[i] << ' ' << resb[i] << '\n';
    }
    res.close();
}
