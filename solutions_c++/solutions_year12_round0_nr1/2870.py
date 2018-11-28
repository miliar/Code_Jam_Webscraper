#include<iostream>
#include<string>
using namespace std;
char exchange (char x) {
    char c;
    switch(x) {
        case 'a':
            return 'y';
        case 'b':
            return 'h';
        case 'c':
            return 'e';
        case 'd':
            return 's';
        case 'e':
            return 'o';
        case 'f':
            return 'c';
        case 'g':
            return 'v';
        case 'h':
            return 'x';
        case 'i':
            return 'd';
        case 'j':
            return 'u';
        case 'k':
            return 'i';
        case 'l':
            return 'g';
        case 'm':
            return 'l';
        case 'n':
            return 'b';
        case 'o':
            return 'k';
        case 'p':
            return 'r';
        case 'q':
            return 'z';
        case 'r':
            return 't';
        case 's':
            return 'n';
        case 't':
            return 'w';
        case 'u':
            return 'j';
        case 'v':
            return 'p';
        case 'w':
            return 'f';
        case 'x':
            return 'm';
        case 'y':
            return 'a';
        case 'z':      
            return 'q';
        default :
            return x;
    }    
}    
int main() {
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int T;
    scanf("%d\n",&T);
    char G[30][110], S[30][110];
    for (int i = 0; i <30; ++ i)
    for (int j = 0; j < 110; ++ j)
        G[i][j] = S[i][j] = '\0';
        
    for (int i = 0; i < T; ++i) {
        fgets(G[i],110,stdin);
        //if (G[i][strlen(G[i])-1] == '\n')
          // G[i][strlen(G[i])-1] = '\0';     
    }
    
    for (int i = 0; i < T; ++ i) {
        for (int j = 0; j < strlen(G[i]); ++ j) {
            S[i][j] = exchange(G[i][j]);
        }
        printf("Case #%d: %s",i+1,S[i]);
    }
    return 0;
}    
        
                      
