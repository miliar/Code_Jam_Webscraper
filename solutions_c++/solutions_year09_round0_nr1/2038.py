#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib>

using namespace std;

int main()
{
    int L, D, N;
    cin >> L >> D >> N;
    string *pWord = new string[D];

    // Input letters
    for (int i = 0; i < D; i++)
    {
        cin >> pWord[i];
    }
    // Cases
    for (int i = 0; i < N; i++)
    {
        string buffer;
        cin >> buffer;
        int length = strlen(buffer.c_str());
        int count = 0;
        int *pSegCount = new int[L];
        string *pSeg = new string[L];
        int curLetter = 0;
        int tmpLetter = 0;

        for (int j = 0; j < L; j++)
        {
            pSegCount[j] = 0;
            pSeg[j] = "";
        }
        // Segment handling
        for (int j = 0; j < length; j++)
        {
            if (buffer.c_str()[j] == '(') {
                j++;
                while (buffer.c_str()[j] != ')' )
                {
                    pSegCount[curLetter]++;
                    pSeg[curLetter]+= buffer[j];
                    tmpLetter++;
                    j++;
                }
                curLetter++;
                tmpLetter = 0;
            } else {
                pSeg[curLetter] = buffer[j];
                pSegCount[curLetter] = 1;
                curLetter++;
            }
        }

        for (int j = 0; j < D; j++)
        {
            int matchCount = 0;
            try {
                for (int k = 0; k < L; k++)
                {
                    for (int m = 0; m < pSegCount[k]; m++)
                    {
                        if (pWord[j][k] == pSeg[k][m]) {
                            matchCount++;
                            break;
                        }
                    }
                    if (matchCount != k + 1) {
                        throw -1;
                    }
                }
                if (matchCount == L) {
                    count++;
                }
            }
            catch (int) {}
        }
        cout << "Case #" << i+1 << ": " << count << endl;
    }

    return 0;

}
