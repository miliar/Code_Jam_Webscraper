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

void tst()
{
    int n;
    cin >> n;
    if(n==0)
    {
        cout << '0' << endl;
        return;
    }
    vector<int> ile(10001);
    for(int i=0;i<n;i++)
    {
        int a;
        cin >> a;
        ile[a]++;
    }
    int alive = 0;
    vector<int> q;

    for(int i=0;i<ile.size();i++)
    {
        int f = ile[i];
        while(alive<f)
        {
            q.pb(0);
            alive++;
        }
        alive = f;
        for(int j=0;j<f;j++)
            q[q.size()-1-j]++;
    }
    int mm = q[0];
    for(int i=0;i<q.size();i++)
        mm = min(mm,q[i]);
    cout << mm << endl;


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
