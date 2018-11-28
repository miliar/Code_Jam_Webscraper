#include <cstdlib>
#include <iostream>

#define NS 100

using namespace std;

int main() {
    int nCase;
    cin>>nCase;
    for(int n=1; n<=nCase; n++) {
        cout<<"Case #"<<n<<": ";
        char sym[NS];
        int dig[NS];
        string inp;
        cin>>inp;
        for(int a=0; a<NS; a++) dig[a] = sym[a] = 0;
        for(int a=0; a<inp.size(); a++) {
            bool match = 0;
            for(int b=0; b<NS; b++) {
                if(sym[b] == inp[a]) {
                    dig[a] = b;
                    match = 1;
                }
            }
            if(!match) {
                for(int b=0; b<NS; b++) {
                    if(b==0 && a==0) b++;
                    if(sym[b]==0) {
                        sym[b] = inp[a];
                        dig[a] = b;
                        break;
                    }
                }
            }
        }
        int base = 0;
        for(int a=0; a<NS; a++) if(sym[a]!=0) base++;
        if(base<2) base = 2;
        unsigned long long total = 0;
        for(int a=0; a<inp.size(); a++) {
            total*=base;
            total+=dig[a];
        }
        cout<<total<<endl;
    }
    return 0;
}
