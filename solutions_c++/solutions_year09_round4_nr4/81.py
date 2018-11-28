#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>

using namespace std;

int x[40], y[40], r[40];
int n;

bool f(double R) {
    vector<long long> v;
    for(int i=0; i<n; i++) {
        for(int j=i+1; j<n; j++) {
            double a = R - r[i], b = R - r[j];
            double c = hypot(x[i]-x[j], y[i]-y[j]);
            if(a <= 0 or b <= 0 or c > a+b) continue;
            double theta = acos((a*a + c*c - b*b) / (2*a*c));
            double phi = atan2(y[j]-y[i], x[j]-x[i]);

            {
                double x0 = x[i] + a*cos(phi + theta);
                double y0 = y[i] + a*sin(phi + theta);

                long long L = 0;
                for(int k=0; k<n; k++) {
                    bool b = (k == i or k == j or hypot(x[k]-x0, y[k]-y0)+r[k] <= R);
                    if(b) L |= (1LL << k);
                }
                v.push_back(L);
            }
            {
                double x0 = x[i] + a*cos(phi - theta);
                double y0 = y[i] + a*sin(phi - theta);
                long long L = 0;
                for(int k=0; k<n; k++) {
                    bool b = (k == i or k == j or hypot(x[k]-x0, y[k]-y0)+r[k] <= R);
                    if(b) L |= (1LL << k);
                }
                v.push_back(L);
            }
        }
    }

    long long full = (1LL << n) - 1;
    for(size_t i=0; i<v.size(); i++) {
        long long L = full ^ v[i];
        if(v[i] == full) return true;
        else if(not (L & (L-1))) {
            return true;
        }
        else {
            for(size_t j=i+1; j<v.size(); j++) {
                if((v[i] | v[j]) == full) return true;
            }
        }
    }
    return false;
}

int main() {
    int T;
    cin >> T;
    for(int t=1; t<=T; t++) {
        double low = 0;
        cin >> n;
        for(int i=0; i<n; i++) {
            cin >> x[i] >> y[i] >> r[i];
            low = max<double>(low, r[i]);
        }
        double high = low;

        if(n >= 3) { 
            high = 1600;
            while(high - low > 1e-6) {
                double mid = (high + low) / 2;
                if(f(mid)) high = mid;
                else low = mid;
            }
        }

        printf("Case #%d: %.8f\n", t, high);
    }
}

