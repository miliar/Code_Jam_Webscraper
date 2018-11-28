#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
    freopen ("A-small-attempt2.in","r",stdin);
    freopen ("A-small-attempt2.out","w",stdout);
    int T, i, j;
    cin >> T;
    string G;
    char c;
    getline (cin,G);
    for(i=0;i<T;i++){
        getline (cin,G);
        for(j=0;j<G.size();j++){
            c = G[j];
            switch(c){
                case 'y':
                    G[j]='a';
                    break;
                case 'n':
                    G[j]='b';
                    break;
                case 'f':
                    G[j]='c';
                    break;
                case 'i':
                    G[j]='d';
                    break;
                case 'c':
                    G[j]='e';
                    break;
                case 'w':
                    G[j]='f';
                    break;
                case 'l':
                    G[j]='g';
                    break;
                case 'b':
                    G[j]='h';
                    break;
                case 'k':
                    G[j]='i';
                    break;
                case 'u':
                    G[j]='j';
                    break;
                case 'o':
                    G[j]='k';
                    break;
                case 'm':
                    G[j]='l';
                    break;
                case 'x':
                    G[j]='m';
                    break;
                case 's':
                    G[j]='n';
                    break;
                case 'e':
                    G[j]='o';
                    break;
                case 'v':
                    G[j]='p';
                    break;
                case 'z':
                    G[j]='q';
                    break;
                case 'p':
                    G[j]='r';
                    break;
                case 'd':
                    G[j]='s';
                    break;
                case 'r':
                    G[j]='t';
                    break;
                case 'j':
                    G[j]='u';
                    break;
                case 'g':
                    G[j]='v';
                    break;
                case 't':
                    G[j]='w';
                    break;
                case 'h':
                    G[j]='x';
                    break;
                case 'a':
                    G[j]='y';
                    break;
                case 'q':
                    G[j]='z';
                    break;
                default:
                    break;
            }
        }
        cout << "Case #" << (i+1) << ": " << G << endl;
    }
    return 0;
}
