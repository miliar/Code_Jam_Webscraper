#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

const int NUM_LETTERS = 19;

using namespace std;

//void countW(vector<int> letters[], int curIndex, int start, int &count);

int main()
{
    int numOfCases;
    cin >> numOfCases;
    cin.get();

    for (int i = 0; i < numOfCases; i++)
    {
        string tmp;
        getline(cin, tmp, '\n');
        int tmpLength = tmp.length();

        vector<int> letters[NUM_LETTERS];
        int count = 0;

        for (int j = 0; j < tmpLength; j++)
        {
            if (tmp[j] == 'w')
            { letters[0].push_back(j); }
            else if (tmp[j] == 'e') {
                letters[1].push_back(j);
                letters[6].push_back(j);
                letters[14].push_back(j);
            } else if (tmp[j] == 'l') {
                letters[2].push_back(j);
            } else if (tmp[j] == 'c') {
                letters[3].push_back(j);
                letters[11].push_back(j);
            } else if (tmp[j] == 'o') {
                letters[4].push_back(j);
                letters[9].push_back(j);
                letters[12].push_back(j);
            } else if (tmp[j] == 'm') {
                letters[5].push_back(j);
                letters[18].push_back(j);
            } else if (tmp[j] == ' ') {
                letters[7].push_back(j);
                letters[10].push_back(j);
                letters[15].push_back(j);
            } else if (tmp[j] == 't') {
                letters[8].push_back(j);
            } else if (tmp[j] == 'd') {
                letters[13].push_back(j);
            } else if (tmp[j] == 'j') {
                letters[16].push_back(j);
            } else if (tmp[j] == 'a') {
                letters[17].push_back(j);
            }
        }

        /*for (unsigned int j = 0; j < letters[0].size(); j++)
        {
            countW(letters, 0, j, count);
        }*/

        for (unsigned int j = 0; j < letters[0].size(); j++) {
            for (unsigned int j1 = 0; j1 < letters[1].size(); j1++) {
                if (letters[0][j] < letters[1][j1]) {
                for (unsigned int j2 = 0; j2 < letters[2].size(); j2++) {
                    if (letters[1][j1] < letters[2][j2]) {
                    for (unsigned int j3 = 0; j3 < letters[3].size(); j3++) {
                        if (letters[2][j2] < letters[3][j3]) {
                        for (unsigned int j4 = 0; j4 < letters[4].size(); j4++) {
                            if (letters[3][j3] < letters[4][j4]) {
                            for (unsigned int j5 = 0; j5 < letters[5].size(); j5++) {
                                if (letters[4][j4] < letters[5][j5]) {
                                for (unsigned int j6 = 0; j6 < letters[6].size(); j6++) {
                                    if (letters[5][j5] < letters[6][j6]) {
                                    for (unsigned int j7 = 0; j7 < letters[7].size(); j7++) {
                                        if (letters[6][j6] < letters[7][j7]) {
                                        for (unsigned int j8 = 0; j8 < letters[8].size(); j8++) {
                                            if (letters[7][j7] < letters[8][j8]) {
                                            for (unsigned int j9 = 0; j9 < letters[9].size(); j9++) {
                                                if (letters[8][j8] < letters[9][j9]) {
                                                for (unsigned int j10 = 0; j10 < letters[10].size(); j10++) {
                                                    if (letters[9][j9] < letters[10][j10]) {
                                                    for (unsigned int j11 = 0; j11 < letters[11].size(); j11++) {
                                                        if (letters[10][j10] < letters[11][j11]) {
                                                        for (unsigned int j12 = 0; j12 < letters[12].size(); j12++) {
                                                            if (letters[11][j11] < letters[12][j12]) {
                                                            for (unsigned int j13 = 0; j13 < letters[13].size(); j13++) {
                                                                if (letters[12][j12] < letters[13][j13]) {
                                                                for (unsigned int j14 = 0; j14 < letters[14].size(); j14++) {
                                                                    if (letters[13][j13] < letters[14][j14]) {
                                                                    for (unsigned int j15 = 0; j15 < letters[15].size(); j15++) {
                                                                        if (letters[14][j14] < letters[15][j15]) {
                                                                        for (unsigned int j16 = 0; j16 < letters[16].size(); j16++) {
                                                                            if (letters[15][j15] < letters[16][j16]) {
                                                                            for (unsigned int j17 = 0; j17 < letters[17].size(); j17++) {
                                                                                if (letters[16][j16] < letters[17][j17]) {
                                                                                    for (unsigned int j18 = 0; j18 < letters[18].size(); j18++) {
                                                                                        if (letters[17][j17] < letters[18][j18]) {
                                                                                            count++;
                                                                                        }}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
        }



        cout << "Case #" << i+1 << ": " << setw(4) << setfill('0') << count << endl;
    }

    return 0;
}

/* void countW(vector<int> letters[], int curIndex, int start, int &count)
{
    if (curIndex == NUM_LETTERS-1) {
        count += letters[curIndex].size() - start;
    } else {
        for (unsigned int i = 0; i < letters[curIndex+1].size(); i++)
        {
            if (letters[curIndex][start] < letters[curIndex+1][i]) {
                countW(letters, curIndex+1, i, count);
            }
        }
    }
} */
