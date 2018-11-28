#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char** argv){
    int casos, t, n, i, j;
    char tabla[105][105];
    int jugados[105];
    int ganados[105];
    double wp[105], owp[105], oowp[105];
    double score;
    int total;

    cout.precision(9);
    ofstream salida("A.out.txt");
    cout.rdbuf(salida.rdbuf());

    cin >> casos;
    for(t=1; t<=casos; t++){
        cin >> n;
        for(i=0; i<n; i++){
            for(j=0; j<n; j++)cin >> tabla[i][j];
        }

        for(i=0; i<n; i++){
            jugados[i] = ganados[i] = 0;
            for(j=0; j<n; j++){
                if(tabla[i][j]!='.') jugados[i]++;
                if(tabla[i][j]=='1') ganados[i]++;
            }

        }

        for(i=0; i<n; i++){
            wp[i] = double(ganados[i])/jugados[i];
        }

        for(i=0; i<n; i++){
            score = 0;
            total = 0;
            for(j=0; j<n; j++){
                if(tabla[j][i]!='.'){
                    if(tabla[j][i]=='1') score += double(ganados[j]-1)/(jugados[j]-1);
                    else score += double(ganados[j])/(jugados[j]-1);
                    total++;
                }
            }
            owp[i] = score/total;
        }

        for(i=0; i<n; i++){
            score = 0;
            total = 0;
            for(j=0; j<n; j++){
                if(tabla[j][i]!='.'){
                    score += owp[j];
                    total++;
                }
            }
            oowp[i] = score/total;
        }

        cout << "Case #"<<t<<":"<<endl;
        for(i=0; i<n; i++){
            cout << 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i] << endl;
            //cout << "wp:" << wp[i] << " owp:" << owp[i] << " oowp:" << oowp[i] << endl;
        }
    }
	return 0;
}
