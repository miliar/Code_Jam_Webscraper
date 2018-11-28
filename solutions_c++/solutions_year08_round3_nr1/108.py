#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
using namespace std;
int main()
{
    freopen("a.txt","rt",stdin);
    freopen("b.txt","wt",stdout);
    int N;
    cin>>N;
    int P,K,L;
    vector<long long> v;
    int temp;
    for(int nn=0;nn<N;nn++)
    {
        cin>>P>>K>>L;
        if(P*K<L)
        {
            cout<<"Case #"<<nn+1<<": Impossible"<<endl;
            continue;
        }
        v.clear();
        for(int i=0;i<L;i++)
        {
            cin>>temp;
            v.push_back(temp);
        }
        sort(v.rbegin(),v.rend());
        long long res=0;
        int cur=0;
        for(long long i=1;i<=P && cur<L;i++)
            for(int j=0;j<K && cur<L;j++,cur++)
                res+=i*v[cur];
        cout<<"Case #"<<nn+1<<": "<<res<<endl;
    }
    return 0;
}
