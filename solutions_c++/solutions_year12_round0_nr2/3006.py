#include<iostream>
using namespace std;
   
int main() {
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int T, S, p, N;
    int total;
    int over = 0, hit = 0;
    cin >> T;
    for (int i = 0; i < T; ++ i) {
        cin >> N >> S >> p;
        over = 0; hit = 0;
        for (int j = 0; j < N; ++ j) {
            cin >> total;
            int f = 3*p-4;
            if (f < 0)
                f = 1;
            if (total >= (3*p-2))
                ++ over;
            else if ((total < (f+2))&&(total >= f))
                ++ hit;
        }
        if (hit < S)
            over += hit;
        else
            over += S;
        if (p == 0) over = N;
        cout << "Case #"<<i+1<<": "<<over<<endl;        
    }    
    return 0;
}    
        
                      
