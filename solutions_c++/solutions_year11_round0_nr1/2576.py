#include <iostream>
#include <math.h>
#include <list>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <memory.h>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <stdio.h>
#include <assert.h>

using namespace std;
#define SET(a,n) memset(a,n,sizeof(a));
#define FOR(a,b,c) for(int a=b;a<c;++a)
#define GN(a) scanf("%d",&a)

typedef long long int LL;
typedef vector<int> VI;

using namespace std;

int n;
vector<char> player;
vector<int> pos;

int adjust(int from,int to,int time_allowed)
{
    int time_needed = abs(from-to);
    if(from<=to)from+=min(time_needed,time_allowed);
    else from-=min(time_needed,time_allowed);

    return from;
}

int getb_next(int from)
{
    FOR(i,from+1,n)if(player[i]=='B')return pos[i];
    return (1<<28);
}

int geto_next(int from)
{
    FOR(i,from+1,n)if(player[i]=='O')return pos[i];
    return (1<<28);
}

int main()
{
    freopen("i.txt","r",stdin);
    freopen("A-large.out","w",stdout);

    int t;
    cin>>t;
    FOR(test,1,t+1)
    {
        cin>>n;
        player.clear();
        pos.clear();
        int o_pos = 1, b_pos = 1,temp;
        char c;
        int total=0;
        FOR(i,0,n)
        {
            cin>>c>>temp;
            player.push_back(c);
            pos.push_back(temp);
        }
        FOR(i,0,n)
        {
            c = player[i];
            temp = pos[i];
            if(c == 'O')
            {
                int bnext_pos = getb_next(i);
                int time_taken = abs(temp-o_pos)+1;
                b_pos = adjust(b_pos,bnext_pos,time_taken);
                total+=time_taken;
                o_pos = temp;
            }
            else
            {
                int onext_pos = geto_next(i);
                int time_taken = abs(temp-b_pos)+1;
                o_pos = adjust(o_pos,onext_pos,time_taken);
                total+=time_taken;
                b_pos = temp;
            }
        }
        cout<<"Case #"<<test<<": "<<total<<endl;
    }

    return 0;
}

