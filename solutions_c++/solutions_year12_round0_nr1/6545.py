#include<iostream>
#include<conio.h>
#include<string>
#include<stdio.h>
#include<fstream.h>
#include<ctype.h>


using namespace std;

fstream f1,f2;

int main()
{int i=0,co=0 ,l,x;
char s[200], r[200];
char c;
f1.open("d.in",ios::in);
f2.open("output.out",ios::out);
f1>>x;

while(f1)
{

f1.get(c);
if(c=='\n')
break;
            }
           
while(f1)
{f1.getline(s,200,'\n');
co++;
l=strlen(s);


for(i=0;i<l;i++)
{c=s[i];
switch(c)
{case 'a':
      r[i]='y';
break;
case 'b':
     r[i]='h';
break;
      case 'c':
           r[i]='e';
break;
case 'd':
     r[i]='s';
break;
      case 'e':
           r[i]='o';
           break;
           case 'f':
                r[i]='c';
                break;
                case 'g':
                     r[i]='v';
                     break;
                     case 'h':
                          r[i]='x';
                          break;
                          case 'i':
                               r[i]='d';
                               break;
                               case 'j':
                                    r[i]='u';
                                    break;
                                    case 'k':
                                    r[i]='i';
                                    break;
                                    case'l':
                                            r[i]='g';
                                            break;
                                            case 'm':
                                                 r[i]='l';
                                                 break;
                                                 case 'n':
                                                      r[i]='b';
                                                      break;
                                                      case 'o':
                                                           r[i]='k';
                                                           break;
                                                           case 'p':
                                                           r[i]='r';
                                                           break;
                                                           case 'q':
                                                                r[i]='z';
                                                                break;
                                                                case 'r':
                                                                     r[i]='t';
                                                                     break;
                                                                     case 's':
                                                                          r[i]='n';
                                                                          break;
                                                                          case 't':
                                                                               r[i]='w';
                                                                               break;
                                                                               case 'u':
                                                                                    r[i]='j';
                                                                                    break;
                                                                                    case 'v':
                                                                                         r[i]='p';
                                                                                         break;
                                                                                         case 'w':
                                                                                              r[i]='f';
                                                                                                       break;
                                                                                                       case 'x':
                                                                                                            r[i]='m';
                                                                                                            break;
                                                                                                             case 'y':
                                                                                                                  r[i]='a';
                                                                                                                  break;
                                                                                                                  case 'z':
                                                                                                                       r[i]='q';
                                                                                                                       break;
                                                                                                                       case ' ':
                                                                                                                            r[i]=' ';
                                                                                                                            break;
                                                                                                                            }
                                                                                                                            }
                                                                                                                            
                                                                                                                            
                                                                                                                      
r[l]='\0'; 

     
if(co<=x)

{
f2<<"Case #";
f2<<co;
f2<<": ";
for(i=0;i<l;i++)
f2.put(r[i]);

f2<<"\n";
}

}
getch();
}

