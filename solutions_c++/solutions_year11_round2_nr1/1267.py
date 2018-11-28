#include <iostream>
#include <string>
#include <vector>

using namespace std;

int T;
int N;
vector<string> schedule;
int W[100]; // Wins
int G[100]; // Games
double OWP[100];
double OOWP[100];
double RPI[100];

void calc()
{
    for(int i=0; i < N; i++) {
        W[i] = 0;
        G[i] = 0;
        for(int j=0; j < N; j++) {
            if(schedule.at(i).at(j) != '.') G[i]++;
            if(schedule.at(i).at(j) == '1') W[i]++;
        }
    }
    for(int i=0; i < N; i++) {
        int num = 0;
        OWP[i] = 0.0;
        for(int j=0; j < N; j++) {
            if(schedule.at(i).at(j) == '.') continue;
            double w = W[j];
            if(schedule.at(i).at(j) == '0') w--;
            OWP[i] += w/(G[j]-1);
            num++;
        }
        OWP[i] /= num;
    }
    for(int i=0; i < N; i++) {
        int num = 0;
        OOWP[i] = 0.0;
        for(int j=0; j < N; j++) {
            if(schedule.at(i).at(j) == '.') continue;
            OOWP[i] += OWP[j];
            num++;
        }
        OOWP[i] /= num;
    }
    for(int i=0; i < N; i++) {
        RPI[i] = 0.25*W[i]/G[i] + 0.50*OWP[i] + 0.25*OOWP[i];
    }
}

int main()
{
    cin >> T;
    for(int tc=0; tc < T; tc++) {
        cin >> N;
        schedule.clear();
        for(int i=0; i<N; i++) {
            string row;
            for(;;) {
                getline(cin, row);
                if(!row.empty()) break;
            }
            schedule.push_back(row);
        }
        calc();
        cout << "Case #" << tc+1 << ":\n";
        for(int i=0; i<N; i++) {
            cout << RPI[i] << endl;
        }
    }
    return 0;
}
