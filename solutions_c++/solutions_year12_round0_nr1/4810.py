#include<iostream>
#include<string>
#include<fstream>
using namespace std;


int main()
{
    char ch;
        
    int num_test;
    int i = 1;
    
    ifstream fin ("A-small-attempt0.in");
    ofstream fout ("output.txt");
    
    fin>>num_test;
    fin.get();
    
    while(i<=num_test)
    {
        bool flag=1;
        fout<<"Case #"<<i<<": ";
        
        while(flag)
        {
            fin.get (ch);
            switch((int)ch)
            {
                case '\n' :
                    fout<<"\n";flag = 0;break;
                case ' ' :
                    fout<<" ";break;
                case 'a' :
                    fout<<"y";break;
                case 'b' :
                    fout<<"h";break;
                case 'c' :
                    fout<<"e";break;
                case 'd' :
                    fout<<"s";break;
                case 'e' :
                    fout<<"o";break;
                case 'f' :
                    fout<<"c";break;
                case 'g' :
                    fout<<"v";break;
                case 'h' :
                    fout<<"x";break;
                case 'i' :
                    fout<<"d";break;
                case 'j' :
                    fout<<"u";break;
                case 'k' :
                    fout<<"i";break;
                case 'l' :
                    fout<<"g";break;
                case 'm' :
                    fout<<"l";break;
                case 'n' :
                    fout<<"b";break;
                case 'o' :
                    fout<<"k";break;
                case 'p' :
                    fout<<"r";break;
                case 'q' :
                    fout<<"z";break;
                case 'r' :
                    fout<<"t";break;
                case 's' :
                    fout<<"n";break;
                case 't' :
                    fout<<"w";break;
                case 'u' :
                    fout<<"j";break;
                case 'v' :
                    fout<<"p";break;
                case 'w' :
                    fout<<"f";break;
                case 'x' :
                    fout<<"m";break;
                case 'y' :
                    fout<<"a";break;
                case 'z' :
                    fout<<"q";break;
            }
        }
        i++;
    }
}
