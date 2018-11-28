#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream in("b.in");
ofstream out("b.out");
    
void solve() {
    int n,s,p;
    in>>n>>s>>p;
    int res = 0;
    int not_used = 0;
    for(int i = 0; i<n;i++) {
        int t;
        in>>t;
        int q = (t+2) / 3;
        if(t >= 2 && t <= 28) {
            if(q >= p) {
                res++; 
                not_used++;
            } else if(q == p-1 && s > 0) {
                res++;
                s--;
            } else {
                not_used++;
            }
        } else {
            if(q >= p) {
                res++; 
            } 
        }
    }
    out<<res;
}
int main() {
    
    
    int t;
    
    in>>t;
    
    for(int i = 0; i<t;i++) {
        
        
        out << "Case #"<<i+1<<": ";
        solve();
        out<<endl;
    }
    
    system("pause");
        
}