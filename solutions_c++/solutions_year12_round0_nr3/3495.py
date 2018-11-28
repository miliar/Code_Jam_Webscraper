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

bool isRotation(int i, int j)
{
    stringstream ss1, ss2;
    string s1, s2;
    ss1<<i;
    ss2<<j;
    s1 = ss1.str();
    s2 = ss2.str();

    s1 += s1;

    if(s1.find(s2)==string::npos)
        return false;

    return true;
}
int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        set<pair<int, int> >s;
        int a, b;
        cin>>a>>b;
        for(int i=a;i<=b;i++)
        {
           for(int j=i+1;j<=b;j++)
           {
               if(isRotation(i, j))
                   s.insert(make_pair(i, j));
           }
        }
        cout<<"Case #"<<t<<": "<<s.size()<<endl;
    }

    return 0;
}
