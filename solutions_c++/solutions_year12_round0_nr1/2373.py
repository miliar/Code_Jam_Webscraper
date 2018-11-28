#include <map>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

map<char, char> learn() {
    map<char, char> m;
    string input = "zqejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
	string output = "qzour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
    for (unsigned i = 0; i < input.size(); i++) {
        m[input[i]] = output[i];
    }
    return m;
}

int main() {
    map<char, char> m = learn();
    char input[256];
    int t;
    cin >> t;
    cin.getline(input, 256);
	for (int ti = 1; ti <= t; ti++) {
        cin.getline(input, 256);
	 
        
        int len = strlen(input);
        for (int i = 0; i < len; i++) {
            input[i] = m[input[i]];
        }
	 
        cout << "Case #" << ti << ": " << input << endl;
    }
    return 0;
}
