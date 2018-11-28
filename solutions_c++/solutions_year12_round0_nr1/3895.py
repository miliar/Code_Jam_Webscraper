#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <ctime>


//#define DEBUG

using namespace std;

int main(){
	#ifndef DEBUG
		freopen("A-small-attempt0.in", "r", stdin);
		freopen("A-small.out", "w", stdout);
	#endif
    char* alphabet = "yhesocvxduiglbkrztnwjpfmaq";	
    char* oldalpha = "abcdefghijklmnopqrstuvwxyz";
    int T, C, numItems;
    cin >> T;
    cin.ignore();
    for (int test = 0; test < T; test++) {
        string line;
        string output;
        getline(cin, line);

        for (int i = 0; i < line.length(); i++) {
            //cout << line[i] << alphabet[(int)(line[i] - 97)];
            if(line[i] != ' ')
                output.push_back(alphabet[line[i] - 97]);
            else
                output.push_back(' ');
        }
        cout << "Case #" << test+1 << ": " << output << endl;//Output Answer:
    }

	#ifdef DEBUG
		system("pause");
	#endif
	
	return 0;
}
