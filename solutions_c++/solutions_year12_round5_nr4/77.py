#include <iostream>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>
#include <sstream>
#include <cstring>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define mp make_pair
#define tr(i,v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)

vector<int> itit(char c)
{
    vector<int> ret;
    ret.pb(c-'a'+10);
    if(c=='o')
        ret.pb(0);
    if(c=='i')
        ret.pb(1);
    if(c=='e')
        ret.pb(3);
    if(c=='a')
        ret.pb(4);
    if(c=='s')
        ret.pb(5);
    if(c=='t')
        ret.pb(7);
    if(c=='b')
        ret.pb(8);
    if(c=='g')
        ret.pb(9);
    return ret;
}


int main()
{
    int t;
    cin >> t;
    for(int tc=1;tc<=t;tc++)
    {
        int two;
        cin >> two;
        string s;
        cin >> s;
        int n = s.size();
        bool M[50][50];
        bzero(M,sizeof(M));
        for(int i=0;i+1<n;i++)
        {
            int j = i+1;
            vector<int> i1 = itit(s[i]);
            vector<int> i2 = itit(s[j]);
            tr(it1,i1)
                tr(it2,i2)
                {
                    M[*it1][*it2] = true;
                }
        }
        int ans = 0;
        vector<int> indeg(50);
        vector<int> outdeg(50);
        for(int i=0;i<50;i++)
            for(int j=0;j<50;j++)
                if(M[i][j])
                {
                    indeg[i]++;
                    outdeg[j]++;
                    ans++;
                }
        int ans2 = 0;
        for(int i=0;i<50;i++)
            if(indeg[i]>outdeg[i])
                ans2 += indeg[i]-outdeg[i];

        cout << "Case #" << tc << ": " << ans + max(1,ans2) << endl;


    }
}
