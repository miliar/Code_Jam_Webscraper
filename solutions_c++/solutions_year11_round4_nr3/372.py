#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <utility>
#include <functional>
#include <sstream>
#include <climits>
#include <cfloat>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstring>
#include <cstdio>
using namespace std;

const long long M=1000000000000;
const int N=1000000;

bool a[N+1];
vector< vector<long long> > v;

int main()
{
    for(int i=2;i<=N;i++)
        if(!a[i])
        {
            long long t=(long long)i*i;
            long long d=t;
            while(d<=N)
            {
                a[d]=true;
                d+=i;
            }
            v.push_back(vector<long long>());
            while(t<=M)
            {
                v[v.size()-1].push_back(t);
                t*=i;
            }
        }
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int Tests;
    scanf("%d",&Tests);
    for(int Test=1;Test<=Tests;Test++)
    {
        printf("Case #%d: ", Test);
        //
        long long a;
        scanf("%lld",&a);
        if(a==1)
        {
            printf("0\n");
            continue;
        }
        long long res=0;
        //
        for(int i=0;i<v.size();i++)
            res+=upper_bound(v[i].begin(),v[i].end(),a)-v[i].begin();
        //
        printf("%lld\n",res+1);
    }
    return 0;
}
