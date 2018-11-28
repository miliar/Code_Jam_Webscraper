#include <iostream>
#include <vector>
using namespace std;

long double X, S, R, T;

vector<pair<long double, long double> > V;

int N;



int main() {
    int Z; cin>>Z;
    for (int z=1; z<=Z; z++) {
        cin>>X>>S>>R>>T>>N;
        
        long double result = 0;
        
        V.clear();
        
        for (int i=0; i<N; i++) {
            long double b, e, w;
            cin>>b>>e>>w;
            V.push_back(pair<long double, long double>(w, e-b));
            X-=e-b;
        }
        
        V.push_back(pair<long double, long double>(0, X));
        
        sort(V.begin(), V.end());
        
        for (int i=0; i<N+1; i++) {
            long double d = V[i].second;
            long double v1 = V[i].first+R;
            long double v2 = V[i].first+S;
            long double t1 = min(T, d/v1);
            d -= t1*v1;
            long double t2 = d/v2;
            
            result += t1+t2;
            T-=t1;
        }
    
        cout<<"Case #"<<z<<": ";
        cout.precision(25);
        cout<<result<<endl;
    }
    
    return 0;
}
