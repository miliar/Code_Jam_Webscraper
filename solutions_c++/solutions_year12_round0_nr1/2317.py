#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <math.h>
#include <windows.h>
using namespace std;
typedef long long s64;
typedef unsigned long long u64;
typedef long s32;
typedef unsigned long long u32;



int main(int argc, char* argv[])
{
    HANDLE handle = GetStdHandle(STD_INPUT_HANDLE);
    DWORD mode;
    GetConsoleMode(handle, &mode);
    mode &= ~ENABLE_ECHO_INPUT;
    SetConsoleMode(handle, mode);


    const char alpha[] = "abcdefghijklmnopqrstuvwxyz";

    const char in0[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    const char in1[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    const char in2[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    const char in3[] = "qz";

    const char out0[] = "our language is impossible to understand";
    const char out1[] = "there are twenty six factorial possibilities";
    const char out2[] = "so it is okay if you want to just give up";
    const char out3[] = "zq";


    

    map<char, char> translate;

    for (int i=0; i < strlen(in0); ++i) {
        translate[in0[i]] = out0[i];
    }
    for (int i=0; i < strlen(in1); ++i) {
        translate[in1[i]] = out1[i];
    }
    for (int i=0; i < strlen(in2); ++i) {
        translate[in2[i]] = out2[i];
    }
    for (int i=0; i < strlen(in3); ++i) {
        translate[in3[i]] = out3[i];
    }




	string line;
	int T;
	cin >> T;
	getline(cin, line);

	for (int t=0; t < T; t++) {

        cout << "Case #" << (t+1) << ": ";


        string out;
        getline(cin, line);
        stringstream ss(line);

        for (int i=0; i < line.length(); ++i) {
            out += translate[line[i]];
        }

        cout << out << endl;
    }

    return 0;
}


