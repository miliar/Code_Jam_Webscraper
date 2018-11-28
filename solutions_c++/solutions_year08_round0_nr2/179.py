#include <iostream>
#include <fstream>
#include <algorithm>
std::ifstream fin("input.txt");

int N, T, Nab, Nba;
int parsetime() {
    char c = fin.get();
    while (c == ' ' || c == '\n') c = fin.get();
    int time = 600*(c-'0');
    time += 60*(fin.get()-'0');
    fin.get();
    time += 10*(fin.get()-'0');
    return time + (fin.get()-'0');
}

int main() {
    fin >> N;
    for (int i=1; i<=N; i++) {
        fin >> T >> Nab >> Nba;
        int time[2][2][200]; // station dep/arr ntime
        for (int j=0; j<Nab; j++) {
            time[0][0][j] = parsetime();
            time[1][1][j] = parsetime();
        }
        for (int j=0; j<Nba; j++) {
            time[1][0][j] = parsetime();
            time[0][1][j] = parsetime();
        }
        std::sort(time[0][0], time[0][0]+Nab);
        std::sort(time[1][1], time[1][1]+Nab);
        std::sort(time[1][0], time[1][0]+Nba);
        std::sort(time[0][1], time[0][1]+Nba);
        int k=0, trains=0, nA=0, nB=0;
        for (int j=0; j<Nab; j++) {
            while (k<Nba && time[0][1][k]+T <= time[0][0][j]) {
                trains++;
                k++;
            }
            if (trains > 0) trains--;
            else nA++;
        }
        k = trains = 0;
        for (int j=0; j<Nba; j++) {
            while (k<Nab && time[1][1][k]+T <= time[1][0][j]) {
                trains++;
                k++;
            }
            if (trains > 0) trains--;
            else nB++;
        }
        printf("Case #%i: %i %i\n", i, nA, nB);
    }
}

