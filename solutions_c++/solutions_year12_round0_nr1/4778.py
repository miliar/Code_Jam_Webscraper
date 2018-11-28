#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream in("x.in");
    ofstream out("x.out");
    int a,i;
    char ch,cc;
    cc=10;
    in>>a;
    for(i=1;i<=a+1;i++)
    {
        if (i!=1) out<<"Case #"<<i-1<<": ";
        do{
            in>> noskipws >>ch;
            if (ch=='a') out<<"y";
            if (ch=='b') out<<"h";
            if (ch=='c') out<<"e";
            if (ch=='d') out<<"s";
            if (ch=='e') out<<"o";
            if (ch=='f') out<<"c";
            if (ch=='g') out<<"v";
            if (ch=='h') out<<"x";
            if (ch=='i') out<<"d";
            if (ch=='j') out<<"u";
            if (ch=='k') out<<"i";
            if (ch=='l') out<<"g";
            if (ch=='m') out<<"l";
            if (ch=='n') out<<"b";
            if (ch=='o') out<<"k";
            if (ch=='p') out<<"r";
            if (ch=='q') out<<"z";
            if (ch=='r') out<<"t";
            if (ch=='s') out<<"n";
            if (ch=='t') out<<"w";
            if (ch=='u') out<<"j";
            if (ch=='v') out<<"p";
            if (ch=='w') out<<"f";
            if (ch=='x') out<<"m";
            if (ch=='y') out<<"a";
            if (ch=='z') out<<"q";
            if (ch==' ') out<<" ";
            if (ch==10&&i!=1) out<<endl;
        }while (ch != cc);
    }
}
