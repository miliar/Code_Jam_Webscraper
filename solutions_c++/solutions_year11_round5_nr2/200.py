#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int T[10002];
int N;


int main() {
    int Z; cin>>Z;
    for (int z=1; z<=Z; z++) {
    
        fill(T, T+10002, 0);
        cin>>N;
        
        if (N==0) {
            cout<<"Case #"<<z<<": 0"<<endl;
            continue;
        }
        
        for (int i=0; i<N; i++) {
            int x; cin>>x;
            T[x+1]++;
        }
        
        for (int i=0; i<10001; i++)
            T[i] -= T[i+1];
        
        
        int result=1000000;
        int i=0;
        for (int j=1; j<=10001; j++) {
            for (int k=0; k<T[j]; k++) {
                while (T[i]>=0) i++;
                T[i]++;
                result = min(result, j-i);
            }
        }
        
        cout<<"Case #"<<z<<": ";
        cout<<result<<endl;
    }
    
    return 0;
}
