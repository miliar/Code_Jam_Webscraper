#include <cstdio>
#include <iostream>
#define MAXN 1001
using namespace std;

typedef long long int i64;

int t,r,n;
i64 q[2*MAXN];
int p[2*MAXN];
i64 k,s,sum;

int main(){
    cin >> t;
    for (int i = 0; i < t; i++){
        cin >> r >> k >> n;
        for (int j = 0; j < n; j++){
            cin >> q[j];
            p[j] = 0;
        }
        for (int j = n; j < n+n; j++){
            q[j] = q[j-n];
            p[j] = 0;
        }
        for (int j = 1; j < n+n; j++){
            q[j]+=q[j-1];
        }
        int l;
        for (int j = 0; j < n; j++){
            if (j == 0) s = 0;
            else s = q[j-1];
            l = j;
            while (q[l]-s <= k && l < j+n)l++;
            p[j] = l-j;
//            cout << p[j] << " ";
        }
//        cout << endl;
        l = 0;
        sum = 0;
        i64 g = 0;
        do{
            g++;
            if (l == 0) sum += q[l+p[l]-1];
            else sum+=q[l+p[l]-1] - q[l-1];
            l = (l+p[l]) % n;
        }while(l != 0 && g < r);
        if (g == r){
            cout << "Case #" << (i+1) << ": " << sum << endl;
        }else{
            sum = (r/g)* sum;
            r = r % g;
            g = 0;
            l = 0;
            if (r != 0)
            do{
                g++;
                if (l == 0) sum += q[l+p[l]-1];
                else sum+=q[l+p[l]-1] - q[l-1];
                l = (l+p[l]) % n;
            }while(g < r);
            cout << "Case #" << (i+1) << ": " << sum << endl;
        }
        
    }
    return 0;
}
