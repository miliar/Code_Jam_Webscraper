#include<fstream.h>
#include<iostream.h>
main()
{
      ifstream f;
      ofstream o;
      int i,j,n;
      char a;
      f.open("A-small-attempt0.in");
      o.open("O.txt");
      f>>n;
      f.read((char*)&a,sizeof(a));
      for(i=0;i<n;i++)
      {
                      o<<"Case #"<<i+1<<": ";
                      do
                      {
                              f.read((char*)&a,sizeof(a));
                              if(a=='a')
                                        o<<'y';
                              else if(a=='b')
                                   o<<'h';
                              else if(a=='c')
                                   o<<'e';
                              else if(a=='d')
                                   o<<'s';
                              else if(a=='e')
                                   o<<'o';
                              else if(a=='f')
                                   o<<'c';
                              else if(a=='g')
                                   o<<'v';
                              else if(a=='h')
                                   o<<'x';
                              else if(a=='i')
                                   o<<'d';
                              else if(a=='j')
                                   o<<'u';
                              else if(a=='k')
                                   o<<'i';
                              else if(a=='l')
                                   o<<'g';
                              else if(a=='m')
                                   o<<'l';
                              else if(a=='n')
                                   o<<'b';
                              else if(a=='o')
                                   o<<'k';
                              else if(a=='p')
                                   o<<'r';
                              else if(a=='q')
                                   o<<'z';
                              else if(a=='r')
                                   o<<'t';
                              else if(a=='s')
                                   o<<'n';
                              else if(a=='t')
                                   o<<'w';
                              else if(a=='u')
                                   o<<'j';
                              else if(a=='v')
                                   o<<'p';
                              else if(a=='w')
                                   o<<'f';
                              else if(a=='x')
                                   o<<'m';
                              else if(a=='y')
                                   o<<'a';
                              else if(a=='z')
                                   o<<'q';
                              else
                                  o.write((char*)&a,sizeof(a));
                      }
                      while(a!='\n' && !(f.eof()));
      }
      f.close();
      o.close();
}
