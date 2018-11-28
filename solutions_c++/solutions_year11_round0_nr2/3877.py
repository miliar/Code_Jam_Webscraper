#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

void solve(const unsigned int nReactions, char** reactions,
        const unsigned int nOppositions, char** oppositions,
        const unsigned int nInvocations, char* invocations,
        unsigned int &nResult, char* &result);

int main(/*int argc, char** argv*/) {
    unsigned int T = 0;

    cin >> T;
    for (unsigned int t = 0; t < T; ++t) {
        unsigned int nReactions;
        char** reactions = NULL;
        unsigned int nOppositions;
        char** oppositions = NULL;
        unsigned int nInvocations;
        char* invocations = NULL;

        //char c;

        cin >> nReactions;
        reactions = new char*[nReactions];
        for (unsigned int i = 0; i < nReactions; ++i) {
            //cin >> c; if (c != ' ') {cerr << "1.c = " << c << endl;exit(-1);}
            reactions[i] = new char[3];
            cin >> reactions[i][0];
            cin >> reactions[i][1];
            cin >> reactions[i][2];
        }

        cin >> nOppositions;
        oppositions = new char*[nOppositions];
        for (unsigned int i = 0; i < nOppositions; ++i) {
            //cin >> c; if (c != ' ') {cerr << "2.c = " << c << endl;exit(-1);}
            oppositions[i] = new char[2];
            cin >> oppositions[i][0];
            cin >> oppositions[i][1];
        }

        cin >> nInvocations;
        invocations = new char[nInvocations];
        //cin >> c; if (c != ' ') {cerr << "3.c = " << c << endl;exit(-1);}
        for (unsigned int i = 0; i < nInvocations; ++i) {
            cin >> invocations[i];
        }

        char* result;
        unsigned int nResult;
        solve(nReactions, reactions, nOppositions, oppositions, nInvocations, invocations, nResult, result);
        cout << "Case #" << (t + 1) << ": [";
        for (unsigned int i = 0; i < nResult; ++i) {
            if (i < nResult - 1) cout << result[i] << ", ";
            else cout << result[i];
        }
        cout << "]" << endl;

        delete[] result;
        delete[] invocations;
        for (unsigned int i = 0; i < nOppositions; ++i) delete[] oppositions[i];
        delete[] oppositions;
        for (unsigned int i = 0; i < nReactions; ++i) delete[] reactions[i];
        delete[] reactions;
    }
    return 0;
}

unsigned int getIndex(const char c) {
    switch (c) {
        case 'Q':return 0;
        case 'W':return 1;
        case 'E':return 2;
        case 'R':return 3;
        case 'A':return 4;
        case 'S':return 5;
        case 'D':return 6;
        case 'F':return 7;
    }
    return 8;
}

void solve(const unsigned int nReactions, char** reactions,
        const unsigned int nOppositions, char** oppositions,
        const unsigned int nInvocations, char* invocations,
        unsigned int &nResult, char* &result) {

    //cerr << "Reactions: " << endl;
    //for (unsigned int i = 0; i < nReactions; ++i) cerr << reactions[i][0] << reactions[i][1] << reactions[i][2] << endl;
    //cerr << "Oppositions: " << endl;
    //for (unsigned int i = 0; i < nOppositions; ++i) cerr << oppositions[i][0] << oppositions[i][1] << endl;
    //cerr << "Invocations: " << endl;
    //for (unsigned int i = 0; i < nInvocations; ++i) cerr << invocations[i];
    //cerr << endl;



    const unsigned int nBases = 8;
    char** react = new char*[nBases];
    for (unsigned int i = 0; i < nBases; ++i) {
        react[i] = new char[nBases];
        for (unsigned int j = 0; j < nBases; ++j) react[i][j] = '0';
    }
    for (unsigned int i = 0; i < nReactions; ++i) {
        react[getIndex(reactions[i][0])][getIndex(reactions[i][1])] = reactions[i][2];
        react[getIndex(reactions[i][1])][getIndex(reactions[i][0])] = reactions[i][2];
    }

    int* opp = new int[nBases];
    for (unsigned int i = 0; i < nBases; ++i) opp[i] = -1;
    for (unsigned int i = 0; i < nOppositions; ++i) {
        opp[getIndex(oppositions[i][0])] = getIndex(oppositions[i][1]);
        opp[getIndex(oppositions[i][1])] = getIndex(oppositions[i][0]);
    }

    result = new char[nInvocations];
    nResult = 0;

    for (unsigned int i = 0; i < nInvocations; ++i) {
        if (nResult == 0 || getIndex(invocations[i]) == nBases) result[nResult++] = invocations[i];
        else {
            if (getIndex(result[nResult - 1]) < nBases && react[getIndex(invocations[i])][getIndex(result[nResult - 1])] != '0') result[nResult - 1] = react[getIndex(invocations[i])][getIndex(result[nResult - 1])];
            else {
                int idx = opp[getIndex(invocations[i])];
                if (idx != -1) {
                    bool set = false;
                    for (unsigned int j = 0; j < nResult; ++j) {
                        if (getIndex(result[j]) == (unsigned int) idx) {
                            nResult = 0;
                            set = true;
                            break;
                        }
                    }
                    if (!set) result[nResult++] = invocations[i];
                } else {
                    result[nResult++] = invocations[i];
                }
            }
        }
    }

    delete[] opp;
    for (unsigned int i = 0; i < nBases; ++i) delete[] react[i];
    delete[] react;
}