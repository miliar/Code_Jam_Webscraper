#include <iostream>
#include <vector>

using namespace std;
typedef vector<char> vectorChar;

int main () {
    char* ref = "yhesocvxduiglbkrztnwjpfmaq";
    char G[30][101];
    unsigned short int T, i, j;
    
    cin >> T;
    getchar();
    for(i=0; i<T; i++) {
        gets(G[i]);
    }
    
    for(i=0; i<T; i++) {
             printf("Case #%d: ", i+1);
             for(j=0; j<strlen(G[i]); j++) {
                      if(G[i][j] != 32)
                        printf("%c", ref[G[i][j] - 97]);
                      else
                        printf("%c", G[i][j]);
             }
             if(i!=T-1)
                cout << endl;
    }
    return 0;
}
