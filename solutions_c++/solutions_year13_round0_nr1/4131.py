#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int solve (vector <string> grid, char c) {
   string a (4, c);
   for (int i = 0; i < 4; i++) //Row
       if (grid [i] == a) return true;
   string b = "";
   for (int i = 0; i < 4; i++) { //Column
       for (int j = 0; j < 4; j++)
           b += grid [j][i];
       if (b == a) return true;
       b = "";
   }
   for (int i = 0; i < 4; i++)  //Diagonal
       for (int j = 0; j < 4; j++)
           if (i == j)
               b += grid [i][j];
   if (b == a) return true;
   b = "";
   for (int i = 0; i < 4; i++)  // reverse diagonal
       for (int j = 0; j < 4; j++)
           if (i + j == 3)
               b += grid [i][j];
   if (b == a) return true;
   return false;

}
int main () {
   freopen ("test.in", "r", stdin);
   freopen ("test.out", "w", stdout);
   int T;
   scanf ("%d", &T);
   string a, b;
   for (int t = 1; t <= T; t++) {
       vector <string> mat1;
       vector <string> mat2;
       int count1 = 0;
       for (int i = 0; i < 4; i++) {
           cin >> a;
           count1 += count (a.begin (), a.end (), '.');
           b = a;
           replace (a.begin (), a.end (), 'T', 'O');
           replace (b.begin (), b.end (), 'T', 'X');
           mat1.push_back (a);
           mat2.push_back (b);
       }   
       if (solve (mat1, 'O')==1) printf ("Case #%d: O won\n", t); 
       else if (solve (mat2, 'X')==1) printf ("Case #%d: X won\n", t); 
       else if (count1 == 0) printf ("Case #%d: Draw\n", t); 
       else printf ("Case #%d: Game has not completed\n", t); 
   }   

   return 0;
}