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
template<class T> bool get_max(T&a,T&b) {
    return b>a?a=b,1:0;
}
template<class T> bool get_min(T&a,T&b) {
    return b<a?a=b,1:0;
}

int N;
int arr[1005];

int main() {
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;
    cin>>T;
    int tt=1;
    while (T--) {
        cin>>N;
        rep(i,N) cin>>arr[i];
        int ans=0;
        int sum=0;
        sort(arr,arr+N);
        rep(i,N){
            ans^=arr[i];
            sum+=arr[i];
        }
        printf("Case #%d: ",tt++);
        if(ans!=0) printf("NO\n");
        else printf("%d\n",sum-arr[0]);
    }
    return 0;
}

