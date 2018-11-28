#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>

using namespace std;

int main(int argc, char **argv) {
    int L, D, N;
    scanf("%d %d %d", &L, &D, &N);
    char *st = new char[L];
    FILE *p = fopen("/home/praveen/Desktop/wordlist.txt", "w");
    for (int i = 0; i < D; ++i) {
        scanf("%s", st);
        fprintf(p, "%s\n", st);
    }
    fclose(p);    
    fflush(stdout);
    string k, cmdarg;
    for (int i = 0; i < N; ++i) {
        printf("Case #%d: ", i+1);
        cin >> k;
        for (string::iterator itr = k.begin(); itr != k.end(); ++itr) {
            if(*itr == '(') {
                *itr = '[';
            }else if(*itr == ')') {
                *itr = ']';
            }
        }        
        cmdarg = "grep -c "+k+" /home/praveen/Desktop/wordlist.txt";        
        system(cmdarg.c_str());
    }
    free(st);
    return 0;
}
