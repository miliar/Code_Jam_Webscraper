#include <iostream>
#include <cmath>

using namespace std;

long double dis(long double px, long double py, long double qx, long double qy){
       return sqrt((px-qx)*(px-qx)+(py-qy)*(py-qy));
}

long double overlap(long double r1, long double r2, long double d){
       long double t1 = r1*r1*acos((d*d+r1*r1-r2*r2)/(2*d*r1));
       long double t2 = r2*r2*acos((d*d+r2*r2-r1*r1)/(2*d*r2));
       long double t3 = 1.0/2.0*sqrt((d+r1+r2)*(-d+r1+r2)*(d+r1-r2)*(d-r1+r2));
       return t1 + t2 - t3;
}

int main(){
    cout.setf(ios::fixed);
    cout.precision(12);
    int Nc; cin >> Nc;
    for (int QQ = 1; QQ <= Nc; QQ++){
        int N,M; cin >> N >> M;
        long double Px[N]; long double Py[N];
        long double Qx[M]; long double Qy[M];
        long double radius[N];
        for (int i=0;i<N;i++){
            cin >> Px[i] >> Py[i];
            radius[i] = 1000000000;
        }
        for (int i=0;i<M;i++){
            cin >> Qx[i] >> Qy[i];
        }/*
        for (int i=0;i<N;i++){
            for (int j=0;j<M;j++) radius[i] <?= dis(Px[i],Py[i],Qx[j],Qy[j]);
        }*/
        long double best = 1000000000;
        long double rb1,rb2;
        // Caso facil
        /*
        for (int i=0;i<M;i++){
            for (int j=0;j<M;j++){
                long double r1,r2,d;
                r1 = dis(Qx[i],Qy[i],Px[0],Py[0]);
                r2 = dis(Qx[j],Qy[j],Px[1],Py[1]);
                d = dis(Px[0],Py[0],Px[1],Py[1]);
                long double ov = overlap(r1,r2,d);
                if (ov < best){
                   best = ov;
                   rb1 = r1; rb2 = r2;
                }
            }
        }*/
        
        cout << "Case #" << QQ << ":";
        for (int i = 0; i < M; i++){
            long double r1,r2,d;
            r1 = dis(Qx[i],Qy[i],Px[0],Py[0]);
            r2 = dis(Qx[i],Qy[i],Px[1],Py[1]);
            d = dis(Px[0],Py[0],Px[1],Py[1]);
            cout << " " << overlap(r1,r2,d);
        } cout << endl;
    }
    return 0;
}
