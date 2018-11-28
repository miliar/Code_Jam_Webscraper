#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

ifstream in("largeA.in");
ofstream out("largeA.out");

int SameRow(vector < vector <char> > a, int row)
{
   for (int j = 0; j < 4; ++j)
      if (a[row][j] != a[row][0])
         return 0;
   if (a[row][0] == '.')
      return 0;
   if (a[row][0] == 'X')
      return -1;
   return 2;
}

int SameCol(vector < vector <char> > a, int col)
{
   for (int i = 0; i < 4; ++i)
      if (a[i][col] != a[0][col])
         return 0;
   if (a[0][col] == '.')
      return 0;
   if (a[0][col] == 'X')
      return -1;
   return 2;
}

int SameDiag1(vector < vector <char> > a)
{
   if (a[1][1] != a[0][0] || a[2][2] != a[0][0] || a[3][3] != a[0][0])
      return false;
   if (a[0][0] == '.')
      return 0;
   if (a[0][0] == 'X')
      return -1;
   return 2;
}

int SameDiag2(vector < vector <char> > a)
{
   if (a[1][2] != a[0][3] || a[2][1] != a[0][3] || a[3][0] != a[0][3])
      return false;
   if (a[0][3] == '.')
      return 0;
   if (a[0][3] == 'X')
      return -1;
   return 2;
}

void print(vector < vector <char> > a)
{
   for (int i = 0; i < 4; ++i)
   {
      for (int j = 0; j < 4; ++j)
         cout << a[i][j];
      cout << endl;
   }
   cout << endl;
}

int Work(vector < vector <char> > a)
{
   return SameRow(a, 0) + SameRow(a, 1) + SameRow(a, 2) + SameRow(a, 3) +
          SameCol(a, 0) + SameCol(a, 1) + SameCol(a, 2) + SameCol(a, 3) +
          SameDiag1(a) + SameDiag2(a);
}

string Solve(vector < vector <char> > a)
{
   for (int i = 0; i < 4; ++i)
      for (int j = 0; j < 4; ++j)
         if (a[i][j] == 'T')
         {
            a[i][j] = 'X';
            int t = Work(a);
            if (t == 0)
            {
               a[i][j] = 'O';
               t = Work(a);
            }
            if (t < 0)
               return "X won";
            if (t > 0)
               return "O won";
         }
   int t = Work(a);
   if (t < 0)
      return "X won";
   if (t > 0)
      return "O won";
   return "";
}

int main()
{
   int test;
   in >> test;   
   for (int t = 1; t <= test; ++t)
   {
      int n, m;
      vector < vector <char> > a(4, vector <char>(4));
      for (int i = 0; i < 4; ++i)
         for (int j = 0; j < 4; ++j)
            in >> a[i][j];
      
      string answer = "Draw";

      for (int i = 0; i < 4; ++i)
         for (int j = 0; j < 4; ++j)
            if (a[i][j] == '.')
               answer = "Game has not completed";
      
      string ans = Solve(a);
      if (ans != "")
         answer = ans;
      
      out << "Case #" << t << ": " << answer << endl;
   }  

   return 0;
}




