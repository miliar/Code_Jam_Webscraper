// Template By Fendy Kosnatha (Seraph)
#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstring>
#include <string.h>

#define fs first
#define sc second
#define mp make_pair
#define pii pair<int, int>

using namespace std;
int pernah[2000001];
vector< vector< vector<int> > > vvi(8);
vector<vector<int> > vv(2000001);
void generate()
{
    for (int i=2;i<=7;i++)
    {
        vector<int> v;
        for (int j=1;j<=i;j++)
            v.push_back(j);
        while (next_permutation(v.begin(), v.end()))
        {
            int naik=0;
            int turun=0;
            for (int j=1;j<v.size();j++)
            {
                if (v[j]-v[j-1]>=2) naik++;
                if (v[j]-v[j-1]<0) turun++;
            }
            //if (naik==1 && turun==1) vvi[i].push_back(v);
            if (naik==0 && turun==1) vvi[i].push_back(v);
        }
    }
}
void recycle(int n, int b)
{
    pernah[n]=1;
    int _n = n;
    vector<int> v;
    while (_n>0)
    {
        v.push_back(_n%10);
        _n/=10;
    }
    reverse(v.begin(), v.end());
    vector<int> vans;
    for (int i=0;i<vvi[v.size()].size();i++)
    {
        int temp=0;
        for (int j=0;j<vvi[v.size()][i].size();j++)
            temp = temp*10 + v[vvi[v.size()][i][j]-1];
        if (temp>n && temp<=b)
        {
            if (pernah[temp]!=n)
            vans.push_back(temp);
            pernah[temp]=n;
        }
    }
    int tot = vans.size();
    vv[n] = vans;
    return;
}
int main()
{
    generate();
    memset(pernah,0,sizeof(pernah));
    for (int i=1;i<=2000000;i++)
        recycle(i,2000000);
    int tc;
    cin>>tc;
    int count=1;
    while (tc--)
    {
        int ans=0;
        //memset(pernah,0,sizeof(pernah));
        int a,b;
        cin>>a>>b;
        for (int i=a;i<=b;i++)
        {
            for (int j=0;j<vv[i].size();j++)
            {
                if (vv[i][j]<=b) ans++;
            }
        }
        cout<<"Case #"<<count++<<": "<<ans<<endl;
    }
    return 0;
}
