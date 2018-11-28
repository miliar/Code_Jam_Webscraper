

#include<iostream>
#include<vector>
#include<cmath>
#include<time.h>
#include<fstream>
#include<queue>
#include<stack>
#include<utility>
#include<stdlib.h>
#include<string.h>
#include<set>
#include<list>
#include<map>
#include<algorithm>
#include <sstream>
#include <unistd.h>

#define GI ({int t;scanf("%d",&t);t;})
#define forn(i,n) for(int i=0;i<n;i++)
#define forab(i,a,b) for(int i=a;i<b;i++)
#define pb(t) push_back(t)
#define pq priority_queue
#define mp(t1,t2) make_pair(t1,t2)
#define vi vector<int>
#define pii pair<int,int>
#define vpii vector<pair<int,int> >

#define INF INT_MAX
#define ep 0.00000001

#define dbg(x) cout << #x << " -> " << (x) << "\t";
#define dbge(x) cout << #x << " -> " << (x) << "\n";

using namespace std;

int main()
{
    int t;
    cin>>t;
    int T = t;
    while(t--){
    int n;
    cin>>n;
    int sum = 0, min = 10000000, xo = 0;
    for(int i=0;i<n;i++)
    {
        int a;
        cin>>a;
        xo = xo ^ a;
//        cout<<xo<<' ';
        if(a < min)
            min = a;
        sum += a;
    }
    if(xo == 0)
    cout<<"Case #"<<T-t<<": "<<sum - min<<endl;
    else 
            cout<<"Case #"<<T-t<<": NO"<<endl;
    }
    //system("pause");
    return 0;
}
