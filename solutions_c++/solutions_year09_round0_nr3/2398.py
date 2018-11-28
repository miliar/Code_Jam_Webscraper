#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
using namespace std;

// welcome to code jam
// 0123456789abcdefghi
#define LEN 19

int solve(string str)
{
    unsigned int subcount[LEN];
    memset(subcount, 0, LEN * sizeof(unsigned int));

    string::iterator it;
    for (it = str.begin(); it < str.end(); ++it) {
        switch (*it) {
            case 'w': subcount[0]++;
                      break;
            case 'e': subcount[1] += subcount[0];
                      subcount[6] += subcount[5];
                      subcount[14] += subcount[13];
                      break;
            case 'l': subcount[2] += subcount[1];
                      break;
            case 'c': subcount[3] += subcount[2];
                      subcount[11] += subcount[10];
                      break;
            case 'o': subcount[4] += subcount[3];
                      subcount[9] += subcount[8];
                      subcount[12] += subcount[11];
                      break;
            case 'm': subcount[5] += subcount[4];
                      subcount[18] += subcount[17];
                      break;
            case ' ': subcount[7] += subcount[6];
                      subcount[10] += subcount[9];
                      subcount[15] += subcount[14];
                      break;
            case 't': subcount[8] += subcount[7];
                      break;
            case 'd': subcount[13] += subcount[12];
                      break;
            case 'j': subcount[16] += subcount[15];
                      break;
            case 'a': subcount[17] += subcount[16];
                      break;
            default:  break;
        }
    }

    return subcount[LEN - 1] % 10000;
}

int main(int argc, char **argv)
{
    ifstream fin(argv[1]);

    int N;
    fin >> N;
    fin.get();

    for (int i = 0; i < N; ++i) {
        // display the progress
        cerr << "Processing " << i << " of " << N << endl;

        string str;
        getline(fin, str);
        cout << "Case #"
             << i + 1
             << ": "
             << setfill('0')
             << setw(4)
             << solve(str)
             << endl;
    }

    fin.close();

    return 0;
}
