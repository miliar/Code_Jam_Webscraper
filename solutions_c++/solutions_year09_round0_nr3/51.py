#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

int main(void)
{
    string line;
    getline(cin, line);
    int N;
    istringstream(line) >> N;
    const string message = "welcome to code jam";
    const int mesLen = message.length();
    for (int caseNo = 1; caseNo <= N; caseNo++) {
        int counter = 0;
        getline(cin, line);
        const int lineLen = line.length();
        vector<vector<int> > memo(lineLen,vector<int>(mesLen,0));
        for (int i = 0; i < lineLen; i++)
            if (line[i] == message[0])
                memo[i][0] = 1;
        for (int i = 0; i < lineLen; i++) {
            for (int j = mesLen-1; j > 0; j--) {
                if (line[i] != message[j]) continue;
                for (int k = 0; k < i; k++)
                    memo[i][j] += memo[k][j-1];
                memo[i][j] %= 10000;
            }
        }
        for (int i = 0; i < lineLen; i++) {
            counter += memo[i][mesLen-1];
            counter %= 10000;
        }
        printf("Case #%d: %04d\n", caseNo, counter);
    }

    return 0;
}

