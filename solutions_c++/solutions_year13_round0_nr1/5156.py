#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
using namespace std;
#define SZ(v) ((int)(v).size())
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPF(i, a, b) for (int i = (a); i <= (b); ++i)
#define REPD(i, a, b) for (int i = (a); i >= (b); --i)
const int maxint = -1u>>1;
char x[5][5];
int t;

int main() {
        freopen("a.in", "r", stdin);
        freopen("a.out", "w", stdout);
        
        scanf("%d", &t);
        for (int cas = 1; cas <= t; cas ++) {
                scanf("%c", &x[0][0]);
                for (int i = 1; i <= 4; i ++) {
                        for (int j = 1; j <= 4; j ++) 
                                scanf("%c", &x[i][j]);
                        scanf("%c", &x[0][0]);                
                }
                //scanf("%c", &x[0][0]);
                //if (cas == 5)
                        //for (int i = 1; i <= 4; i ++) {
                                //for (int j = 1; j <= 4; j ++)
                                        //printf("%c", x[i][j]);
                               // cout <<endl;
                      //  } 
                
                printf("Case #%d: ", cas);
                int n, m, t;
                int flag = 0;
                bool check = true;
                for (int i = 1; i <= 4; i ++)
                        for (int j = 1; j <= 4; j ++)
                                if (x[i][j] == '.') check = false;
                
                for (int i = 1; i <= 4; i ++) {
                        n = 0, m = 0, t = 0;
                        for (int j = 1; j <= 4; j ++) {
                                if (x[i][j] == 'X') n ++;
                                if (x[i][j] == 'O') m ++;
                                if (x[i][j] == 'T') t ++;
                        }                
                        if (n == 4 || (n == 3 && t == 1)) {
                                flag = 1;
                                break;
                        }  
                        if (m == 4 || (m == 3 && t == 1)) {
                                flag = 2;
                                break;
                        }
                        n = 0, m = 0, t = 0;
                        for (int j = 1; j <= 4; j ++) {
                                if (x[j][i] == 'X') n ++;
                                if (x[j][i] == 'O') m ++;
                                if (x[j][i] == 'T') t ++; 
                        }
                        if (n == 4 || (n == 3 && t == 1)) {
                                flag = 1;
                                break;
                        }  
                        if (m == 4 || (m == 3 && t == 1)) {
                                flag = 2;
                                break;
                        }
                        
                        n = 0, m = 0, t = 0;
                        for (int j = 1; j <= 4; j ++) {
                                if (x[j][j] == 'X') n ++;
                                if (x[j][j] == 'O') m ++;
                                if (x[j][j] == 'T') t ++;        
                        }    
                        if (n == 4 || (n == 3 && t == 1)) {
                                flag = 1;
                                break;
                        }  
                        if (m == 4 || (m == 3 && t == 1)) {
                                flag = 2;
                                break;
                        }

                        n = 0, m = 0, t = 0;
                        for (int j = 1; j <= 4; j ++) {
                                if (x[j][4 - j + 1] == 'X') n ++;
                                if (x[j][4 - j + 1] == 'O') m ++;
                                if (x[j][4 - j + 1] == 'T') t ++;        
                        }    
                        if (n == 4 || (n == 3 && t == 1)) {
                                flag = 1;
                                break;
                        }  
                        if (m == 4 || (m == 3 && t == 1)) {
                                flag = 2;
                                break;
                        }

                }        
        
                if (flag == 1) cout <<"X won"<<endl;
                if (flag == 2) cout <<"O won"<<endl;
                if (flag == 0) {
                        if (check) cout <<"Draw"<<endl; else cout <<"Game has not completed"<<endl;
                }        
        }
        
        return 0;
}













