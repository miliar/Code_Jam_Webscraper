#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;


FILE *fin, *fout; 


void solution(char *input, char *output)
{
    fin = fopen(input,"r");
    fout = fopen(output,"w+");
    int T;
    fscanf(fin,"%d\n",&T);
    //printf("T is = %d\n\n" ,T );
    for(int k=0;k<T;k++)
    {
        char a[4][4];
        short v[4]={0,0,0,0};
        short vertical =0;
        short hor = 0;
        short t= 10;
        short found = 0; // 1 for X , 2 for O, 3 for Game not completed , 4 for draw
        
        fscanf(fin,"%c %c %c %c %c %c %c %c %c %c %c %c %c %c %c %c\n",&a[0][0], &a[0][1],&a[0][2], &a[0][3], 
                       &a[1][0], &a[1][1], &a[1][2], &a[1][3], &a[2][0], &a[2][1], &a[2][2], &a[2][3], &a[3][0], &a[3][1], &a[3][2], &a[3][3]);
        
        for(int i=0 ;i <4; i++)
        {
             for(int j=0; j<4; j++)
             {
                     if(j==0) hor = 0;
                     if(a[i][j] == 'T')
                     {
                        v[j] += t;
                        hor += t;
                     }                    
                     else if(a[i][j] == 'X') 
                      {
                        v[j]++;
                        hor++;
                      }
                     else if(a[i][j] == 'O') 
                      {
                        v[j]--;
                        hor--;
                      }
                     else if(a[i][j] == '.')
                     {
                        found = 3;
                        break;
                     }
                     if(( i==3 && (v[j] == 4 || v[j] == 13)) || hor == 4 || hor == 13)
                      {
                        found = 1;
                        break;
                      } 
                     if(( i==3 && (v[j] == -4 || v[j] == 7)) || hor == -4 ||hor == 7)
                      {
                        found = 2;
                        break;
                      }                       
                    
             }    // Exit from j loop of matrix
          if(found ==1 || found == 2)
          {
            break;
          }    
        } // Exit from the outer i loop of matrix 
        if(found == 0 || found == 3)
        {
          short score_diag1=0;
          short score_diag2 =0;
          for(int i=0 ;i <4; i++)
           {
                  if(a[i][i] == 'X')
                     score_diag1 += 1;
                  else if(a[i][i] == 'O')
                     score_diag1 -= 1;
                  else if(a[i][i] == 'T')
                     score_diag1 += t;
                 
                  if(a[i][3-i] == 'X')
                     score_diag2 += 1;
                  else if(a[i][3-i] == 'O')
                     score_diag2 -= 1;
                  else if(a[i][3-i] == 'T')
                   score_diag2 += t;
            }
          if(score_diag1 == 4 || score_diag2 == 4 || score_diag1 == 13 || score_diag2 == 13)
          {
             found = 1;
          }
          else if(score_diag1 == -4 || score_diag2 == -4|| score_diag1 == 7 || score_diag2 == 7)
          {
             found = 2;
          }
          
        }
       if(found == 0)
         found = 4; 
       fprintf(fout,"Case #%d: ", k+1);
       switch(found)
       {
          case 1 :
               fprintf(fout,"X won\n");
               break;
          case 2 :
               fprintf(fout,"O won\n");
               break;
          case 3 :
               fprintf(fout,"Game has not completed\n");
               break;
          case 4 :
               fprintf(fout,"Draw\n");
               break;
          default:
               break;
               
       }
       //fprintf(fout,"%d\n", found);
    } // Exit the For loop taking inputs
    fclose(fin);
    fclose(fout);
} // Exit solution

int main ()
{
    solution("A-small-attempt0.in", "Output.txt");
   // getchar();
    return 0;
}
