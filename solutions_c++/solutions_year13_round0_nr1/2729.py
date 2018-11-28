#include <iostream>
#include <fstream>
using namespace std;

const char CDATA[] = "A-large.in";
const char CRES[]  = "output.out";

int n;
char tab[4][4];

// Decleration of funcions
bool CheckRow(char,int);
bool CheckColumn(char,int);
bool CheckDiagonal(char);

int main()
{
    ifstream fin(CDATA);
    ofstream fout(CRES);
    fin >> n;

    for (int i = 0; i < n; ++i)
    {
       int xNum = 0;
       int oNum = 0;
       int tNum = 0;

       for (int j = 0; j < 4; ++j)
         for (int k = 0; k < 4; ++k)
         {
            fin >> tab[j][k];
            if (tab[j][k] == 'X') xNum++;
            if (tab[j][k] == 'O') oNum++;
            if (tab[j][k] == 'T') tNum++;
         }

       bool found = false;
       for (int j = 0; j < 4; ++j)
         if (!found && (CheckRow('X',j) || CheckColumn('X',j)))
         {
            fout << "Case #" << i+1 << ": X won\n";
            found = true;
         }
         else if (!found && (CheckRow('O',j) || CheckColumn('O',j)))
         {
            fout << "Case #" << i+1 << ": O won\n";
            found = true;
         }

       if (!found)
       {
         if (CheckDiagonal('X'))
            fout << "Case #" << i+1 << ": X won\n";
         else if (CheckDiagonal('O'))
            fout << "Case #" << i+1 << ": O won\n";
         else if (xNum + oNum + tNum == 16)
            fout << "Case #" << i+1 << ": Draw\n";
         else
            fout << "Case #" << i+1 << ": Game has not completed\n";
       }
    }
    fin.close();
    fout.close();

    return 0;
}

bool CheckRow(char a, int k)
{
   for (int i = 0; i < 4; ++i)
      if (tab[k][i] != a && tab[k][i] != 'T') return false;
   return true;
}

bool CheckColumn(char a, int k)
{
   for (int i = 0; i < 4; ++i)
      if (tab[i][k] != a && tab[i][k] != 'T') return false;
   return true;
}

bool CheckDiagonal(char a)
{
   int stmp  = 0;
   int stmp2 = 0;
   for (int i = 0; i < 4; ++i)
   {
      if (tab[i][i] == a || tab[i][i] == 'T') stmp++;
      if (tab[4-i-1][i] == a || tab[4-i-1][i] == 'T') stmp2++;
   }

   if (stmp == 4 || stmp2 == 4)
      return true;
   return false;
}
