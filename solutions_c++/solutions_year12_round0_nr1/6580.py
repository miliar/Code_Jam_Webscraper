// reading a text file
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
char sentence[301];
int case1=1;
int number = 0;
int count=0;
int arraynum=0;
char junk[5];

int main () {
  string line;
  ifstream myfile ("A-small-attempt9.in");
  myfile >> number;
  if (myfile.is_open())
  {
	myfile.getline(junk, 3);

    while ( number > 0 )
    {
	
      myfile.getline(sentence, 300);
	  arraynum=strlen(sentence) ;
	  count=0;
	  
	  while (count < arraynum )
	  {
	if (sentence[count] == 'a')
    sentence[count] = 'y';
    else
    if (sentence[count] == 'b')
    sentence[count] = 'h';
    else
    if (sentence[count] == 'c')
    sentence[count] = 'e';
    else
    if (sentence[count] == 'd')
    sentence[count] = 's';
    else
    if (sentence[count] == 'e')
    sentence[count] = 'o';
    else
    if (sentence[count] == 'f')
    sentence[count] = 'c';
    else
    if (sentence[count] == 'g')
    sentence[count] = 'v';
    else
    if (sentence[count] == 'h')
    sentence[count] = 'x';
    else
    if (sentence[count] == 'i')
    sentence[count] = 'd';
    else
    if (sentence[count] == 'j')
    sentence[count] = 'u';
    else
    if (sentence[count] == 'k')
    sentence[count] = 'i';
    else
    if (sentence[count] == 'l')
    sentence[count] = 'g';
    else
    if (sentence[count] == 'm')
    sentence[count] = 'l';
    else
    if (sentence[count] == 'n')
    sentence[count] = 'b';
    else
    if (sentence[count] == 'o')
    sentence[count] = 'k';
    else
    if (sentence[count] == 'p')
    sentence[count] = 'r';
    else
    if (sentence[count] == 'q')
    sentence[count] = 'z';
    else
    if (sentence[count] == 'r')
    sentence[count] = 't';
    else
    if (sentence[count] == 's')
    sentence[count] = 'n';
    else
    if (sentence[count] == 't')
    sentence[count] = 'w';
    else
    if (sentence[count] == 'u')
    sentence[count] = 'j';
    else
    if (sentence[count] == 'v')
    sentence[count] = 'p';
    else
    if (sentence[count] == 'w')
    sentence[count] = 'f';
    else
    if (sentence[count] == 'x')
    sentence[count] = 'm';
    else
    if (sentence[count] == 'y')
    sentence[count] = 'a';
    else
    if (sentence[count] == 'z')
    sentence[count] = 'q';
    else {
    sentence[count] = ' ';
	
	}
	count++;
	  }
	  ofstream myfile2;
  myfile2.open ("example.out", ios::app);
   myfile2 << "Case #"<< case1 << ": ";
	  myfile2 << sentence << endl;
  myfile2.close();
      
	  
	  case1++;

	  number--;
	  memset(sentence, 0, sizeof(sentence));
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}
