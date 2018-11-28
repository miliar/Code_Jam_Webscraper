#include <iostream>
#include <sstream>

using namespace std;

int main(){
    int cases; cin >> cases;
    int answers[cases];
    cin.clear(); cin.sync();
    for (int t = 0; t < cases; t++) {
        char input[210];
        cin.getline(input, 210, '\n');
        stringstream ss (stringstream::in | stringstream::out);
        ss << input;
        int n; ss >> n;
        char R; int P;
        int Opos, Bpos; Opos = Bpos = 1;
        int time = 0;
        int Otime, Btime; Otime = Btime = 0;
        for (int i = 0; i < n; i++) {
            ss >> R; ss >> P;
            if (R == 'O') {
                time -= Otime;
                Otime += abs(Opos - P);
                if (Otime <= Btime) Otime = Btime;
                Otime -= Btime - 1; Btime = 0;
                Opos = P;
                time += Otime;
            }
            else if (R == 'B') {
                time -= Btime;
                Btime += abs(Bpos - P);
                if (Btime <= Otime) Btime = Otime;
                Btime -= Otime - 1; Otime = 0;
                Bpos = P;
                time += Btime;
            }
        }
        answers[t] = time;
    }
    for (int t = 0; t < cases; t++)
        cout << "Case #" << t+1 << ": " << answers[t] << endl;
    //system("PAUSE");
    return 0;
}
