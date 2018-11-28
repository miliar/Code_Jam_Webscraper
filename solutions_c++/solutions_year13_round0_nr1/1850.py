#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
using namespace std;

bool fless(double a,double b){ return b-a>1e-6; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-6; }

char s[10][10];
int N = 4;

bool done = false, not_completed = false;
char ans;

int check_rows(){
  // row
  for (int i=0;i<N;i++){
    char sym = s[i][0];
    if (sym == '.') {
      not_completed = true;   
      continue;
    }
    bool ok = true;
    for (int j=1;j<N;j++){
      if (s[i][j] =='.') {
        ok = false;
        not_completed = true;
      }
      if (sym=='T'){
        sym = s[i][j];
      }
      if (sym != s[i][j] && s[i][j]!='T') {
        ok = false;
      }
    }
    if (ok){
      ans = sym;
      done = true;
    }
  }
}

int check_cols(){
        // col
        for (int i=0;i<N;i++){
            char sym = s[0][i];
            if (sym == '.') {
                not_completed = true;   
                continue;
            }
            bool ok = true;
            for (int j=1;j<N;j++){
                if (s[j][i] =='.') {
                    ok = false;
                    not_completed = true;
                }
                if (sym=='T'){
                    sym = s[j][i];
                }
                if (sym != s[j][i] && s[j][i]!='T') {
                    ok = false;
                }
            }
            if (ok){
                ans = sym;
                done = true;
            }
        }
}

int check_dia1(){
    char sym = s[0][0];
    if (sym == '.') {
        not_completed = true;
        return 0;
    }
    bool ok = true;
    for (int i=1;i<N;i++){
        if (s[i][i] == '.') {
            ok = false;
            not_completed = true;
        }
        if (sym=='T'){
            sym = s[i][i];
        }
        if (sym != s[i][i] && s[i][i]!='T') {
          ok = false;
        }
    }
    if (ok){
        ans = sym;
        done = true;
    }
}
int check_dia2(){
    char sym = s[3][0];
    if (sym == '.') {
        not_completed = true;
        return 0;
    }
    bool ok = true;
    for (int i=1;i<N;i++){
        if (s[3-i][i] == '.') {
            ok = false;
            not_completed = true;
        }
        if (sym=='T'){
            sym = s[3-i][i];
        }
        if (sym != s[3-i][i] && s[3-i][i]!='T') {
          ok = false;
        }
    }
    if (ok){
        ans = sym;
        done = true;
    }
}

int main(){
    int tt; scanf("%d",&tt);
    for (int ti=1;ti<=tt;ti++){
        done = false; 
        not_completed = false;
        ans = ' ';

        for (int i=0;i<N;i++){
            scanf("%s", s[i]);
        }

        check_rows();
        check_cols();
        check_dia1();
        check_dia2();

        printf("Case #%d: ",ti);
        if (done) {
            if (ans=='O') printf("O won");
            else if (ans=='X') printf("X won");
        } else {
            if (not_completed) printf("Game has not completed");
            else printf("Draw");
        } 
        puts("");
    }
    return 0;
}

