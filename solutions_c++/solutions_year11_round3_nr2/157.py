/*
 * Author: OldY
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
const int maxint = -1u>>1;
const double pi = acos(-1.0);


int Cas;
long long a[1010];
long long dis[1001000];
long long t;
int n,c,l;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin >> Cas;
    for(int cas = 1 ; cas <= Cas ; cas++){
        cin >> l >> t >> n >> c;
        //cout << l << " " << t << " " << n << " " << c << endl;
        long long ta_dis = 0;
        memset(dis , 0 , sizeof(dis));
        for(int i = 0 ; i < c ; i++) cin >> a[i];
        for(int i = 0 ; i < n ; i++){
            dis[i] = a[i%c];
            ta_dis += dis[i];
        }
        //for(int i = 0 ; i < n ; i++) cout << dis[i] << " ";
        //cout << endl;
        if(ta_dis*2LL <= t){
            cout << "Case #" << cas << ": ";
            cout << ta_dis*2LL << endl;
        }else{
            long long tmp = t/2LL;
            long long ans = t;
            long long cnt = 0;
            int st = 0;
            for(int i = 0 ; i < n ; i++){
                if(tmp < cnt+dis[i]){
                    st = i;
                    break;
                }
                cnt += dis[i];
            }
            //for(int i = 0 ; i < n ; i++) cout << dis[i] << " ";cout << endl;
            //cout << tmp << endl;
            //cout << st << endl;
            dis[st] = cnt + dis[st] - tmp;
            sort(dis+st , dis + n);
            //for(int i = 0 ; i < n ; i++) cout << dis[i] << " ";cout << endl;
            int k = 0;
            for(int i = n - 1; i >= st ; i--){
                if(k < l){
                    ans += dis[i];
                    k++;
                }
                else ans += dis[i]*2LL;
            }
            cout << "Case #" << cas << ": ";
            cout << ans << endl;
        }
    }
    return 0;
}

