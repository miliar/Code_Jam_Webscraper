#include <fstream>
#include <vector>

using namespace std;

int main()
{
    int cases, N, P;
    char R;
    fstream fin;
    fin.open("input.in");
    ofstream fout;
    fout.open("output.txt");
    fin >> cases;
    for (int counter = 1; counter <= cases; counter++) {
        vector<int> positions;
        vector<char> robots;
        fin >> N;
        int currPosO = 1, currPosB = 1;
        for (int i = 0; i < N; i++) {
            fin >> R >> P;
            robots.push_back(R);
            positions.push_back(P);
        }
        int turns = 0, passedSince = 0;
        char lastPlayer = robots.at(0);
        while (robots.size() > 0) {
            if ((robots.at(0) == 'O' && positions.at(0) == currPosO) ||
                (robots.at(0) == 'B' && positions.at(0) == currPosB)) {
                    turns++;
                    if (lastPlayer != robots.at(0)) {
                        passedSince = 0;
                    }
                    passedSince++;
                    lastPlayer = robots.at(0);
                    robots.erase(robots.begin() + 0);
                    positions.erase(positions.begin() + 0);
            } else {
                if (robots.at(0) == 'O') {
                    if (positions.at(0) > currPosO) {
                        if (passedSince > 0 && lastPlayer == 'B') {
                            passedSince--;
                        } else {
                            turns++;
                            passedSince++;
                            lastPlayer = 'O';
                        }
                        currPosO++;
                    } else {
                        if (passedSince > 0 && lastPlayer == 'B') {
                            passedSince--;
                        } else {
                            turns++;
                            passedSince++;
                            lastPlayer = 'O';
                        }
                        currPosO--;
                    }
                } else {
                    if (positions.at(0) > currPosB) {
                        if (passedSince > 0 && lastPlayer == 'O') {
                            passedSince--;
                        } else {
                            turns++;
                            passedSince++;
                            lastPlayer = 'B';
                        }
                        currPosB++;
                    } else {
                        if (passedSince > 0 && lastPlayer == 'O') {
                            passedSince--;
                        } else {
                            turns++;
                            passedSince++;
                            lastPlayer = 'B';
                        }
                        currPosB--;
                    }
                }
            }
        }
        fout << "Case #" << counter << ": " << turns << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
