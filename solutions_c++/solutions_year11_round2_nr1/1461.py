#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int c = 0; c < t; c++){
        int n;
        cin >> n;

        map<int, map<int, int> > games;
        vector<double> wp(n);
        vector<double> owp(n);
        vector<double> oowp(n);
        for(int i = 0; i < n; i++){
            string line;
            cin >> line;
            int ngames = 0;
            int nwins = 0;
            for(int j = 0; j < n; j++){
                char x = line[j];
                if(x == '.') games[i][j] = -1;
                else if(x == '0') {
                    ngames++;
                    games[i][j] = 0;
                }
                else if(x == '1') {
                    ngames++;
                    nwins++;
                    games[i][j] = 1;
                }
            }
            if(ngames > 0) wp[i] = (double) nwins / (double) ngames;
            else wp[i] = 0.0;
        }

        for(int i = 0; i < n; i++){
            double sumwp = 0;
            double numwp = 0;
            for(int j = 0; j < n; j++){
                // He is an opponent
                if(games[i][j] != -1){
                    numwp = numwp + 1.0;
                    int ngames = 0;
                    int nwins = 0;
                    for(int k = 0; k < n; k++){
                        if(k != i && games[j][k] != -1){
                            ngames++;
                            nwins += games[j][k];
                        }
                    }
                    if(ngames > 0){
                        double localwp = (double) nwins / (double) ngames;
                        sumwp += localwp;
                    }
                }
            }
            if(numwp > 0) owp[i] = sumwp / numwp;
            else owp[i] = 0.0;
        }

        for(int i = 0; i < n; i++){
            double sumowp = 0;
            int numowp = 0;
            for(int j = 0; j < n; j++){
                if(games[i][j] != -1){
                    sumowp += owp[j];
                    numowp++;
                }
            }
            if(numowp > 0) oowp[i] = sumowp / (double) numowp;
            else oowp[i] = 0.0;
        }

        cout << "Case #" << c+1 << ":" << endl;
        for(int i = 0; i < n; i++){
            double rpi = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
            cout << rpi << endl;
        }
    }

}
