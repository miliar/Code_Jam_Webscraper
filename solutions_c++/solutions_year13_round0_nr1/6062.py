#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

double output[200];

FILE *fpd = NULL;

void solve()
{
}

int main ()
{
    int T;
    
    FILE *fpI = fopen("A-small-attempt1.in", "r");
    FILE *fpO = fopen("output.txt", "w+");
    
    fpd = fopen("debug.txt", "w+");
    
    
    fscanf(fpI, "%d", &T);
    fprintf(fpd, "%d\n", T);
    for (int i = 0; i < T; i++)
    {
        unsigned int s[8][8] = {0};
        int x_left_diag_cnt = 0;
        int x_right_diag_cnt = 0;
        int o_right_diag_cnt = 0;
        int o_left_diag_cnt = 0;
        int t_right_diag_cnt = 0;
        int t_left_diag_cnt = 0;
        
        int no_of_x = 0;
        int no_of_o = 0;
        int no_of_t = 0;
        
        int x_won = 0;
        int o_won = 0;
        int draw = 0; 
                  
         fprintf(fpd, "\n Printing Grid Info for Test case %d\n", i);
         fscanf(fpI, "%c", &s[0][0]);
         for (int j = 1; j <= 4; j++)
         {
              for (int k = 1; k <= 4; k++) {
                  fscanf(fpI, "%c", &s[j][k]);
                  if (s[j][k] == 'X') {
                      s[j][5]++;
                      s[5][k]++;
                      if (j == k) {
                            x_left_diag_cnt++;
                      }
                  }

                  if (s[j][k] == 'O') {
                      s[j][6]++;
                      s[6][k]++;
                      if (j == k) {
                            o_left_diag_cnt++;
                      }
                  }

                  if (s[j][k] == 'T') {
                      s[j][7]++;
                      s[7][k]++;
                      if (j == k) {
                            t_left_diag_cnt++;
                      }
                  }

                  fprintf(fpd, "%c ", s[j][k]);
              }
                  if (s[j][5-j] == 'X') {
                           x_right_diag_cnt++;
                  }
                  if (s[j][5-j] == 'O') {
                           o_right_diag_cnt++;
                  }
                  if (s[j][5-j] == 'T') {
                           t_right_diag_cnt++;
                  }
              fscanf(fpI, "%c", &s[0][0]);
              fprintf(fpd, "\n");
         }
         
        fprintf(fpd, "\n x_left_diag_cnt = %d", x_left_diag_cnt);
        fprintf(fpd, "\n x_right_diag_cnt = %d", x_right_diag_cnt);
        fprintf(fpd, "\n o_left_diag_cnt = %d", o_left_diag_cnt);
        fprintf(fpd, "\n o_right_diag_cnt = %d", o_right_diag_cnt);
        fprintf(fpd, "\n t_left_diag_cnt = %d", t_left_diag_cnt);
        fprintf(fpd, "\n t_right_diag_cnt = %d", t_right_diag_cnt);
        
        fprintf(fpd, "\n\n\n");

        if ((x_left_diag_cnt == 4) || (x_left_diag_cnt == 3 && t_left_diag_cnt == 1)
            || (x_right_diag_cnt == 4)|| (x_right_diag_cnt == 3 && t_right_diag_cnt == 1)) {
            
            x_won = 1;
        }
                
        if ((o_left_diag_cnt == 4) || (o_left_diag_cnt == 3 && t_left_diag_cnt == 1)
            || (o_right_diag_cnt == 4) || (o_right_diag_cnt == 3 && t_right_diag_cnt == 1)) {
            
            o_won = 1;
        }
        
        for (int a = 1; a <= 4; a++) {
            if (s[a][5] == 4 || (s[a][5] == 3 && s[a][7]  == 1)) {
               x_won = 1;
               break;
            }
            
            if (s[a][6] == 4 || (s[a][6] == 3 && s[a][7]  == 1)) {
               o_won = 1;
               break;
            }
            
            if (s[5][a] == 4 || (s[5][a] == 3 && s[7][a]  == 1)) {
               x_won = 1;
               break;
            }
            
            if (s[6][a] == 4 || (s[6][a] == 3 && s[7][a]  == 1)) {
               o_won = 1;
               break;
            }
            no_of_x += s[a][5];
            no_of_o += s[a][6];
        }
        
        no_of_t += t_left_diag_cnt + t_right_diag_cnt;
        fprintf(fpd, "\n no_of_x = %d", no_of_x);
        fprintf(fpd, "\n no_of_o = %d", no_of_o);
        fprintf(fpd, "\n no_of_t = %d", no_of_t);
        if ((no_of_x == 8 || no_of_o == 8) && (no_of_x + no_of_t == no_of_o || no_of_x ==  no_of_o + no_of_t)) {
            draw = 1;
        }
        
        fprintf(fpO, "Case #%d: ", (i+1));
        
        if (x_won)
        {
           fprintf(fpO, "X won\n");
        }
        else if (o_won) 
        {
           fprintf(fpO, "O won\n");
        }
        else if (draw)
        {
           fprintf(fpO, "Draw\n");
        }
        else 
        {
           fprintf(fpO, "Game has not completed\n");
        }
    } 
}
