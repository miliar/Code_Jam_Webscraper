#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#define max_n 9999999
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
#define pi acos(-1)

using namespace std;

typedef long long ll;
typedef vector <int > vi;
typedef pair<int,int> pii;
typedef vector <pii> vii;


int main(){
    int T,diag_x[3],diag_y[3],diag_t[3],col_x[5],col_y[5],col_t[5],row_x[5],row_y[5],row_t[5];
    bool x_win,y_win,dot_win;
    char temp[10];
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        x_win=y_win=dot_win=false;
        memset(diag_x,0,sizeof(diag_x));
        memset(diag_y,0,sizeof(diag_y));
        memset(diag_t,0,sizeof(diag_t));
        memset(row_x,0,sizeof(row_x));
        memset(row_y,0,sizeof(row_y));
        memset(row_t,0,sizeof(row_t));
        memset(col_x,0,sizeof(col_x));
        memset(col_y,0,sizeof(col_y));
        memset(col_t,0,sizeof(col_t));
        
        for(int i=0;i<4;i++){
            scanf("%s",temp);
            for(int j=0;j<4;j++){
                if(temp[j]=='.')dot_win=true;
                
                if(i==j){
                    if(temp[j]=='X')diag_x[0]++;
                    else if(temp[j]=='O')diag_y[0]++;
                    else if(temp[j]=='T')diag_t[0]++;
                }
                if(i+j==3){
                    if(temp[j]=='X')diag_x[1]++;
                    else if(temp[j]=='O')diag_y[1]++;
                    else if(temp[j]=='T')diag_t[1]++;
                }
                
                if(temp[j]=='X'){row_x[i]++;col_x[j]++;}
                else if(temp[j]=='O'){row_y[i]++;col_y[j]++;}
                else if(temp[j]=='T'){row_t[i]++;col_t[j]++;}
            }
        }
        for(int i=0;i<2&&!x_win&&!y_win;i++){
            if(diag_x[i]==4||(diag_t[i]==1&&diag_x[i]==3))x_win = true;
            if(diag_y[i]==4||(diag_t[i]==1&&diag_y[i]==3))y_win = true;
        }
        for(int i=0;i<4&&!x_win&&!y_win;i++){
            if(row_x[i]==4||(row_t[i]==1&&row_x[i]==3))x_win = true;
            if(row_y[i]==4||(row_t[i]==1&&row_y[i]==3))y_win = true;
            if(col_x[i]==4||(col_t[i]==1&&col_x[i]==3))x_win = true;
            if(col_y[i]==4||(col_t[i]==1&&col_y[i]==3))y_win = true;
            
        }
        printf("Case #%d: ",t);
        if(x_win)puts("X won");
        else if(y_win)puts("O won");
        else if(dot_win)puts("Game has not completed");
        else puts("Draw");
    }
    return 0;
}
