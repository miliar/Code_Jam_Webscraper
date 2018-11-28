#include<iostream>
#include<sstream>
#include<string>

using namespace std;

int main() {
    int n;
    cin >> n;
    string output = "";
    for (int caseNum = 1; caseNum <= n; ++caseNum) {
        int numInts;
        cin >> numInts;
        unsigned int sum = 0, xorSum = 0;
        unsigned int min = 0-1; // max int
        for (int i = 0; i < numInts; ++i) {
            int next;
            cin >> next;
            if (next < min)
                min = next;
            sum += next;
            xorSum = xorSum xor next;
        }

        // Output
        string thisCase = "Case #";
        stringstream convert;
        convert << caseNum;
        thisCase += convert.str();
        thisCase += ": ";
        if (xorSum != 0)
            thisCase += "NO\n";
        else {
            stringstream cvert;
            cvert.flush();
            cvert << (sum - min);
            thisCase += cvert.str();
            thisCase += "\n";
        }
        output += thisCase;
    }
    cout << output;

    return 1;
}


