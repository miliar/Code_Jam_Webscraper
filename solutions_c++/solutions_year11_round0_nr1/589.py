#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#include <string>
#define rep(i,n) for(int i=0;i<n;i++)
#define For(i,a,b) for(int i=a;i<=b;i++)
#define tr(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define all(x) x.begin(),x.end()
#define pb push_back
using namespace std;
const int inf=~0U>>1;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef long long LL;
template<class T> bool get_max(T&a,T&b){return b>a?a=b,1:0;}
template<class T> bool get_min(T&a,T&b){return b<a?a=b,1:0;}

char ch[105];
int num[105];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin>>T;
    int t=1;
    while(T--){
        int n,k;
        cin>>n;
        int re1=0,re2=0;
        int prev1=1,prev2=1;
        int re=0;
        for(int i=0;i<n;i++){
            cin>>ch[i]>>num[i];
        }
        for(int i=0;i<n;i++){
            if(ch[i]=='O'){
                int t=abs(num[i]-prev1)+1;
                if(re1+t>re) re=t+re1;
                else re++;
                re1=re;
                prev1=num[i];
            }else{
                int t=abs(num[i]-prev2)+1;
                if(re2+t>re) re=t+re2;
                else re++;
                re2=re;
                prev2=num[i];
            }
        }
        printf("Case #%d: %d\n",t++,re);
    }
    return 0;
}
