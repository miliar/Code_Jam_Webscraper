#include<iostream>
#include<conio.h>
#include<fstream>

using namespace std;

char change(char c)
{
            
   if(c==' ')
     return ' ';
   switch(c) 
   {
         case 'a':c='y';
                  break;
         case 'b':c='h';
                  break;
         case 'c':c='e';
                  break;
         case 'd':c='s';
                  break;
         case 'e':c='o';
                  break;
         case 'f':c='c';
                  break;
         case 'g':c='v';
                  break;
         case 'h':c='x';
                  break;
         case 'i':c='d';
                  break;
         case 'j':c='u';
                  break;
         case 'k':c='i';
                  break;
         case 'l':c='g';
                  break;
         case 'm':c='l';
                  break;
         case 'n':c='b';
                  break;
         case 'o':c='k';
                  break;
         case 'p':c='r';
                  break;
         case 'q':c='z';
                  break;
         case 'r':c='t';
                  break;
         case 's':c='n';
                  break;
         case 't':c='w';
                  break;
         case 'u':c='j';
                  break;
         case 'v':c='p';
                  break;
         case 'w':c='f';
                  break;
         case 'x':c='m';
                  break;
         case 'y':c='a';
                  break;
         case 'z':c='q';
                  break;
         }
       return c;
}
int main()
{
    char l[1000],s[1000],a[1000][1000];
    int i=0,j=0,t=0,c=0,n=0;
    fstream fin,fout;
    fin.open("A-small-attempt7.in",ios::in);
    fout.open("A-small.txt",ios::out);
    while(!fin.eof())
    {
                   fin.getline(l,1000);
                   if(c==0)
                   {
                           for(i=0;l[i]!='\0';i++)
                           {
                                 n=n*10+(l[i]-48);          
                           }
                           c=1;
                   }
                   else
                   {
                     j=0;
                     for(i=0;l[i]!='\0';i++)
                     {
                           s[j++]=change(l[i]);
                           s[j]='\0';                       
                     }
                     strcpy(a[t++],s);
                   }
    }
    for(i=0;i<n;i++)
    {
                 cout<<"Case #"<<i+1<<": "<<a[i]<<endl;
                 fout<<"Case #"<<i+1<<": "<<a[i]<<endl;    
    }    
    fout.close();
    getch();   
    return 0;
    }
