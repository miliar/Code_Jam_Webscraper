#include <cstdio>
#include <cstring>

using namespace std;

int T, C=1;
char M[8][8];

inline bool X(char c) {
    return (c=='X' or c=='T');
}

inline bool O(char c) {
    return (c=='O' or c=='T');
}


int main() {

    for(scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);
        bool tp=false;
        for (int i=0;i<4;i++) {
            scanf("%s",M[i]);
            for (int j=0;j<4;j++)
                if (M[i][j]=='.') tp=true;
        }
        int ganha=-1;
        for (int i=0;i<4;i++) for (int j=0;j<4;j++) {
            if (j+3<4 and X(M[i][j]) and X(M[i][j+1]) and X(M[i][j+2]) and X(M[i][j+3]))
                ganha=0;
            if (j+3<4 and O(M[i][j]) and O(M[i][j+1]) and O(M[i][j+2]) and O(M[i][j+3]))
                ganha=1;
            if (i+3<4 and X(M[i][j]) and X(M[i+1][j]) and X(M[i+2][j]) and X(M[i+3][j]))
                ganha=0;
            if (i+3<4 and O(M[i][j]) and O(M[i+1][j]) and O(M[i+2][j]) and O(M[i+3][j]))
                ganha=1;
            if (i+3<4 and j+3<4 and X(M[i][j]) and X(M[i+1][j+1]) and X(M[i+2][j+2]) and X(M[i+3][j+3]))
                ganha=0;
            if (i+3<4 and j+3<4 and O(M[i][j]) and O(M[i+1][j+1]) and O(M[i+2][j+2]) and O(M[i+3][j+3]))
                ganha=1;
            if (i+3<4 and j-3<4 and X(M[i][j]) and X(M[i+1][j-1]) and X(M[i+2][j-2]) and X(M[i+3][j-3]))
                ganha=0;
            if (i+3<4 and j-3<4 and O(M[i][j]) and O(M[i+1][j-1]) and O(M[i+2][j-2]) and O(M[i+3][j-3]))
                ganha=1;
        }
        if (ganha!=-1) {
            printf("%c won\n",ganha==0?'X':'O');
            continue;
        }
        printf("%s\n",tp?"Game has not completed":"Draw");
    }

    return 0;
}
