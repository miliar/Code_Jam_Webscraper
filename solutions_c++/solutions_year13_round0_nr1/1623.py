#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        char s[9][9];
        for(int i=0;i<4;i++)
            scanf("%s",s[i]);
        int k, u = 2;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(s[i][j] == '.')
                    u = 3;
        k=1;
        for(int i=0;i<4;i++)
            if(s[i][i] == '.' || s[i][i] == 'O') k=0;
        if(k) u = 0;
        k=1;
        for(int i=0;i<4;i++)
            if(s[i][3-i] == '.' || s[i][3-i] == 'O') k=0;
        if(k) u = 0;
        for(int i=0;i<4;i++){
            k=1;
            for(int j=0;j<4 && k;j++)
                if(s[i][j] == '.' || s[i][j] == 'O') k=0;
            if(k) u = 0;
            k=1;
            for(int j=0;j<4 && k;j++)
                if(s[j][i] == '.' || s[j][i] == 'O') k=0;
            if(k) u = 0;
        }
        
        k=1;
        for(int i=0;i<4;i++)
            if(s[i][i] == '.' || s[i][i] == 'X') k=0;
        if(k) u = 1;
        k=1;
        for(int i=0;i<4;i++)
            if(s[i][3-i] == '.' || s[i][3-i] == 'X') k=0;
        if(k) u = 1;
        for(int i=0;i<4;i++){
            k=1;
            for(int j=0;j<4 && k;j++)
                if(s[i][j] == '.' || s[i][j] == 'X') k=0;
            if(k) u = 1;
            k=1;
            for(int j=0;j<4 && k;j++)
                if(s[j][i] == '.' || s[j][i] == 'X') k=0;
            if(k) u = 1;
        }
        
        
        printf("Case #%d: %s\n", tt, u==0?"X won":(u==1?"O won":(u==2?"Draw":"Game has not completed")));
    }
    return 0;
}

