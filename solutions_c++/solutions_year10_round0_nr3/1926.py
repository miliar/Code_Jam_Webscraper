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
#include <cstring>
#include <complex>
#include <queue>
#include <ctime>
/*
#include <ext/numeric>
#include <ext/hash_map>
#include <ext/hash_set>
*/
using namespace std;
//using namespace __gnu_cxx;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)

int v[1005];
int r,k,n;

long long getpre(int prelen)
{
    int stp = 0;
    int stepcnt =0;
    long long res=0;
    while(stepcnt<prelen){
        long long cc=0,cnt=0;
		while(1){
			if(cc+v[stp]>k||cnt>=n)
				break;
            cc+=v[stp],stp++,stp%=n,cnt++;
		}
        res+=cc;
		stepcnt++;
    }
    return res;
}

long long getpost(int stp,int rem){
    long long res=0;
    while(rem){
        long long cc=0,cnt=0;
		while(1){
			if(cc+v[stp]>k||cnt>=n)
					break;
            cc+=v[stp],stp++,stp%=n,cnt++;
		}
        res+=cc;
        rem--;
    }
    return res;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.in","rt",stdin);
    freopen("out.out","wt",stdout);
#endif
    int t;
    scanf("%d",&t);
    rep(tt,0,t){
        scanf("%d %d %d",&r,&k,&n);
        rep(i,0,n)
            scanf("%d",&v[i]);
        vector<long long> vis(n,-1);
        vector<long long>score;
        long long stp = 0;
        long long stepcnt=0;
        while(stepcnt<r){
            if(vis[stp]!=-1)
                break;
            vis[stp]=stepcnt++;
            long long cc= 0,cnt=0;
			while(1){
				if(cc+v[stp]>k||cnt>=n)
					break;
                cc+=v[stp],stp++,stp%=n,cnt++;
			}
            score.PB(cc);
        }
        if(stepcnt == r){
            long long res=0;
            rep(i,0,score.size())
                res+=score[i];
            cout<<"Case #"<<tt+1<<": "<<res<<endl;
            continue;
        }
        long long prelen = vis[stp];
        long long cyclelen = stepcnt-vis[stp];
        long long res = getpre(prelen);
        long long sccycle = 0;
        rep(i,vis[stp],stepcnt)
            sccycle+=score[i];
        r-=prelen;
        int x = r/cyclelen;
        res+=sccycle*x;
        res+=getpost(stp,r%cyclelen);
        cout<<"Case #"<<tt+1<<": "<<res<<endl;
    }
    
    return 0;
}
