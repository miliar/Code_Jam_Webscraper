#include<iostream>
#include<string>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

int main() {
    FILE* f = fopen("PA.txt", "w");
    int n;
    int i, j, count = 1;
    string s;
    char s_G[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
                    'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
    cin >> n;
    getline(cin, s);
    while(n--) {
        getline(cin, s);
        for(i = 0;i < s.size();i++) {
            if(s[i] == ' ') continue;
            else s[i] = s_G[s[i] - 'a'];
        }
        cout << "Case #" << count << ": " << s << endl;
        fprintf(f, "Case #%d: ", count++);
        for(j = 0;j < s.size();j++) {
            fprintf(f, "%c", s[j]);
        }
        fprintf(f, "\n");
    }
    //system("pause");
}
