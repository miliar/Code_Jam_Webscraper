#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int maxn = 20000010;

long long a[maxn];
long long b[maxn];
long long L, t, N, C;


long long Cal(){
    long long sum=0;
    long long cur;
    long long ret = 0;

    int i = 0, j = 0;
    for(;sum < t && j < N; i = (i + 1) % C, j ++)
        sum += a[i];

    int cnt = 0;
    if(sum >= t){
        cur = sum;
        cnt = 0;
        b[cnt ++ ] = sum - t;
        for(;j < N; i = (i + 1) % C, j ++){
            cur += a[i];
            b[cnt ++ ] = a[i];
        }
        if(cnt <= L){
            ret = cur / 2;
        }
        else{
            sort(b, b + cnt);
            sum = 0;
            for(i = cnt - 1; i >= cnt - L; i --)
                sum += b[i];
            ret = sum / 2 + cur - sum;
        }
    }
    else{
        ret = sum;
    }

    return ret;
}

int main(){
    freopen("B-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T;
    cin >> T;


    for(int k = 1; k <= T; k ++){

        cin >> L >> t >> N >> C;
        for(int i = 0; i < C; i ++){
            cin >> a[i];
            a[i] <<= 1;
        }

        cout << "Case #" << k << ": " << Cal() << endl;
    }
}
