#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<string>
#include<iterator>
#include<string>
#include<sstream>
#include<cassert>
#include<ctime>
#include<cmath>

#define MP make_pair
#define PB push_back
#define X first
#define Y second
#define oo 2000000000
#define MOD 1000000007
#define LL long long int
#define PII pair<int,int>
#define DEBUG 0

using namespace std;
char str[10][10];
int T;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for(int I=1;I<=T;I++){
        int dots = 0;
        for(int i=0;i<4;i++){
            scanf("%s",str[i]);
            for(int j=0;j<4;j++){
                dots += (str[i][j] == '.');
            }
        }
        int winner = -1;
        for(int i=0;i<4;i++){
            int x,o,t;
            x = o = t = 0;
            for(int j=0;j<4;j++) x += (str[i][j] == 'X') , o += (str[i][j] == 'O') , t += (str[i][j] == 'T');
            if((x == 4) || (x == 3 && t == 1)){
                winner = 0;break;
            }
            else if((o == 4) || (o == 3 && t == 1)){
                winner = 1;break;
            }
        }
        for(int i=0;i<4;i++){
            int x,o,t;
            x = o = t = 0;
            for(int j=0;j<4;j++) x += (str[j][i] == 'X') , o += (str[j][i] == 'O') , t += (str[j][i] == 'T');
            if((x == 4) || (x == 3 && t == 1)){
                winner = 0;break;
            }
            else if((o == 4) || (o == 3 && t == 1)){
                winner = 1;break;
            }
        }
        int x,o,t ;
        x = o = t = 0;
        for(int i=0;i<4;i++){
            x += (str[i][i] == 'X') , o += (str[i][i] == 'O') , t += (str[i][i] == 'T');
        }
        if((x == 4) || (x == 3 && t == 1)){
            winner = 0;
        }
        else if((o == 4) || (o == 3 && t == 1)){
            winner = 1;
        }
        x = o = t = 0;
        for(int i=3;i >= 0;i--){
            x += (str[i][3-i] == 'X') , o += (str[i][3-i] == 'O') , t += (str[i][3-i] == 'T');
        }
        if((x == 4) || (x == 3 && t == 1)){
            winner = 0;
        }
        else if((o == 4) || (o == 3 && t == 1)){
            winner = 1;
        }
        printf("Case #%d: ",I);
        if(winner == 0) printf("X won\n");
        else if(winner == 1) printf("O won\n");
        else if(dots == 0) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
