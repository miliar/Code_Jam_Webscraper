#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    long long i, t;
    char c;
    fstream infile("A-small.in");
    ofstream outfile("A-small.out");
    infile >> t;
    infile.get(c);
    for(i=1; i<=t; ++i)
    {
      outfile << "Case #" <<i<<": ";
      infile.get(c);
      while (c!='\n'){
      if (c=='a')c='y';
      else if (c=='b')c='h';
      else if (c=='c')c='e';
      else if (c=='d')c='s'; 
      else if (c=='e')c='o';
      else if (c=='f')c='c';
      else if (c=='g')c='v';
      else if (c=='h')c='x';
      else if (c=='i')c='d'; // or q
      else if (c=='j')c='u';
      else if (c=='k')c='i';
      else if (c=='l')c='g';
      else if (c=='m')c='l';
      else if (c=='n')c='b';
      else if (c=='o')c='k';
      else if (c=='p')c='r';
      else if (c=='q')c='z'; 
      else if (c=='r')c='t';
      else if (c=='s')c='n';
      else if (c=='t')c='w';
      else if (c=='u')c='j';
      else if (c=='v')c='p';
      else if (c=='w')c='f';
      else if (c=='x')c='m';
      else if (c=='y')c='a';
      else if (c=='z')c='q'; // or i
      cout << c;      
      outfile << c;
      infile.get(c);
      }
      cout << endl;
      outfile << endl;
    }
    infile.close();
    outfile.close();
cin.ignore();
}
