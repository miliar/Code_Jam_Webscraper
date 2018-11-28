#include <iostream>
#include <string>
#include <map>
#include <sstream>

using namespace std;

bool isRecycled(const string& str1, const string& str2) {
    string concat = str1 + str1;
    return concat.find(str2) != string::npos;
}

int main(void) {
    int numLines = 0;
    cin >> numLines;

    int num = 1;

    while (true) {
        int num1 = 0, num2 = 0;
        cin >> num1 >> num2;

        if (cin.fail())
            break;

        //cout << num1 << " "  << num2 << " ";

        int count = 0;

        for (int i = num1; i <= num2; i++) {
            for (int j = i + 1; j <= num2; j++) {
                stringstream str1, str2;
                str1 << i;
                str2 << j;

                const string one = str1.str();
                const string two = str2.str();
                if (isRecycled(one, two)) {
                    count++;
                } else if (isRecycled(two, one)) {
                    count++;
                }
            }
        }

        cout << "Case #" << num << ": " << count << endl;
        num++;
    }
}
