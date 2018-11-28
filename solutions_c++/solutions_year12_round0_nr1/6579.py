#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<stdio.h>
#include<string.h>


void main()
{clrscr();
 fstream file,writ;
 file.open("input.in", ios::in|ios::beg);
 writ.open("ans.txt", ios::out);
 int a;
 char str1[102],str2[102];
 file>>a;
 file.getline(str1,100);
 for(int b=1;b<=a;b++)
 {

 file.getline(str1,102);
 for(int i=0;i<=100;i++)
 {
  if(str1[i]== 'y')
	str2[i] = 'a';
  else if(str1[i]== 'n')
	str2[i] = 'b';
  else 	if(str1[i]== 'f')
	str2[i] = 'c';
	else if(str1[i]== 'i')
	str2[i] = 'd';
	else if(str1[i]== 'c')
	str2[i] = 'e';
	else if(str1[i]== 'w')
	str2[i] = 'f';
	else if(str1[i]== 'l')
	str2[i] = 'g';
	else if(str1[i]== 'b')
	str2[i] = 'h';
	else if(str1[i]== 'k')
	str2[i] = 'i';
	else if(str1[i]== 'u')
	str2[i] = 'j';
	else if(str1[i]== 'o')
	str2[i] = 'k';
	else if(str1[i]== 'm')
	str2[i] = 'l';
	else if(str1[i]== 'x')
	str2[i] = 'm';
	else if(str1[i]== 's')
	str2[i] = 'n';
  else 	if(str1[i]== 'e')
	str2[i] = 'o';
	else if(str1[i]== 'v')
	str2[i] = 'p';
	else if(str1[i]== 'z')
	str2[i] = 'q';
	else if(str1[i]== 'p')
	str2[i] = 'r';
	else if(str1[i]== 'd')
	str2[i] = 's';
	else if(str1[i]== 'r')
	str2[i] = 't';
	else if(str1[i]== 'j')
	str2[i] = 'u';
	else if(str1[i]== 'g')
	str2[i] = 'v';
  else 	if(str1[i]== 't')
	str2[i] = 'w';
  else 	if(str1[i]== 'h')
	str2[i] = 'x';
	else if(str1[i]== 'a')
	str2[i] = 'y';
	else if(str1[i]== 'q')
	str2[i] = 'z';
	else
	str2[i] = str1[i];

  }

  writ<<"Case #"<<b<<": "<<str2<<"\n";

  }
  
  }
