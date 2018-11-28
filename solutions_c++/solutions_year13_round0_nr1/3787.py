#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <assert.h>
#include<string>
using namespace std;
int main()
{
    int t, n, k;
	FILE *fp=fopen("in.txt", "r"), *ofp=fopen("out.txt", "w");
    char s[10][10];
    fscanf(fp, "%d", &n);
    for(int k=1;k<=n;k++) {
       for(int i=0;i<4;i++) {
               fscanf(fp, "%s", &s[i][0]);
       }
       int in = 0;
       bool flag = false;
       for(int i=0;i<4;i++) {
           int a = 0, b = 0, c = 0, d= 0;
           for(int j=0;j<4;j++) {
               if(s[i][j] == 'O') a++;
               if(s[i][j] == 'X') b++;
               if(s[i][j] == 'T') a++, b++;

               if(s[j][i] == 'O') c++;
               if(s[j][i] == 'X') d++;
               if(s[j][i] == 'T') c++, d++;

               if(s[i][j] == '.') in = 1;
           }
           if(a == 4 || c == 4) {
              fprintf(ofp, "Case #%d: %s\n", k, "O won");
              flag = true;
              break;
           }
           else if(b == 4 || d == 4) {
              fprintf(ofp, "Case #%d: %s\n", k, "X won");
              flag = true;
              break;
           }
       }
       int a = 0, b = 0, c = 0, d = 0;
       for(int i=0;i<4;i++) {
          if(s[i][i] == 'O') a++;
          if(s[i][i] == 'X') b++;
          if(s[i][i] == 'T') a++, b++;

          if(s[3-i][i] == 'O') c++;
          if(s[3-i][i] == 'X') d++;
          if(s[3-i][i] == 'T') c++, d++;
       }
       if(flag == false)
          if(a == 4 || c == 4) {
              fprintf(ofp, "Case #%d: %s\n", k, "O won");
              flag = true;
           }
           else if(b == 4 || d == 4) {
              fprintf(ofp, "Case #%d: %s\n", k, "X won");
              flag = true;
           }
       if(flag == false) {
          if(in) fprintf(ofp, "Case #%d: %s\n", k, "Game has not completed");
          else fprintf(ofp, "Case #%d: %s\n", k, "Draw");
       }

    }           
    fclose(fp);fclose(ofp); 
    system("pause");
    return 0;
}
