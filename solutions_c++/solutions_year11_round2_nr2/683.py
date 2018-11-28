#include <string>
#include <vector>
#include <iostream>
#include <limits>
using namespace std;

int C, D;

vector<int> P, V;


bool check(long long T) {
    long long freePos = numeric_limits<long long>::min();
    for (int i=0; i<C; i++) {
        long long currPos = max(freePos, P[i]-T);
        long long lastPos = currPos+(V[i]-1)*D;
        if (lastPos-P[i] > T)
            return false;
        freePos = lastPos+D;
    }
    return true;
}


int main() {
    
    int TT; cin>>TT;
    for (int t=1; t<=TT; t++) {
        cin>>C>>D;
        D*=2;
        
        P.resize(C), V.resize(C);
        for (int i=0; i<C; i++)
            cin>>P[i]>>V[i], P[i]*=2;
        
        long long a=0, b=numeric_limits<long long>::max();
        while (a<b) {
            long long x=(a+b)/2;
            if (check(x)) b=x;
            else a=x+1;
        }
        
        cout<<"Case #"<<t<<": "<<(a/2);
        if (a%2==0) cout<<".0";
        else cout<<".5";
        cout<<endl;
    }

    return 0;
}
