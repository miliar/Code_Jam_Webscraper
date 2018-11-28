#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
int main()
{
    int t,i;
    char s1[101],ch;
    ifstream in;
    ofstream out;
    out.open("out_a.txt");
    in.open("ina.txt");
    in>>t;
    in.get(ch);
    while(t--)
    {
         in.getline(s1,101);
         int l=strlen(s1);
         for(i=0;i<l;i++)
         {if(s1[i]=='a')
         s1[i]='y';
         else if(s1[i]=='b')
         s1[i]='h';
         else if(s1[i]=='c')
         s1[i]='e';
         else if(s1[i]=='d')
         s1[i]='s';
         else if(s1[i]=='e')
         s1[i]='o';
         else if(s1[i]=='f')
         s1[i]='c';
         else if(s1[i]=='g')
         s1[i]='v';
         else if(s1[i]=='h')
         s1[i]='x';
         else if(s1[i]=='i')
         s1[i]='d';
         else if(s1[i]=='j')
         s1[i]='u';
         else if(s1[i]=='k')
         s1[i]='i';
         else if(s1[i]=='l')
         s1[i]='g';
         else if(s1[i]=='m')
         s1[i]='l';
         else if(s1[i]=='n')
         s1[i]='b';
         else if(s1[i]=='o')
         s1[i]='k';
         else if(s1[i]=='p')
         s1[i]='r';
         else if(s1[i]=='q')
         s1[i]='z';
         else if(s1[i]=='r')
         s1[i]='t';
         else if(s1[i]=='s')
         s1[i]='n';
         else if(s1[i]=='t')
         s1[i]='w';
         else if(s1[i]=='u')
         s1[i]='j';
         else if(s1[i]=='v')
         s1[i]='p';
         else if(s1[i]=='w')
         s1[i]='f';
         else if(s1[i]=='x')
         s1[i]='m';
         else if(s1[i]=='y')
         s1[i]='a';
         else if(s1[i]=='z')
         s1[i]='q';
         }
        out<<"Case #"<<(30-t)<<": "<<s1<<endl;

    }
    in.close();
    out.close();
    return 0;
}
