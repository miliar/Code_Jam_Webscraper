#include <iostream>
//{[
using namespace std;

int main()
{
    int t=0,T,n=0,N;
    cin >> T;
    while(t<T){
        t++;
        cin >> N;n=0;
        int cur=0,rB=0,rO=0,pB=1,pO=1;
        while(n<N){
            n++;
            char R;
            int P;
            cin >> R >> P;
            if(R=='O'){
                int m = abs(pO-P)+1;
                if(cur<rO+m){cur=rO+m; rO+=m;}else {cur++;rO=cur;}
                pO=P;
            }else{
                int m = abs(pB-P)+1;
                if(cur<rB+m){cur=rB+m; rB+=m;}else {cur++;rB=cur;}
                pB=P;
            }

            //cout << R << P << "cur:" << cur  << " rB:" << rB  << " rO:" << rO  << " pB:" << pB  << " pO:" << pO << endl;
        }
        cout << "Case #" << t << ": " << cur <<endl;
    }
    return 0;
}
