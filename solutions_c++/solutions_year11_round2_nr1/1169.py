#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

struct team{
    double jugados;
    double ganados;
    vector<int> contrarios;
    double WP, OWP, OOWP;
};
    

int main(){
    ofstream fout ("out.out");
    ifstream fin ("in.in");
    int t;
    fin >> t;
    for (int caso = 1; caso <= t; caso++){
        int n;
        fin >> n;
        string s;
        vector<team> teams (n);
        vector<string> games (n);
        for (int i = 0; i < n; i++){
            fin >> s;
            games[i] = s;
            for (int j = 0; j < n; j++){
                if (s[j] == '1') teams[i].ganados++;
                if (s[j] != '.'){ 
                    teams[i].jugados++;
                    teams[i].contrarios.push_back(j);
                }
            }
            teams[i].WP = teams[i].ganados/teams[i].jugados;
        }
        for (int i = 0; i < n; i++){
            double res = 0;
            for (int j = 0; j < teams[i].contrarios.size(); j++){
                int opp = teams[i].contrarios[j];
                double jtmp = teams[opp].jugados, gtmp = teams[opp].ganados;
                jtmp--;
                if (games[opp][i] == '1') gtmp--;
                double tmp = gtmp/jtmp;
                res+=tmp;
            }
            teams[i].OWP = res/teams[i].jugados;
        }
        fout << "Case #" << caso << ":" << endl;
        for (int i = 0; i < n; i++){
            double res = 0;
            for (int j = 0; j < teams[i].contrarios.size(); j++){
                int opp = teams[i].contrarios[j];
                res+=teams[opp].OWP;
            }
            teams[i].OOWP = res/teams[i].jugados;
            double WP = teams[i].WP, OWP = teams[i].OWP, OOWP = teams[i].OOWP;
            fout << 0.25*WP+0.5*OWP+0.25*OOWP << endl;
        }
    }
}
