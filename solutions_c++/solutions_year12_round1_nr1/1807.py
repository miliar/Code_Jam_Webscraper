#include <iostream>
#include <math.h>
using namespace std;

int main() {
    int T,A,B,i,uk,count;
    float p[3],prob[8],E,KT,BO,BT;
    cin >> T;
    for (count=1; count<=T; count++) {
        cin >> A >> B;
        for (i=0; i<A; i++)
            cin >> p[i];
        switch (i) {
            case 1: prob[0] = p[0]; prob[1] = 1-p[0]; break;
            case 2:
                prob[0] = p[0]*p[1];
                prob[1] = p[0]*(1-p[1]);
                prob[2] = (1-p[0])*p[1];
                prob[3] = (1-p[0])*(1-p[1]); break;
            case 3:
                prob[0] = p[0]*p[1]*p[2];
                prob[1] = p[0]*p[1]*(1-p[2]);
                prob[2] = p[0]*(1-p[1])*p[2];
                prob[3] = p[0]*(1-p[1])*(1-p[2]); 
                prob[4] = (1-p[0])*p[1]*p[2];
                prob[5] = (1-p[0])*p[1]*(1-p[2]);
                prob[6] = (1-p[0])*(1-p[1])*p[2];
                prob[7] = (1-p[0])*(1-p[1])*(1-p[2]); break;
        }
        E=0; KT=0; BO=0; BT=0;
        uk = pow(2,i);
        //cout << uk;
        for (i=0; i<uk; i++) {
            E += (B+2)*prob[i];
            if (i<1) KT += (B-A+1)*prob[i]; else KT += (2*B+2-A)*prob[i];
            if (i<2) BO += (B-A+3)*prob[i]; else BO += (2*B+4-A)*prob[i];
            if (i<3) BT += (B-A+5)*prob[i]; else BT += (2*B+6-A)*prob[i];
        }
//        cout << E << " " << KT << " " << BO << " " << BT << endl;
        if ((E < KT) && (E < BO) && (E < BT))
            printf("Case #%d: %.6f\n",count,E);
        else if ((KT < BO) && (KT < BT))
            printf("Case #%d: %.6f\n",count,KT);
        else if (BO < BT)
            printf("Case #%d: %.6f\n",count,BO);
        else printf("Case #%d: %.6f\n",count,BT);
        
    }
}
