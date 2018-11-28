#include <fstream>
#include <iostream>
#include <cstring>

using namespace std;

int a[26];

int main()
{
    char line1[128], line2[128];
    ifstream f("a.in");
    for(int i = 0; i < 3; ++i){
        f.getline(line1, 128);
        f.getline(line2, 128);
        for(int j = 0; j < strlen(line1); ++j){
            if(line1[j] == ' ') continue;
            a[line1[j]-'a'] = line2[j] - 'a';
        }
    }
    a['z'-'a'] = 'q' - 'a';
    a['q' - 'a'] = 'z'-'a';
    f.close();

    ifstream f2("b.in");
    ofstream f3("b.out");
    int T, t = 0;
    f2 >> T; f2.get();
    while(t++ < T){
        f2.getline(line1, 128);
        f3 << "Case #" << t << ": ";
        for(int j = 0; j < strlen(line1); ++j){
            if(line1[j] == ' ') f3 << ' ';
            else f3 << (char)(a[line1[j]-'a'] + 'a');
        }
        f3 << endl;
    }
    f3.close();
    f2.close();
    return 0;
}
