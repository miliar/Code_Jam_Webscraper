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
#include <string>
#include <string.h>
using namespace std;
set< pair<int,int> >s;
set< pair<int,int> > :: iterator it;
void init()
{
    for(int i=1;i<=2000000;i++)
    {
        stringstream ss;
        ss<<i;
        string test;ss>>test;
        for(int j=test.length()-1;j>=1;j--)
        {
                string te1 = test.substr(j);
                string te2 = test.substr(0,j);
                string n = te1+te2;
                stringstream ss1(n);
                int check;ss1>>check;
                if(check>i)
                {
                    s.insert(make_pair(i,check));
                }
        }    
    }
}
int main()
{
    init();
    freopen("C-large.in","r",stdin);
    freopen("outCN.txt","w",stdout);
    int t;cin>>t;
    for(int ca=1;ca<=t;ca++)
    {
        int A,B;
        cin>>A>>B;
        int ret = 0;
        for(it=s.begin();it!=s.end();it++)
        {
            pair<int,int> tem = (*it);;
            if(tem.first < tem.second && tem.first >=A && tem.second <=B)
                ret++;
        }
        cout<<"Case #"<<ca<<": "<<ret<<endl;
    }
}
