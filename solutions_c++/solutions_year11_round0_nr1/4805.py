#include<iostream>
#include<conio.h>
using namespace std;
struct robot
{
 char color;
 short position[100];
 bool kolejnosc[100];
 short actual;
 short bef;
};
short movement(robot orange, robot blue, const short n)
{
 short moves = 0; 
 for (int x = 0; x < n; x++)
 { // dla ka¿dego przypadku
 bool czy = false;
  do
  {
   if (blue.actual < blue.position[blue.bef]) ++blue.actual; 
   else if (blue.actual == blue.position[blue.bef] && blue.kolejnosc[x] == true) {++blue.bef;czy = true;}
   else if (blue.actual > blue.position[blue.bef]) --blue.actual; //dla blue
   if (orange.actual < orange.position[orange.bef]) ++orange.actual;
   else if (orange.actual == orange.position[orange.bef] && orange.kolejnosc[x] == true) {++orange.bef;czy = true;}
   else if (orange.actual > orange.position[orange.bef]) --orange.actual;
  
   ++moves;
  } while (czy == false);
 }
 return moves;
}
int main()
{
 short t,n; robot orange, blue; short wynik[100];
 orange.color = 'O'; blue.color = 'B';
 cin >> t;
 for (int i = 0; i < t; i++)
 {
  cin >> n; orange.bef = 0; blue.bef = 0;
  for (int b = 0; b < n; b++)
  {
    orange.actual = 1; blue.actual = 1;
   char ktory;
   cin >> ktory;
   switch (ktory)
   {
    case 'O': cin >> orange.position[orange.bef];   blue.kolejnosc[b] = false; orange.kolejnosc[b] = true; ++orange.bef; break;
    case 'B': cin >> blue.position[blue.bef];  orange.kolejnosc[b] = false; blue.kolejnosc[b] = true; ++blue.bef; break;
   }
  }
  orange.bef = 0; blue.bef = 0;
  wynik[i] = movement(orange, blue, n);
 }
 for (int i = 0; i < t; i++)
 {
      cout << "Case #" << i+1 << ": " << wynik[i] << endl;
 }  
 return 0;
}
