#include <cstdio>
#include <cstdlib>

int main(int argc, char **argv)
{
    int N = 0;
    int buttons = 0;
    
    int pos_O = 1;
    int pos_B = 1;    
    int temp = 0;
    int total_moves = 0;
    int temp_moves = 0;
    int curr_move = 0;
    char color;
    char prev_color;    
    
    
    scanf("%d", &N);
    
    for (int i = 1; i <= N; i++)
    {
          scanf("%d", &buttons);
          
          total_moves = 0;
          temp_moves = 0;
          pos_O = 1;
          pos_B = 1;
          prev_color = '\0';
          
          while (buttons--)
          {
               scanf(" %c", &color);
               scanf("%d", &temp);
               
               if (color == 'O')
               {
                  curr_move = abs(temp - pos_O) + 1;
                  pos_O = temp;
               }
               else
               {
                  curr_move = abs(temp - pos_B) + 1;
                  pos_B = temp;
               }
               
               
               
               if (color == prev_color || prev_color == '\0')
               {
                 total_moves += curr_move;
                 temp_moves += curr_move;
               }
                 
               else
               {
                 if (curr_move > temp_moves)
                    temp_moves = curr_move - temp_moves;  
                 else
                    temp_moves = 1;
                    
                 total_moves += temp_moves;
               }
               prev_color = color;
          }
          
          printf("Case #%d: %d\n", i, total_moves);
    }    
    
    return 0;
}
