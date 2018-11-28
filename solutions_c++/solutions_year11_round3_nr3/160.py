#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#define REP(i,n) for(int i=0;i<n;i++)
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

int a[105];
int n;

bool check(int num){
    bool flag=true;
    for(int i=0;i<n;i++){
        if(a[i]!=0&&num%a[i]==0) continue;
        if(a[i]%num==0) continue;
        flag=false;
        break;
    }
    if(flag) return true;
    else return false;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T;
    cin>>T;
    int tt=1;
    int l,h;
    while(T--){
        cin>>n>>l>>h;
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        int i;
        for(i=l;i<=h;i++){
            if(check(i)){
                break;
            }
        }
        printf("Case #%d: ",tt++);
        if(i==h+1){
            puts("NO\n");
        }else{
            printf("%d\n",i);
        }
    }
    return 0;
}
