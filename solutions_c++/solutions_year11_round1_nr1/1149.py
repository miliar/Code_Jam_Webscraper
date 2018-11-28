#include <iostream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; i++)

#define FORI(i,b,a) for(int i = b - 1 ; i >= a ; i--)

#define LL long long
#define ULL unsigned long long
#define UI unsigned int

#define VI vector<int>
#define VS vector<string>

#define pb push_back

int gcd(int a,int b) {
    if(a%b == 0) return b;
    else return gcd(b,a%b);
}

int main() {
    int tc,T;
    LL N;
    int pd,pg;
    int d;
    cin>>tc;
    FOR(T,1,tc+1) {
                  
        cin>>N>>pd>>pg;
        int tPlayed;
        
        if(pd == 0 && pg >= 0 && pg != 100) {
                  cout << "Case #"<<T<< ": " << "Possible" << endl;
                  continue;
        }
        if(pd == 0 && pg == 100) {
                  cout << "Case #"<<T<< ": " << "Broken" << endl;
                  continue;
        }
        
        else {
             d = gcd(100,pd);
             tPlayed = 100 / d;
        }
        
        if(tPlayed <= N ) {
              if(pg == 0 && pd != 0) {
                  cout << "Case #"<<T<< ": " << "Broken" << endl;
                  continue;
              }
              if(pg == 100 && pd != 100) {
                  cout << "Case #"<<T<< ": " << "Broken" << endl;
                  continue;
              }
              cout << "Case #"<<T<< ": " << "Possible" << endl;
        }
        else {
            cout << "Case #"<<T<< ": " << "Broken" << endl;
        }
        
    }
    return (0);
}
