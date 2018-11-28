#include <fstream>
#include <iostream>
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>


using namespace std;
int main()
{ ifstream ifl;
ifl.open("as.in");
ofstream of;
of.open("out.txt");

char ch;
ifl.get(ch);

int n1=ch-48;

ifl.get(ch);
if(ch!='\n') { n1=n1*10+(ch-48);
ifl.get(ch);
}



cout<<n1;



char co;

for(int i=0;i<n1;++i)
{	of<<"Case #"<<i+1<<": ";
 for(int j=0;j<100;++j)
{   ifl.get(co);
cout<<co;

  if(co!='\n'){

	if(co=='a') co='y';
  else if(co=='b') co='h';
  else if(co=='c') co='e';
  else if(co=='d') co='s';
  else if(co=='e') co='o';
  else if(co=='f') co='c';
  else if(co=='g') co='v';
  else if(co=='h') co='x';
  else if(co=='i') co='d';
  else if(co=='j') co='u';
  else if(co=='k') co='i';
  else if(co=='l') co='g';
  else if(co=='m') co='l';
  else if(co=='n') co='b';
  else if(co=='o') co='k';
  else if(co=='p') co='r';
  else if(co=='q') co='z';
  else if(co=='r') co='t';
  else if(co=='s') co='n';
  else if(co=='t') co='w';
  else if(co=='u') co='j';
  else if(co=='v') co='p';
  else if(co=='w') co='f';
  else if(co=='x') co='m';
  else if(co=='y') co='a';
  else if(co=='z') co='q';
  
}
else{ if(i<n1-1) of<<"\n";
	break;
}

of<<co;
if(j==99){ ifl.get(co);   of<<"\n";
}


}
}
















}