#include <iostream>
#include <vector>
#include <string>
using namespace std;

string solve(int n, int k) {
    int num=1<<n;
    k%=num;
    string bits;
    while(k) {
        bits = char(k%2 + '0') + bits;
        k/=2;
    }
    if(bits.size()<n||bits.find("0")!=string::npos) return "OFF";
    else return "ON";
}

int main() {
    int t;
    cin>>t;
    int n,k;
    for (int c=1;c<=t;c++) {
        cin>>n>>k;
        cout<<"Case #"<<c<<": "<<solve(n,k)<<endl;
    }
}
