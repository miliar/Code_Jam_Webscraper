#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{   int i,j,l,t;
    ifstream fin;
    ofstream fout;
    string str;
    fin.open("A-small-attempt0.in");
    fout.open("Output.txt");
    
    fin>>t;
    getline(fin,str);
    
    for(j=1;j<=t;j++)
    {
                getline(fin,str);
                l=str.length();
                
                for(i=0;i<str.length();i++)
                {
                                           switch(str.at(i))
                                           {
                                                            case 'y':str.at(i)='a';
                                                                     break;
                                                            case 'n':str.at(i)='b';
                                                                     break;
                                                            case 'f':str.at(i)='c';
                                                                     break;
                                                            case 'i':str.at(i)='d';
                                                                     break;
                                                            case 'c':str.at(i)='e';
                                                                     break;
                                                            case 'w':str.at(i)='f';
                                                                     break;
                                                            case 'l':str.at(i)='g';
                                                                     break;
                                                            case 'b':str.at(i)='h';
                                                                     break;
                                                            case 'k':str.at(i)='i';
                                                                     break;
                                                            case 'u':str.at(i)='j';
                                                                     break;
                                                            case 'o':str.at(i)='k';
                                                                     break;
                                                            case 'm':str.at(i)='l';
                                                                     break;
                                                            case 'x':str.at(i)='m';
                                                                     break;
                                                            case 's':str.at(i)='n';
                                                                     break;
                                                            case 'e':str.at(i)='o';
                                                                     break;
                                                            case 'v':str.at(i)='p';
                                                                     break;
                                                            case 'z':str.at(i)='q';
                                                                     break;
                                                            case 'p':str.at(i)='r';
                                                                     break;
                                                            case 'd':str.at(i)='s';
                                                                     break;
                                                            case 'r':str.at(i)='t';
                                                                     break;
                                                            case 'j':str.at(i)='u';
                                                                     break;
                                                            case 'g':str.at(i)='v';
                                                                     break;
                                                            case 't':str.at(i)='w';
                                                                     break;
                                                            case 'h':str.at(i)='x';
                                                                     break;
                                                            case 'a':str.at(i)='y';
                                                                     break;
                                                            case 'q':str.at(i)='z';
                                                                     break;
                                           }
                                           
                }
                fout<<"Case #"<<j<<": "<<str<<"\n";
    }
                return 0;
    }
                                                            
                                                            
