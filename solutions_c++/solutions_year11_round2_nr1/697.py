#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> WPa, WPb;
vector<double> OWP, OOWP;
vector<string> T;
int N;

double WP(int i, int x) {
    if (T[i][x]=='1') return double(WPa[i]-1)/double(WPb[i]-1);
    else if (T[i][x]=='0') return double(WPa[i])/double(WPb[i]-1);
    else return double(WPa[i])/double(WPb[i]);
}

int main() {
    
    int TT; cin>>TT;
    for (int t=1; t<=TT; t++) {
        cin>>N;
        
        T.clear(), WPa.clear(), WPb.clear(), OWP.clear(), OOWP.clear();
        
        for (int i=0; i<N; i++) {
            string s; cin>>s;
            T.push_back(s);
        }
        
        // calc WP
        for (int i=0; i<N; i++) {
            int won=0, played=0;
            for (int j=0; j<N; j++) {
                if (T[i][j]=='1') won++, played++;
                else if (T[i][j]=='0') played++;
            }
            WPa.push_back(won);
            WPb.push_back(played);
            //WP.push_back(double(won)/double(played));
            //cout<<"WP["<<i<<"]="<<WP[i]<<endl;
        }

        // calc OWP
        for (int i=0; i<N; i++) {
            int z=0;
            double sum=0;
            for (int j=0; j<N; j++) {
                if (T[i][j]!='.' && i!=j) sum+=WP(j, i), z++;
            }
            OWP.push_back(sum/z); //cerr<<"sum/z "<<sum<<"/"<<z<<endl;
//             cerr<<"OWP["<<i<<"]="<<OWP[i]<<endl;
        }

        // calc OOWP
        for (int i=0; i<N; i++) {
            int z=0;
            double sum=0;
            for (int j=0; j<N; j++) {
                if (T[i][j]!='.') sum+=OWP[j], z++;
            }
            OOWP.push_back(sum/z);
//             cout<<"OOWP["<<i<<"]="<<OOWP[i]<<endl;
        }
        
        cout<<"Case #"<<t<<":"<<endl;
        for (int i=0; i<N; i++)
            cout.precision(10), cout<<(0.25*double(WPa[i])/double(WPb[i])+0.50*OWP[i]+0.25*OOWP[i])<<endl;
    }
    
    return 0;
}
