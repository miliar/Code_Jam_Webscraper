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
#include <string>
#include <cstring>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
using namespace std;

#define REP(i,a,b) for(int i=a; i < b; i++)
#define REPE(i, a, b) for(int i=a; i <=b; i++)

typedef long long ll;
const int maxN = 10000;

ll dist[maxN];
ll len[maxN];
ll avail[maxN];

int main()
{
    ios_base::sync_with_stdio(false);

    /*
     We need to keep track of 
     1) The current available vine length
     */
    int T;
    cin>>T;
    for(int idx=1; idx <= T; idx++)
    {
        int N,D;
        cin>>N;
        for(int i=0; i < N; i++)
        {
            cin>>dist[i]>>len[i];
            avail[i] = -1ll;
        }
        cin>>D;
        avail[0] = dist[0];
        bool isValid = false;
        for(int i=0; i < N && avail[i] != -1ll; i++)
        {
            int range = dist[i] + avail[i];
            if(range >= D)
            {
                isValid = true;
                break;
            }
            for(int j=i+1; j < N && dist[j] <= range; j++)
            {
                avail[j] = max(avail[j], min(dist[j] - dist[i], len[j]));
            }
        }
        
        cout<<"Case #"<<idx<<": ";
        if(isValid) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }

    return 0;
}