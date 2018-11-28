#include <iostream>

using namespace std;

int main(int ac, char* av[])
{
    int i,T,N,K;
    cin >> T;
    for(i=0; i<T;i++) {
        int s = 0;
        cin >> N >> K;
        if(N>0) {
            s = K & 1;
            --N;
            for( ; s!=0 && N>0; --N) {
                K >>= 1;
                s = s & K & 1;
            }
        }
        
        cout << "Case #" << (i+1) << ": "
            << (s&1 ? "ON" : "OFF")
            << endl;
    }
    
    return 0;
}
