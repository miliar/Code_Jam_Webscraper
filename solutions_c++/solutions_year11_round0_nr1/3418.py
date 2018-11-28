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
#include <cstring>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define FOR( i,a,b ) for(int i=a;i<b;i++)
#define NS string::npos
#define VI vector <int>
#define sz size
#define PI <int ,int >
#define CLEAR(cab) memset(cab,0,sizeof cab)
using namespace std;
int main()
{
    freopen("input_large_bot.txt","r",stdin);
    freopen("output_bot_large.txt","w",stdout);
   vector < int > vi;
   vector < char > vc;
    int n,i,test;
    vi.resize(200);
    vc.resize(200);
    scanf("%d",&test);
    int cs=0;
    int opos_pre=1,bpos_pre=1,opos_new=1,bpos_new=1,time_tot=0,timeo=0,timeb=0;
    while(test--)
    {
        cs++;

    scanf("%d",&n);
    opos_pre=1;
    bpos_pre=1;
    opos_new=1;
    bpos_new=1;
    time_tot=0;
    timeo=0;
    timeb=0;
     for(i=0;i<n;i++)
    {
        //scanf("%c%d",&vc[i],&vi[i]);
        cin>>vc[i]>>vi[i];
     //   cout<<vi[i]<<" "<<vc[i]<<endl;
    }

    for(i=0;i<n;i++)
    {

        if(vc[i]=='O')
        {
            opos_new=vi[i];
            timeo+=abs(opos_new-opos_pre)+1;
            timeo=max(timeo,time_tot+1);
            time_tot=timeo;
            opos_pre=opos_new;

        }

        if(vc[i]=='B')
        {
            bpos_new=vi[i];
            timeb+=abs(bpos_new-bpos_pre)+1;
        //    cout<<bpos_new<<"*"<<bpos_pre<<"*"<<timeb<<endl;
            timeb=max(timeb,time_tot+1);
            time_tot=timeb;
            bpos_pre=bpos_new;
        }
     //   cout<<timeb<<" "<<timeo<<" "<<time_tot<<endl;
    }
    printf("Case #%d: %d\n",cs,time_tot);
    //cout<<endl;
    }

return 0;
}

