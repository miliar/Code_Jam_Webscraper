#include <stdio.h>
#include <stdlib.h>

char a[4][4];

char readin()
{
 char c;
 while (scanf("%c", &c), c!='.' && c!='T' && c!='O' && c!='X');
 return c;     
}
     
void init()
{
     for (int i = 0; i < 4; ++i)
         for (int j = 0; j < 4; ++j)
             a[i][j] = readin();     
}

bool empty()
{
     for (int i = 0; i < 4; ++i)for (int j = 0; j < 4; ++j) if (a[i][j] == '.') return true;
     return false;     
}
     
void getwin(int flag)
{
     if (flag == 1) printf("X won\n"); else printf("O won\n");     
}
     
void work()
{
     for (int i = 0; i < 4; ++i){
         int flag = 0;/*0 start; 1:X 2:O -1:Failure*/
         for (int j = 0; j < 4; ++j)
             if (a[i][j] == '.'){ flag = -1; break;}
             else if (a[i][j] =='T') continue;
             else if (a[i][j] =='O'){
                  if (flag == 0 || flag == 2) flag = 2; else {flag = -1; break;}
             }
             else
             {
                  if (flag == 0 || flag == 1) flag = 1; else {flag = -1; break;}
             }
             if (flag!=-1) {
                getwin(flag); return;
             }
     }     
     for (int j = 0; j < 4; ++j){
         int flag = 0;/*0 start; 1:X 2:O -1:Failure*/
         for (int i = 0; i < 4; ++i)
             if (a[i][j] == '.'){ flag = -1; break;}
             else if (a[i][j] =='T') continue;
             else if (a[i][j] =='O'){
                  if (flag == 0 || flag ==2 ) flag = 2; else {flag = -1; break;}
             }
             else
             {
                  if (flag == 0 || flag == 1) flag = 1; else {flag = -1; break;}
             }
             if (flag!=-1) {
                getwin(flag); return;
             }
     }     
         int flag = 0;/*0 start; 1:X 2:O -1:Failure*/
         for (int i = 0; i < 4; ++i)
             if (a[i][i] == '.'){ flag = -1; break;}
             else if (a[i][i] =='T') continue;
             else if (a[i][i] =='O'){
                  if (flag == 0 || flag == 2) flag = 2; else {flag = -1; break;}
             }
             else
             {
                  if (flag == 0 || flag == 1) flag = 1; else {flag = -1; break;}
             }
             if (flag!=-1) {
                getwin(flag); return;
             }
         flag = 0;
         for (int i = 0; i < 4; ++i)
             if (a[i][3-i] == '.'){ flag = -1; break;}
             else if (a[i][3-i] =='T') continue;
             else if (a[i][3-i] =='O'){
                  if (flag == 0 || flag == 2) flag = 2; else {flag = -1; break;}
             }
             else
             {
                  if (flag == 0 || flag == 1) flag = 1; else {flag = -1; break;}
             }
             if (flag!=-1) {
                getwin(flag); return;
             }
         
         if (empty()) 
            printf("Game has not completed\n");
         else
             printf("Draw\n");
             
}
          
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cases, i = 0;
    scanf("%d", &cases);
    while (cases--){
          ++i;
          printf("Case #%d: ", i);
          init();
          work();      
    }
    return 0;
}
