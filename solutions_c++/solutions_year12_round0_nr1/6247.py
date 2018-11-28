#include<iostream.h>
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<fstream.h>
void main()
{ clrscr();
  fstream file1,file2 ;
  char ch[100];
  int ntc;
  file1.open("input.in",ios::in);
  file2.open("output.out",ios::out);

  while(!file1.eof())
  {
    char ip[100];
    file1.getline(ip,100,'\n');
    int ntc = atoi(ip);
    if(ntc >1 && ntc <=30)
    {

    for(int i=1;i<=ntc;i++)
    {
      file2<<"Case #"<<i<<": ";
      char ch;
      file1.get(ch);
      int count=1;
      while(ch != '\n')
       {


	 switch(ch)
	      {
	    case 'a' : ch='y';
		      file2.put(ch);
		      break;
	    case 'b' : ch='h';
		      file2.put(ch);
		      break;
	    case 'c' : ch='e';
		      file2.put(ch);
		      break;
	    case 'd' : ch='s';
		      file2.put(ch);
		      break;
	    case 'e' : ch='o';
		      file2.put(ch);
		      break;
	    case 'f' : ch='c';
		      file2.put(ch);
		      break;
	    case 'g' : ch='v';
		      file2.put(ch);
		      break;
	    case 'h' : ch='x';
		      file2.put(ch);
		      break;
	    case 'i' : ch='d';
		      file2.put(ch);
		      break;
	    case 'j' : ch='u';
		      file2.put(ch);
		      break;
	    case 'k' : ch='i';
		      file2.put(ch);
		      break;
	    case 'l' : ch='g';
		      file2.put(ch);
		      break;
	    case 'm' : ch='l';
		      file2.put(ch);
		      break;
	    case 'n' : ch='b';
		      file2.put(ch);
		      break;
	    case 'o' : ch='k';
		      file2.put(ch);
		      break;
	    case 'p' : ch='r';
		      file2.put(ch);
		      break;
	    case 'q' : ch='z';
		      file2.put(ch);
		      break;
	    case 'r' : ch='t';
		      file2.put(ch);
		      break;
	    case 's' : ch='n';
		      file2.put(ch);
		      break;
	    case 't' : ch='w';
		      file2.put(ch);
		      break;
	    case 'u' : ch='j';
		      file2.put(ch);
		      break;
	    case 'v' : ch='p';
		      file2.put(ch);
		      break;
	    case 'w' : ch='f';
		      file2.put(ch);
		      break;
	    case 'x' : ch='m';
		      file2.put(ch);
		      break;
	    case 'y' : ch='a';
		      file2.put(ch);
		      break;
	    case 'z' : ch='q';
		      file2.put(ch);
		      break;
	    default: ch=' ';
		    file2.put(ch);

	}
	file1.get(ch);
	count++;
	if(ch =='\n')
	  file2<<"\n";

     }
     if(file1.eof())
      {cout<<"unexpected end of file";
       exit(0);
      }
    }
   }
 }
  file1.close();
  file2.close();
}