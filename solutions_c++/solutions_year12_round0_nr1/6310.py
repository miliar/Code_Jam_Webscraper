#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {

    string problem1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    string problem2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    string problem3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

    string solve1 = "our language is impossible to understand";
    string solve2 = "there are twenty six factorial possibilities";
    string solve3 = "so it is okay if you want to just give up";

    map <char, char> M;
    M['a'] = 'y';
    M['o'] = 'e';
    M['z'] = 'q';
    M['q'] = 'z';
    M[' '] = ' ';
    for(int i=0;i<(int)solve1.length();i++) {
        if(solve1[i] != ' ') {
            M[problem1[i]] = solve1[i];
        }
    }
    for(int i=0;i<(int)solve2.length();i++) {
        if(solve2[i] != ' ') {
            M[problem2[i]] = solve2[i];
        }
    }
    for(int i=0;i<(int)solve3.length();i++) {
        if(solve3[i] != ' ') {
            M[problem3[i]] = solve3[i];
        }
    }

    /*for(int i='a';i<='z';i++) {
        cout<<(char)i<<" -> "<<M[(char)i]<<endl;
    }*/

    // Input:
    int T;
    cin>>T;
    cin.get();
    for(int i=0;i<T;i++) {
        string problem;
        char solve[200] = {'\0'};
        getline(cin, problem, '\n');
        for(int j=0;j<(int)problem.length();j++) {
            solve[j] = M[problem[j]];
        }
        cout<<"Case #"<<(i+1)<<": "<<solve<<endl;
    }



    return 0;
}
