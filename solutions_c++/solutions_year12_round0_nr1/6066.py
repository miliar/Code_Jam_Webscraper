#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
int main()
{
    ifstream in;
    in.open("A-small-attempt0.in");
    string s;
    ofstream out;
    out.open("out.txt");
    int t;
    getline(in,s);
    t=0;
    in.clear();
              
              while( getline (in,s))
              {
                               t++;
                              out<<"Case #"<<t<<": ";
                    for(int j=0;j<s.length();j++)
                    {
                      if(s[j]=='a')
                      out<<'y';
                      if(s[j]=='b')
                      out<<'h';
                      if(s[j]=='c')
                      out<<'e';
                      if(s[j]=='d')
                      out<<'s';
                      if(s[j]=='e')
                      out<<'o';
                      if(s[j]=='f')
                      out<<'c';
                      if(s[j]=='g')
                      out<<'v';
                      if(s[j]=='h')
                      out<<'x';
                      if(s[j]=='i')
                      out<<'d';
                      if(s[j]=='j')
                      out<<'u';
                      if(s[j]=='k')
                      out<<'i';
                      if(s[j]=='l')
                      out<<'g';
                      if(s[j]=='m')
                      out<<'l';
                      if(s[j]=='n')
                      out<<'b';
                      if(s[j]=='o')
                      out<<'k';
                      if(s[j]=='p')
                      out<<'r';
                      if(s[j]=='q')
                      out<<'z';
                      if(s[j]=='r')
                      out<<'t';
                      if(s[j]=='s')
                      out<<'n';
                      if(s[j]=='t')
                      out<<'w';
                      if(s[j]=='u')
                      out<<'j';
                      if(s[j]=='v')
                      out<<'p';
                      if(s[j]=='w')
                      out<<'f';
                      if(s[j]=='x')
                      out<<'m';
                      if(s[j]=='y')
                      out<<'a';
                      if(s[j]=='z')
                      out<<'q';
                      if(s[j]==' ')
                      out<<' ';
                    }
              out<<endl;
             
              
    }
    out.close();
              in.close();
             // cin>>t;
    return 0;
}
