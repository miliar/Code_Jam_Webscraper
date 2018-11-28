#include <iostream>
#include <vector>
#include <iomanip>


using namespace std;

typedef pair<long double,long double> PII;
typedef pair<long double,PII> PIII;

#define s first
#define b second.first
#define e second.second

int main(){
    int Tc;
    cin >> Tc;
    for(int tc=1;tc<=Tc;tc++){
            long double X, S, R, t, N;
            cin >> X >> S >> R >> t >> N;
            vector<PIII> w((int)N);
            long double nw = X;
            for(int i=0;i<N;i++){
                    cin >> w[i].b >> w[i].e >> w[i].s;
                    nw -= w[i].e - w[i].b;
            }
            w.push_back(PIII(0, PII(0, nw)));
            sort(w.begin(),w.end());
            long double sol = 0;
            for(int i=0;i<w.size();i++){
                    long double Rt = min(t, (w[i].e - w[i].b) / (R + w[i].s));
//                    cerr << w[i].e << " " << w[i].b << " " << w[i].s << " " << Rt << " " << t << endl;
                    t -= Rt;
                    sol += Rt + ((w[i].e - w[i].b - Rt * (R + w[i].s)) / (S + w[i].s));
            }
            cout << "Case #" << tc << ": " << fixed << setprecision(10) << sol << endl;
    }
}



