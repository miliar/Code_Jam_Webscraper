#include <iostream>
//#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <numeric>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) (int)(v.size())


int main()
{
    char buf[1000];
    int runs, run, i, j, k;
    buf[0] = i = j = k = 0;
    scanf("%d\n", &runs);
    for (run = 1; run <= runs; run++)
    {
        scanf("%s",buf);
        vector<int> v;
        for(i=0;buf[i];i++)
            v.pb(buf[i]-'0');
        bool b=next_permutation(v.begin(),v.end());
        if(!b)
        {
            v.pb(0);
            sort(v.begin(),v.end());
            for(i=0;v[i]==0;i++);
            swap(v[0],v[i]);
        }
        printf("Case #%d: ",run);
        for(i=0;i<sz(v);i++)
            printf("%d",v[i]);
        printf("\n");            
    }
    return 0;
}
