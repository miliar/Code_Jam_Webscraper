#include<iostream>
#include<cmath>

using namespace std;

FILE *fin=freopen("A-large.in","r",stdin);
FILE *fout=freopen("probA.out","w",stdout);

int main() {
    int t, pO, pB,tO,tB;
    int T;
    cin>>T;
    for(int i =0;i<T;i++) {
        pO=pB=1;
        t=0;
        tO=tB=0;
        int M;
        cin>>M;
        for(int j=0;j<M;j++) {
            char c1;
            cin>>c1;
            int pos;
            cin>>pos;
            if(c1=='O') {
                if(abs(pos-pO)>=(t-tO))
                    t+=abs(pos-pO)-(t-tO);

                pO=pos;
                tO=t+1;
            }
            if(c1=='B') {
                if(abs(pos-pB)>=(t-tB))
                    t+=abs(pos-pB)-(t-tB);
                pB=pos;
                tB=t+1;
            }
            t+=1;
            cin.get();
        }
        cout<<"Case #"<<(i+1)<<": "<<t<<"\n";
    }
    return 0;
}
