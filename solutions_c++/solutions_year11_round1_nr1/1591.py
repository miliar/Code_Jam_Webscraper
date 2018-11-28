#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>

using namespace std;

//BEGINTEMPLATE_BY_SCORPIOLIU


#define REP(i,a) for(int i=0;i<int(a);++i)


#define SMALL
//#define LARGE

int main()
{
#ifdef SMALL
    //ifstream fin("A-small-practice.in");ofstream fout("A-small-practice.out");
    //ifstream fin("A-small-attempt0.in");ofstream fout("A-small-attempt0.out");
    freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
#endif
#ifdef LARGE
    //ifstream fin("A-large-practice.in");ofstream fout("A-large-practice.out");
    //ifstream fin("A-large.in");ofstream fout("A-large.out");
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
#endif
    int T;
    cin>>T;
    int n = 1;
    REP(z,T)
    {

        cout<<"Case #"<<z+1<<": ";
        //////////////////////////////////////
        int N, PD, PG;
        cin>>N>>PD>>PG;
        int B, C;
        bool flag = true;

        {
            for (int i = 1; i <= N; i++)
            {
                if ((i*PD)%100 != 0)
                    continue;
                for (int j = 0; j<100000; j++)
                {
                    B = (PG-PD)*i + PG*j;
                    if (B%100 == 0 && B/100 <= j && B >= 0)
                    {
                        cout<<"Possible";
                        flag = false;
                        goto hi;
                    }
                }
            }
            hi:     if (flag) cout<<"Broken";
        }


        //////////////////////////////////////
        cout<<endl;
    }


    return 0;
}
