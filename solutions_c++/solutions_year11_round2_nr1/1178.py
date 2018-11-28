
#include <fstream>
#include <iostream>

using namespace std;

int main() {
    
    ifstream fin;
    ofstream fout;
    int t, n;
    char table[110][110];
    double wp[110], owp[110], oowp[110], rpi[110];
    
    
        
    fin.open("A.in", ios_base::in);
    fout.open("A.out", ios_base::out);
    
    fin >> t;
    for (int i = 0; i < t; i++) {
        fin >> n;
       
        for (int j = 0; j < n; j++) {
            fin >> table[j];
            table[j][n] = '\0';
        }
        
        for (int j = 0; j < n; j++) {
            int won = 0, played = 0;
            for (int h = 0; h < n; h++) {
                if (table[j][h] != '.') {
                    played++;
                    if (table[j][h] == '1') {
                        won++;
                    }
                }
            }
            wp[j] = ((double)won) / ((double)played);
            //cout << wp[j] << endl;
        }
        
        for (int j = 0; j < n; j++) {
            double sum = 0.0;
            int opp= 0;
            for (int k = 0; k < n; k++) {
                if ((k != j) && (table[k][j]!='.')) {
                    opp++;
                    int won = 0, played = 0;
                    for (int h = 0; h < n; h++) {
                        if (h != j) {
                            if (table[k][h] != '.') {
                                played++;
                                if (table[k][h] == '1') {
                                    won++;
                                }
                            }
                        }
                    }
                    sum += ((double)won) / ((double)played);
                }
            }
            owp[j] = sum / ((double)(opp));
//            cout << owp[j] << endl;
        }
        
        for (int j = 0; j < n; j++) {
            double sum = 0.0;
            int opp = 0;
            for (int k = 0; k < n; k++) {
                if ((k != j) && (table[k][j]!='.')) {
                    opp++;
                    sum += owp[k];
                }
            }
            oowp[j] = sum / ((double)(opp));
//            cout << oowp[j] << endl;
        }
        
        fout << "Case #" << i+1 << ":" << endl;
        
        for (int j = 0; j < n; j++) {
            double rpi = 0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j];
            fout << rpi << endl;
        }
        
    }
    
    fin.close();
    
    fout.close();
}
