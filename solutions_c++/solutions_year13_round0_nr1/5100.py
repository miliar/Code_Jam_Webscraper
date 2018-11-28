#include <stdio.h>
#include <string.h>
#include <windows.h>
#include <algorithm>
#include <vector>
using namespace std;

int C;




char input[4][4];
bool IsWon(char P);
bool IsTie();
main () {
	FILE *fin  = fopen ("in", "r");
	FILE *fout = fopen ("out", "w");

fscanf( fin, " %d", &C);

for (int i = 0; i < C; i++)
 {

 for (int i = 0; i < 4; i++)
  {
	    fscanf( fin, "%s", &input[i][0]);
  }

if (IsWon('X'))
{
   fprintf (fout, "Case #%d: X won\n",i+1);
}
else if(IsWon('O'))
{
   fprintf (fout, "Case #%d: O won\n",i+1);
}
else if(IsTie())
{
    fprintf (fout, "Case #%d: Draw\n",i+1);
}
else
{
    fprintf (fout, "Case #%d: Game has not completed\n",i+1);
}
 }




	return 0;
}
bool IsTie()
{
   for (int i = 0; i < 4; i++)
   {
       for (int j=0;j<4;j++)
       {
         if (input[i][j]=='.')
         {
             return false;
         }
       }
   }
   return true;
}

bool IsWon(char P)
{
   int c=0;
   for (int i = 0; i < 4; i++)
   {
       for (int j=0;j<4;j++)
       {
         if (input[i][j]==P || input[i][j]=='T')
         {
             c++;
         }
       }
       if (c==4)
       {
           return true;
       }
       else
       {
           c=0;
       }
   }

   for (int i = 0; i < 4; i++)
   {
       for (int j=0;j<4;j++)
       {
         if (input[j][i]==P || input[j][i]=='T')
         {
             c++;
         }
       }
       if (c==4)
       {
           return true;
       }
       else
       {
           c=0;
       }
   }

for (int i = 0; i < 4; i++)
   {
         if (input[i][i]==P || input[i][i]=='T')
         {
             c++;
         }
   }
          if (c==4)
       {
           return true;
       }
       else
       {
           c=0;
       }

for (int i = 0; i < 4; i++)
   {
         if (input[i][3-i]==P || input[i][3-i]=='T')
         {
             c++;
         }
   }
          if (c==4)
       {
           return true;
       }
       else
       {
           return false;
       }

}
