#include<iostream.h>
#include<stdio.h>
#include<conio.h>


char tr(char a)

{
 switch(a)

 {
  case 'a':  return 'y'  ;
  case 'b':  return 'h'  ;
  case 'c':  return 'e'  ;
  case 'd':  return 's'  ;
  case 'e':  return 'o'  ;
  case 'f':  return 'c'  ;
  case 'g':  return 'v'  ;
  case 'h':  return 'x'  ;
  case 'i':  return 'd'  ;
  case 'j':  return 'u'  ;
  case 'k':  return 'i'  ;
  case 'l':  return 'g'  ;
  case 'm':  return 'l'  ;
  case 'n':  return 'b'  ;
  case 'o':  return 'k'  ;
  case 'p':  return 'r'  ;
  case 'q':  return 'z'  ;
  case 'r':  return 't'  ;
  case 's':  return 'n'  ;
  case 't':  return 'w'  ;
  case 'u':  return 'j'  ;
  case 'v':  return 'p'  ;
  case 'w':  return 'f'  ;
  case 'x':  return 'm'  ;
  case 'y':  return 'a'  ;
  case 'z':  return 'q'  ;
 default : return a;
 }


}



void main()
{

	int t,i=0;
	char str[5000];


	int count=0;
	cin>>t;
	while(t--)

	{
	gets(str);
	i=0;
	cout<<"Case #"<<++count<<": ";

	while(str[i])
	{
	   cout<<tr(str[i++]);

	}
	cout<<endl;

	}

}

