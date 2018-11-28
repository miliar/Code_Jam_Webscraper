#include <cstdio>

char tab[4][4];


void ReadTab(FILE *file)
{
     char a;
     for(int i=0;i<4;++i)
     {
             for(int j=0;j<4;++j)
             {
                     fscanf(file, "%c", &a);
                     tab[i][j]=a;
             }
             fscanf(file, "\n");
     }
}

bool X_win_state()
{
     //checking rows
     for(int i=0;i<4;++i)
     {
             if(tab[i][0]=='T' || tab[i][0]=='X')
                               if(tab[i][1]=='T' || tab[i][1]=='X')
                                                 if(tab[i][2]=='T' || tab[i][2]=='X')
                                                                   if(tab[i][3]=='T' || tab[i][3]=='X')
                                                                                     return true;               
     }
     
     //checking columns
     for(int i=0;i<4;++i)
     {
             if(tab[0][i]=='T' || tab[0][i]=='X')
                               if(tab[1][i]=='T' || tab[1][i]=='X') 
                                                 if(tab[2][i]=='T' || tab[2][i]=='X') 
                                                                   if(tab[3][i]=='T' || tab[3][i]=='X') 
                                                                                     return true;        
     }
     
     //checking diagonals
     
     if(tab[0][0]=='X' || tab[0][0]=='T')
                       if(tab[1][1]=='X' || tab[1][1]=='T')
                                         if(tab[2][2]=='X' || tab[2][2]=='T')
                                                           if(tab[3][3]=='X' || tab[3][3]=='T')
                                                                             return true;
     if(tab[0][3]=='X' || tab[0][3]=='T')
                       if(tab[1][2]=='X' || tab[1][2]=='T')
                                         if(tab[2][1]=='X' || tab[2][1]=='T')
                                                           if(tab[3][0]=='X' || tab[3][0]=='T')
                                                                             return true;
        
     return false;
}


bool O_win_state()
{
     //checking rows
     for(int i=0;i<4;++i)
     {
             if(tab[i][0]=='T' || tab[i][0]=='O')
                               if(tab[i][1]=='T' || tab[i][1]=='O')
                                                 if(tab[i][2]=='T' || tab[i][2]=='O')
                                                                   if(tab[i][3]=='T' || tab[i][3]=='O')
                                                                                     return true;               
     }
     
     //checking columns
     for(int i=0;i<4;++i)
     {
             if(tab[0][i]=='T' || tab[0][i]=='O')
                               if(tab[1][i]=='T' || tab[1][i]=='O') 
                                                 if(tab[2][i]=='T' || tab[2][i]=='O') 
                                                                   if(tab[3][i]=='T' || tab[3][i]=='O') 
                                                                                     return true;        
     }
     
     //checking diagonals
     
     if(tab[0][0]=='O' || tab[0][0]=='T')
                       if(tab[1][1]=='O' || tab[1][1]=='T')
                                         if(tab[2][2]=='O' || tab[2][2]=='T')
                                                           if(tab[3][3]=='O' || tab[3][3]=='T')
                                                                             return true;
     if(tab[0][3]=='O' || tab[0][3]=='T')
                       if(tab[1][2]=='O' || tab[1][2]=='T')
                                         if(tab[2][1]=='O' || tab[2][1]=='T')
                                                           if(tab[3][0]=='O' || tab[3][0]=='T')
                                                                             return true;
     
     return false;
}


bool Game_finished()
{
     for(int i=0;i<4;++i)
     {
             for(int j=0;j<4;++j)
             {
                     if(tab[i][j]=='.')
                                       return false;
             }
     }
     return true;
}

void game(int n,FILE *file, bool x, bool o, bool finished)
{
     
     /*fprintf(file, "X %d\n", (int)x);
     fprintf(file, "O %d\n", (int)o);
     fprintf(file, "Game %d\n", (int)finished);*/

     if(x==true && o==false)
                fprintf(file,"Case #%d: X won\n",n);
     else if(x==false && o==true)
          fprintf(file,"Case #%d: O won\n",n);
          else if(x==false && o==false && finished==false)
               fprintf(file,"Case #%d: Game has not completed\n",n);
               else
                   fprintf(file,"Case #%d: Draw\n",n);
}

int main()
{
    FILE *fwrite;
    fwrite=fopen("output.txt","w");
    FILE *fread;
    fread=fopen("A-large.in", "r");
    
    int games;
    fscanf(fread, "%d \n", &games);
    for(int i=0;i<games;++i)
    {
            ReadTab(fread);
            game(i+1,fwrite,X_win_state(), O_win_state(), Game_finished());
            /*for(int i=0;i<4;++i)
            {
                    for(int j=0;j<4;++j)                    
                            fprintf(fwrite, "%c", tab[i][j]);
                    fprintf(fwrite,"\n");
            }*/
    }
     
     fclose(fwrite);
     fclose(fread);
     return 0;
}
