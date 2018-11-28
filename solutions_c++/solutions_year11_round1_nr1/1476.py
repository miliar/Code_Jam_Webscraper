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
#include <cstdlib>
#include <ctime>

using namespace std;


int gcd(int a, int b)
{
    int t;
    while(b!=0)
    {
        t=b;
        b = a%b;
        a = t;
    }
    return a;
}
int main()
{

    int T, N, PD, PG;
    cin>>T;
    for(int t=0;t<T;t++)
    {
        cout<<"Case #"<<t+1<<": ";
        cin>>N>>PD>>PG;
        if(PG==0 && PD!=0)
            cout<<"Broken";
        else if(PG==100 && PD!=100)
            cout<<"Broken";
        else
        {
            int dgcd = gcd(PD, 100);
            int ggcd = gcd(PG, 100);

            if(100/dgcd>N)
                cout<<"Broken";
            else
            {
                cout<<"Possible";
            
            }
        }
        cout<<endl;
            
    }

    return 0;
}
