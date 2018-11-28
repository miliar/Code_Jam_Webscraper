#include <iostream>

using namespace std;



char transformuj(char co)
{
if (co=='a') return 'y';
if (co=='b') return 'h';
if (co=='c') return 'e';
if (co=='d') return 's';
if (co=='e') return 'o';
if (co=='f') return 'c';
if (co=='g') return 'v';
if (co=='h') return 'x';
if (co=='i') return 'd';
if (co=='j') return 'u';
if (co=='k') return 'i';
if (co=='l') return 'g';
if (co=='m') return 'l';
if (co=='n') return 'b';
if (co=='o') return 'k';
if (co=='p') return 'r';
if (co=='q') return 'z';
if (co=='r') return 't';
if (co=='s') return 'n';
if (co=='t') return 'w';
if (co=='u') return 'j';
if (co=='v') return 'p';
if (co=='w') return 'f';
if (co=='x') return 'm';
if (co=='y') return 'a';
if (co=='z') return 'q';

}


int main()
{

 int pocet;
 char pom;

 cin >> pocet;
 cin.get(pom);

 for (int i=1; i<=pocet; i++)
   {
   cout << "Case #" << i << ": ";
   do
     {
	cin.get(pom);
	if (pom!='\n')cout.put(transformuj(pom));
     }
   while (!cin.eof() && pom!='\n');
    cout << '\n';	
   }
 cout << '\n'; 
 return 0;

}
