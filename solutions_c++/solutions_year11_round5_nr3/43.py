#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
using namespace std;
#define pb push_back
#define mp make_pair
#define tr(i,v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)
#define all(x) x.begin(),x.end()

int dx[] = {1,0,1,1};
int dy[] = {0,1,1,-1};

int type(char c)
{
    if(c == '-')
        return 0;
    if(c=='|')
        return 1;
    if(c=='\\')
        return 2;
    return 3;
}

void tst()
{
    int r,c;
    cin >> r >> c;

    vector<string> in(r);

    for(int i=0;i<r;i++)
        cin >> in[i];

    vector<vector<int> > tt(r,vector<int>(c));
    for(int i=0;i<r;i++)
        for(int j=0;j<c;j++)
            tt[i][j] = type(in[i][j]);

    vector<int> p1(r*c);
    vector<int> p2(r*c);

    vector<vector<int> > att(r*c);

    for(int y=0;y<r;y++)
        for(int x=0;x<c;x++)
        {
            int l = y*c+x;
            int x1 = (x + dx[tt[y][x]]+c)%c;
            int y1 = (y + dy[tt[y][x]]+r)%r;
            int l1 = y1*c+x1;
            int x2 = (x - dx[tt[y][x]]+c)%c;
            int y2 = (y - dy[tt[y][x]]+r)%r;
            int l2 = y2*c+x2;
            p1[l] = l1;
            p2[l] = l2;
            att[l1].pb(l);
            att[l2].pb(-l-1);
        }

    vector<int> dec(r*c);

    int n = r*c;
    for(int v=0;v<n;v++)
    {
        if(dec[v])
            continue;

        vector<int> toclear;
        queue<int> q;
        q.push(v);
        dec[v] = 1;
//        cout << "trying " << v << " to be " << 1 << endl;
        toclear.pb(v);
        bool ok=true;
        while(!q.empty())
        {
            int u = q.front();
            q.pop();
            int targ;
            if(dec[u]==1)
                targ = p1[u];
            else
                targ = p2[u];
//            cout << u << " is: " << dec[u] << " so:\n";
            tr(j,att[targ])
            {
                if(*j == u || *j == -u-1)
                    continue;
                int targ2;
                int forc;
                if(*j >= 0)
                {
                    targ2 = *j;
                    forc = 2;
                }
                else
                {
                    targ2 = - *j - 1;
                    forc = 1;
                }
//                cout <<  targ2 << " is: " << forc << endl;
                if(dec[targ2]==0)
                {
                    dec[targ2] = forc;
                    q.push(targ2);
                    toclear.pb(targ2);
                    continue;
                }
                if(dec[targ2]!=forc)
                {
//                    cout << "fail" << endl;
                    ok = false;
                    while(!q.empty())
                        q.pop();
                    break;
                }
            }
        }
        if(ok)
            continue;
        tr(j,toclear)
            dec[*j] = 0;
        toclear.clear();

        q.push(v);
        dec[v] = 2;
//        cout << "trying " << v << " to be " << 2 << endl;
        toclear.pb(v);
        ok = true;
        while(!q.empty())
        {
            int u = q.front();
            q.pop();
            int targ;
            if(dec[u]==1)
                targ = p1[u];
            else
                targ = p2[u];
//            cout << u << " is: " << dec[u] << " so:\n";
            tr(j,att[targ])
            {
                if(*j == u || *j == -u-1)
                    continue;
                int targ2;
                int forc;
                if(*j >= 0)
                {
                    targ2 = *j;
                    forc = 2;
                }
                else
                {
                    targ2 = - *j - 1;
                    forc = 1;
                }
//                cout <<  targ2 << " is: " << forc << endl;
                if(dec[targ2]==0)
                {
                    dec[targ2] = forc;
                    q.push(targ2);
                    toclear.pb(targ2);
                    continue;
                }
                if(dec[targ2]!=forc)
                {
//                    cout << "fail" << endl;
                    ok = false;
                    while(!q.empty())
                        q.pop();
                    break;
                }
            }
        }
        if(!ok)
        {
            cout << "0\n";
            return;
        }
    }
//    tr(j,dec)
//        cout << *j << ' ';
    
    vector<int> who(n);
    for(int i=0;i<n;i++)
        if(dec[i]==1)
            who[p1[i]] = i;
        else
            who[p2[i]] = i;

    vector<int> vis(n);
    int col = 1;
    int ans = 1;
    for(int i=0;i<n;i++)
    {
        if(vis[i])
            continue;
        vis[i] = col;
        int u,v;
        u  = i;
        
        if(dec[i]==1)
            v = who[p2[i]];
        else
            v = who[p1[i]];

        while(!vis[v])
        {
            vis[v] = col;
            u = v;
            if(dec[u]==1)
                v = who[p2[u]];
            else
                v = who[p1[u]];
        }
        if(vis[v]==col)
            ans = (2*ans)%1000003;
        col++;
    }

    cout << ans;
    
    
    cout << endl;



}

int main()
{
    int t;
    cin >> t;
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);
        tst();
    }
}
