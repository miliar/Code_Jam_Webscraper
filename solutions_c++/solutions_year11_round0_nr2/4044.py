#include <iostream>

using namespace std;

class TestCase
{
    public:
        virtual ~TestCase();

        char getCombChar(char c1, char c2);
        char getOppChar(char c);

        int numOfCombPairs_;
        char** combPairs_;
        int numOfOppPairs_;
        char** oppPairs_;
        int numOfCharsToInv_;
        char* charsToInvoke_;
};

TestCase::~TestCase()
{
    for (int i = 0; i < numOfCombPairs_; i++) {
        delete[] combPairs_[i];
    }

    delete[] combPairs_;

    for (int i = 0; i < numOfOppPairs_; i++) {
        delete[] oppPairs_[i];
    }

    delete[] oppPairs_;
    delete[] charsToInvoke_;
}

char TestCase::getCombChar(char c1, char c2)
{
    for (int i = 0; i < numOfCombPairs_; i++) {
        if ((combPairs_[i][0] == c1 && combPairs_[i][1] == c2) || (combPairs_[i][0] == c2 && combPairs_[i][1] == c1)) {
            return combPairs_[i][2];
        }
    }

    return '\0';
}

char TestCase::getOppChar(char c)
{
    for (int i = 0; i < numOfOppPairs_; i++) {
        if (oppPairs_[i][0] == c) {
            return oppPairs_[i][1];
        } else if (oppPairs_[i][1] == c) {
            return oppPairs_[i][0];
        }
    }

    return '\0';
}

bool strHasChar(const char* str, char c)
{
    int i = 0;

    while (str[i] != '\0') {
        if (str[i] == c) {
            return true;
        }

        i++;
    }

    return false;
}

int main()
{
    int numOfTestCases = 0;

    cin >> numOfTestCases;

    TestCase* testCases = new TestCase[numOfTestCases];

    for (int i = 0; i < numOfTestCases; i++) {
        int numOfCombPairs = 0;

        cin >> numOfCombPairs;

        testCases[i].numOfCombPairs_ = numOfCombPairs;
        testCases[i].combPairs_ = new char*[numOfCombPairs];

        for (int j = 0; j < numOfCombPairs; j++) {
            testCases[i].combPairs_[j] = new char[5];
            cin >> testCases[i].combPairs_[j];
        }

        int numOfOppPairs = 0;

        cin >> numOfOppPairs;

        testCases[i].numOfOppPairs_ = numOfOppPairs;
        testCases[i].oppPairs_ = new char*[numOfOppPairs];

        for (int j = 0; j < numOfOppPairs; j++) {
            testCases[i].oppPairs_[j] = new char[4];
            cin >> testCases[i].oppPairs_[j];
        }

        int numOfCharsToInv = 0;

        cin >> numOfCharsToInv;

        testCases[i].numOfCharsToInv_ = numOfCharsToInv;
        testCases[i].charsToInvoke_ = new char[numOfCharsToInv + 2];

        cin >> testCases[i].charsToInvoke_;
    }

    for (int i = 0; i < numOfTestCases; i++) {
        TestCase* testCase = &testCases[i];
        int numOfCharsToInv = testCase->numOfCharsToInv_;
        char* result = new char[numOfCharsToInv];

        result[0] = testCase->charsToInvoke_[0];
        result[1] = '\0';

        int endPtr = 1;

        for (int j = 1; j < numOfCharsToInv; j++) {
            char currCharToInvoke = testCase->charsToInvoke_[j];

            if (endPtr > 0) {
                char combChar = testCase->getCombChar(result[endPtr - 1], currCharToInvoke);

                if (combChar != '\0') {
                    result[endPtr - 1] = combChar;
                } else {
                    char oppChar = testCase->getOppChar(currCharToInvoke);
                    bool resHasOppChar = false;

                    if (oppChar != '\0') {
                        resHasOppChar = strHasChar(result, oppChar);
                    }

                    if (resHasOppChar) {
                        result[0] = '\0';
                        endPtr = 0;
                    } else {
                        result[endPtr] = currCharToInvoke;
                        result[endPtr + 1] = '\0';
                        endPtr++;
                    }
                }
            } else {
                result[0] = currCharToInvoke;
                result[1] = '\0';
                endPtr = 1;
            }
        }

        cout << "Case #" << i + 1 << ": [";

        for (int j = 0; j < endPtr - 1; j++) {
            cout << result[j] << ", ";
        }

        if (endPtr - 1 >= 0) {
            cout << result[endPtr - 1];
        }

        cout << "]" << endl;

        delete[] result;
    }

    delete[] testCases;

    return 0;
}
