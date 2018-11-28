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

int main()
{
    int T,tt,n,i,pos,curro=1, currb=1, timeo=0, timeb=0;
    char ch;
    cin>>T;
    for(tt=1;tt<=T;tt++)
    {
        cin>>n;
        curro=1, currb=1, timeo=0, timeb=0;
        for(i=0;i<n;i++)
        {
            cin>>ch;
            if(ch=='O')
            {
                cin>>pos;
                timeo+=abs(curro-pos);
                timeo+=1;
                curro=pos;
                if(timeo<=timeb)
                    timeo=(timeb+1);
            }
            else
            {
                cin>>pos;
                timeb+=abs(currb-pos);
                timeb+=1;
                currb=pos;
                if(timeb<=timeo)
                    timeb=(timeo+1);
            }
        }
        cout<<"Case #"<<tt<<": "<<max(timeo,timeb)<<endl;
    }
}
