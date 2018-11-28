#include <iostream>
#include <fstream>
using namespace std;

int N,K;
bool solve(){
        int table[32]={
                1,
                2,
                4,
                8,
                16,
                32,
                64,
                128,
                256,
                512,
                1024,
                2048,
                4096,
                8192,
                16384,
                32768,
                65536,
                131072,
                262144,
                524288,
                1048576,
                2097152,
                4194304,
                8388608,
                16777216,
                33554432,
                67108864,
                134217728,
                268435456,
                536870912,
                1073741824,
                2147483648
        };
        int sum = table[N];
        if( (K+1)%sum == 0)
                return true;
        else
                return false;
}
int main(){
        int C;
        cin>>C;
        for(int i = 0; i <C; i++){
                cin>>N>>K;
                cout<<"Case #"<<(i+1)<<": ";
                if(solve())
                        cout<<"ON"<<endl;
                else
                        cout<<"OFF"<<endl;
        }
        return 0;
}
