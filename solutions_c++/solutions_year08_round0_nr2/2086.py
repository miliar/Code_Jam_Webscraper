#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

#define N           1000
#define COL         4

#define DEPARTURE   0
#define ARRIVAL     1
#define PLATFORM    2
#define USED        3

#define YES         1
#define NO          0

#define PLATFORMA   0
#define PLATFORMB   1


void printData(int data[N][COL], int total) {
    for(int i = 0; i < total; i++) {
        for (int j = 0; j < COL; j++) {
            cout << data[i][j] << ":";
        }
        cout << endl;
    }
}

void initializeData(int array[N][COL]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < COL; j++) {
            array[i][j] = 0;
        }
    }
}

int convertToMin (string time) {
    int min = 0;
    string token;
    bool secondTime = false;
    istringstream iss(time);
    while ( getline(iss, token, ':') ) {
        if (!secondTime) {
            min = min + atoi(token.c_str()) * 60;
            secondTime = true;
        } else {
            min = min + atoi(token.c_str());
        }
    }
    return min;
}

void sort(int data[N][COL], int total) {
    int min = data[0][DEPARTURE];
    int temp = 0;
    int temp2 = 0;
    int temp3 = 0;
    int temp4 = 0;
    for (int i = 0; i < total-1; i++) {
        for (int j = i+1; j < total; j++) {
            if (data[i][DEPARTURE] > data[j][DEPARTURE]) {
                temp = data[i][DEPARTURE];
                temp2 = data[i][ARRIVAL];
                temp3 = data[i][PLATFORM];
                temp4 = data[i][USED];
                data[i][DEPARTURE] = data[j][DEPARTURE];
                data[i][ARRIVAL] = data[j][ARRIVAL];
                data[i][PLATFORM] = data[j][PLATFORM];
                data[i][USED] = data[i][USED];
                data[j][DEPARTURE] = temp;
                data[j][ARRIVAL] = temp2;
                data[j][PLATFORM] = temp3;
                data[j][USED] = temp4;
            }
        }
    }
}

void findNumTrain(int data[N][COL], int NA, int NB, int &A, int &B) {
    A = 0;
    B = 0;
    bool need = false;
    int index = 0;
    if (data[0][PLATFORM] == PLATFORMA) {
        A++;
    } else {
        B++;
    }
    for (int i = 1; i < NA + NB; i++) {
        for (int j = 0; j < i; j++) {
            if (data[i][PLATFORM] != data[j][PLATFORM]) {
                if (data[i][DEPARTURE] >= data[j][ARRIVAL] && data[j][USED] == NO) {
                    need = false;
                    data[j][USED] = YES;
                    cout << "false" << endl;
                    break;
                } else
                    need = true;
            } else {
                cout << "true" << endl;
                need = true;
            }
        }
        if (need) {
            if (data[i][PLATFORM] == PLATFORMA) {
                A++;
                cout << "A(" << A <<") at: " << data[i][DEPARTURE] << endl;
            } else {
                B++;
                cout << "B(" << B << ") at: " << data[i][DEPARTURE] << endl;
            }
        } else {
            cout << "No Need at:" << data[i][DEPARTURE] << endl;
        }
    }
}

int main () {
    ifstream myfile ("B-large.in");
    ofstream myoutput ("out.txt");

    int data[N][COL];

    int numOfCase = 0; //N
    int T = 0;
    int NA = 0, NB = 0;
    int caseNum = 1;

    int numOfA = 0;
    int numOfB = 0;

    string getString = " ";

    //cout << "Number of Case: ";
    //Get first line
    getline (myfile, getString);
    numOfCase = atoi(getString.c_str());
    cout << "numOfCase: " << numOfCase << endl;

    while (numOfCase != 0) {
        initializeData(data);

        string temp;
        //cout << "Turnaround Time: ";
        //cin >> T;
        getline (myfile, getString);
        T = atoi(getString.c_str());

        //cout << "NA NB: ";
        //cin >> NA >> NB;
        getline (myfile, getString);
        istringstream iss(getString);
        string token;
        bool secondTime = false;
        while ( getline(iss, token, ' ') ) {
            if (!secondTime) {
                NA = atoi(token.c_str());
                cout << "NA: " << NA << endl;
                secondTime = true;
            } else {
                NB = atoi(token.c_str());
                cout << "NB: " << NB << endl;
            }
        }

        //cout << "Data: " << endl;
        for (int i = 0; i < NA; i++) {
            getline (myfile, getString);
            istringstream iss(getString);
            string token, str1, str2;
            bool secondTime = false;
            while ( getline(iss, token, ' ') ) {
                if (!secondTime) {
                    str1 = token;
                    secondTime = true;
                } else {
                    str2 = token;
                }
            }
            for (int j = 0; j < COL - 2; j++) {
                //cin >> temp;
                if (j == 0) {
                    temp = str1;
                } else {
                    temp = str2;
                }
                data[i][j] = convertToMin(temp);
                if (j == ARRIVAL) {
                    data[i][j] = data[i][j] + T;
                }
            }
            data[i][PLATFORM] = PLATFORMA;
            cout << "Data A: " << data[i][DEPARTURE] << ":" << data[i][ARRIVAL] << ":" << data[i][PLATFORM] << endl;
        }
        for (int i = NA; i < NB+NA; i++) {
            getline (myfile, getString);
            istringstream iss(getString);
            string token, str1, str2;
            bool secondTime = false;
            while ( getline(iss, token, ' ') ) {
                if (!secondTime) {
                    str1 = token;
                    secondTime = true;
                } else {
                    str2 = token;
                }
            }
            for (int j = 0; j < COL - 2; j++) {
                //cin >> temp;
                if (j == 0) {
                    temp = str1;
                } else {
                    temp = str2;
                }
                data[i][j] = convertToMin(temp);
                if (j == ARRIVAL) {
                    data[i][j] = data[i][j] + T;
                }
            }
            data[i][PLATFORM] = PLATFORMB;
            cout << "Data B: " << data[i][DEPARTURE] << ":" << data[i][ARRIVAL] << ":" << data[i][PLATFORM] << endl;
        }

        sort(data, NA + NB);
        findNumTrain(data, NA, NB, numOfA, numOfB);
        printData(data, NA + NB);

        myoutput << "Case #" << caseNum << ": " << numOfA << " " << numOfB << "\n";
        caseNum++;

        numOfCase--;
    }
    myfile.close();
    myoutput.close();
    cout << "Done." << endl;
    getchar();
    return 0;
}
