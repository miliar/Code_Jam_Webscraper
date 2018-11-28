#include<iostream>
#include<fstream>
#include<conio.h>
#include<string.h>
using namespace std;
int main()
{
    int n;
    char *s;
    char ch;
    ifstream fin;
    ofstream fout;
    fin.open("A.in",ios::in);
    fout.open("A.out",ios::out);
    fin>>n;
    for(int i = 0;i<=n;i++)
    {
        fin.getline(s,'/n');
        if (i ==0)
        continue;
        fout<<"Case #"<<i<<": ";

       for(int k = 0; k < strlen(s); k++)
        {
                
                            if(s[k]== 'a'){fout<<"y";}
                            if(s[k]== 'b'){fout<<"h";}
                            if(s[k]== 'c'){fout<<"e";}
                            if(s[k]== 'd'){fout<<"s";}
                            if(s[k]== 'e'){fout<<"o";}
                            if(s[k]== 'f'){fout<<"c";}
                            if(s[k]== 'g'){fout<<"v";}
                            if(s[k]== 'h'){fout<<"x";}
                            if(s[k]== 'i'){fout<<"d";}
                            if(s[k]== 'j'){fout<<"u";}
                            if(s[k]== 'k'){fout<<"i";}
                            if(s[k]== 'l'){fout<<"g";}
                            if(s[k]== 'm'){fout<<"l";}
                            if(s[k]== 'n'){fout<<"b";}
                            if(s[k]== 'o'){fout<<"k";}
                            if(s[k]== 'p'){fout<<"r";}
                            if(s[k]== 'q'){fout<<"z";}
                            if(s[k]== 'r'){fout<<"t";}
                            if(s[k]== 's'){fout<<"n";}
                            if(s[k]== 't'){fout<<"w";}
                            if(s[k]== 'u'){fout<<"j";}
                            if(s[k]== 'v'){fout<<"p";}
                            if(s[k]== 'w'){fout<<"f";}
                            if(s[k]== 'x'){fout<<"m";}
                            if(s[k]== 'y'){fout<<"a";}
                            if(s[k]== 'z'){fout<<"q";}
                            if(s[k]== ' '){fout<<" ";}
                           
                }
                fout<<endl;
            }
    getch();
    fin.close();
    fout.close();
    }
