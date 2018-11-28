#include<iostream>
#include<set>
using namespace std;
  
int getN(long long int x) {
    int n = 1;
    while(x/n) {
        n *= 10;
    }    
    return n/10;
}    
int main() {
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    set<long long int> s;   
    int T, hit;
    long long int A, B;
    cin >> T;
    for (int i = 0; i < T; ++ i) {
        cin >> A >> B;
        s.clear();
        long long int tmp;
        int N, n;
        for (long long int x = A; x <= B; ++ x) {
            N = getN(x);
            n = 10;
            while (true) {
                tmp = (x%N)*n+(x/N);
                if (tmp == x)
                    break; 
                if ((tmp>=A)&&(tmp<=B)) {
                    if (tmp < x) {
                        tmp = (tmp << 32) | x;
                    }
                    else {
                        tmp = (x << 32) | tmp;
                    }
                    s.insert(tmp);
                }              
                n *= 10;
                N /= 10; 
            }    
        }    
        cout << "Case #"<<i+1<<": "<<s.size()<<endl;        
    }    
    return 0;
}    
        
                      
