#include <iostream>
#include <algorithm>

using namespace std;

const int MAXN = 1000000;
const double MAXT = 1e+12;
const int MAXI = 70;

int n,d;
int initial[MAXN];

inline bool test(double t){
    double pos = initial[0] - t;
    for(int i=1;i<n;++i){
        if(initial[i] < pos + d){
            double npos = initial[i] + t;
            if(npos < pos+d){
                return false;
            }
            pos = pos + d;
        }
        else{
            double npos = initial[i] - t;
            if(npos < pos + d){
                npos = pos + d;
            }
            pos = npos;
        }
    }
    
    return true;
}

int main(){
    int t;
    cin >> t;
    
    for(int lp=1;lp<=t;++lp){
        int c;
        cin >> c >> d;
        n = 0;
        for(int i=0;i<c;++i){
            int p,v;
            cin >> p >> v;
            for(int j=n;j<n+v;++j){
                initial[j] = p;
            }
            n += v;
        }
        
        double low = 0;
        double high = MAXT;
        
        for(int it=0;it<MAXI;++it){
            double mid = (low+high)/2;
            
            if(test(mid)){
                high = mid;
            }
            else{
                low = mid;
            }
        }
        
        cout << "Case #" << lp << ": " << low << "\n";
    }
    
    return 0;
}