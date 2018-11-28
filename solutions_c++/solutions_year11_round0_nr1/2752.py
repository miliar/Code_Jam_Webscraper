#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;
#define forn(i,n) for(int i = 0 ; i < n ; i ++)
#define pb push_back
main()
{
    #ifdef ACMTUYO
        freopen("a.in","r",stdin);
    #endif
    int cc;
    cin >>cc;
    forn(kk,cc)
    {
        int n;
        cin>>n;
        vector<int> bot;
        vector<int> rob;
        forn(i,n)
        {
            char a;
            int b;
            cin >>a >>b;
            bot.pb(b);
            if (a == 'O')
                rob.pb(0);
            else rob.pb(1);
        }
        int pos[] = {1,1};
        int tim[] = {0,0};
        int res = 1;
        forn(i,n)
        {
            int x = rob[i];
            tim[x] += abs(pos[x] - bot[i])+1;
            tim[x] = max(tim[x], tim[(x+1 )%2]+1);
            pos[x] = bot[i];
            res = max(tim[0],tim[1]);

        }
        cout<<"Case #"<<kk+1<<": "<<res<<endl;


    }

}
