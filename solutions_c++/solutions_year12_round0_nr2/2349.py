/*	SURENDRA KUMAR MEENA	*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long int LL;
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define R(i,n,k) for(int i=n;i>=k;i--)
#define CLR(s,v) memset(s,v,sizeof(s))

int main(){
    int t;
    cin>>t;
    FF(kase,1,t+1){
        cout<<"Case #"<<kase<<": ";
        int n,s,p;
        cin>>n>>s>>p;
        int ans=0;
        F(i,n){
            int k;
            cin>>k;
            if(p<=k){
                if(k-p>=2*p-2)
                    ans++;
                else if(s>0 && k-p>=2*p-4){
                    s--;
                    ans++;
                }
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}
