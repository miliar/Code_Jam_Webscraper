/* 
 * File:   main.cpp
 * Author: a.elbashandi
 *
 * Created on April 13, 2013, 7:27 PM
 */

#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define pi acos(-1.0)
#define N 1000000
#define LL long long

#define For(i, a, b) for( int i = (a); i < (b); i++ )
#define Fors(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fore(it, x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define Set(a, s) memset(a, s, sizeof (a))
#define Read(r) freopen(r, "r", stdin)
#define Write(w) freopen(w, "w", stdout)

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    
    Read("A-large.in");
    Write("file.out");
    
    int T, cases = 1; scanf("%d", &T);
    while(T--){
        char buff[4][4];
        char a;
        bool thereIsPoint = false;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf(" %c", &a);
                buff[i][j] = a;
                if(a == '.')
                    thereIsPoint = true;
            }
        }
        
        string str[10];
        char st[4];
        for (int i = 0; i < 4; i++) {
            str[i] = "";
            for (int j = 0; j < 4; j++) {
                char c = buff[i][j];
                str[i] += c;
            }
            
            str[i + 4] = "";
            for (int j = 0; j < 4; j++) {
                char c = buff[j][i];
                str[i + 4] += c;
            }
        }
        
        str[8] = "";
        str[9] = "";
        
        for (int i = 0; i < 4; i++) {
            char c = buff[i][i];
            str[8] += c;
            c = buff[i][3 - i];
            str[9] += c;
        }
               
        
        bool xWin, yWin;
        xWin = yWin = false;
        for (int i = 0; i < 10; i++) {
            if(str[i] == "XXXT" || str[i] == "XXTX" || str[i] == "XTXX" || str[i] == "TXXX" || str[i] == "XXXX"){
                xWin = true;
                break;
            }else if(str[i] == "OOOT" || str[i] == "OOTO" || str[i] == "OTOO" || str[i] == "TOOO" || str[i] == "OOOO"){
                yWin = true;
                break;
            }
        }
        
        if(xWin)
            printf("Case #%d: X won\n", cases++);
        else if(yWin)
            printf("Case #%d: O won\n", cases++);
        else if(thereIsPoint)
            printf("Case #%d: Game has not completed\n", cases++);
        else
            printf("Case #%d: Draw\n", cases++);
    }
    return 0;
}

