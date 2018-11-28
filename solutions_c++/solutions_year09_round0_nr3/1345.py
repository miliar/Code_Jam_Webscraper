#include <iostream>
#include <string>

using std::string;
using std::cin;
using std::cout;
using std::endl;

int main() {
    string test_string = "welcome to code jam";

    int case_num;
    char tmp;
    int count[500];

    cin >> std::skipws >> case_num;
    cin.getline(&tmp, 1);

    for (int c = 1; c <= case_num; c++) {

        string data_in;
        std::getline(cin, data_in);

        for (int i = 0; i < data_in.size(); i++) count[i] = 0;

        for (int d = 0; d < data_in.size(); d++)
            if (data_in[d] == test_string[0]) count[d] = 1;

        for (int t = 1; t < test_string.size(); t++) {
            int sum = 0;
            for (int d = 0; d < data_in.size(); d++) {
                if (data_in[d] == test_string[t-1]) sum = (sum + count[d]) % 10000;
                else if (data_in[d] == test_string[t]) count[d] = sum;
            }
        }

        int output = 0;
        for (int i = 0; i < data_in.size(); i++)
        {
            if (data_in[i] == test_string[test_string.size() - 1]) output = (output + count[i]) % 10000;
        }

        cout << "Case #" << c << ": ";
        cout.fill('0');
        cout.width(4);
        cout << output % 10000 << endl;
    }

    return 0;
}
