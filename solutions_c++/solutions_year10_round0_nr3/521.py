#include <iostream>
#include <cstdio>
using namespace std;

        long long R, k;
        int n;
        long long a[2010];
        long long s[2010], p[1010], c[1010], d[1010];

int main(){
    freopen("C-large.in","r",stdin);
    freopen("c.out","w",stdout);
    
    int ntest;
    cin>>ntest;
    for (int test=1;test<=ntest;test++){

        memset(d, 0, sizeof(d)); // sum of the longest chain start at i
        memset(c, 0, sizeof(c));
        memset(a, 0, sizeof(a));
        memset(s, 0, sizeof(s)); // value of res at that start point
        memset(p, 0, sizeof(p)); // value of R at that start point

        cin>>R>>k>>n;
        
        for (int i=0;i<n;i++){
            cin>>a[i];
            a[i+n] = a[i];
        }

        // check if all can fit to the
        long long sum=0;
        for (int i=0;i<n;i++){
            sum+= a[i];
        }
        if (sum <= k){
            cout<<"Case #"<<test<<": "<<sum*R<<endl;
            continue;
        }

        // find the next starting point
        int j=0;
        sum = 0;
        while (sum + a[j] <= k) sum += a[j++];
        c[0] = j;
        d[0] = sum;

        for (int i=1;i<n;i++){
            sum -= a[i-1];
            while (sum + a[j] <= k) sum+=a[j++];
            c[i] = j % n;
            d[i] = sum;
        }
        
        long long res = 0;
        
        // find the circle that starting point will fall into
        int start = 0;
        while (R>0 && p[start] == 0){
            p[start] = R;
            s[start] = res;

//            cout<<start<<" "<<res<<" "<<R<<endl;
            res += d[start];
            start = c[start];
            R--;
        }
        
//        cout<<R<<" "<<res<<" "<<start<<endl;
        
        if (R>0){
            // if not running out of R and find the circle
            int length = p[start] - R;
            long long sum_circle = res - s[start];
            res += sum_circle * (R / length);
            R %= length;
        }
        
        while (R>0){
            res+=d[start];
            start = c[start];
            R--;
        }

        cout<<"Case #"<<test<<": "<<res<<endl;
    }
    
    return 0;
}
