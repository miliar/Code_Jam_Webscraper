#include<iostream>
#include<fstream>

using namespace std;

int main(){
    
    fstream fi;
    ofstream fo;
    char a;
    int i,num=0,j=1;
    string str;
    fi.open("A-small-attempt2.in");
    fo.open("res.txt");
    fi>>num;
    while(num>=0)
    { 
     getline(fi, str);
     
     i=0;
     while(str[i]!='\0'){
    a=str[i];                
    if(a=='a')a='y';
    else if(a=='b')a='h';
    else if(a=='c')a='e';
    else if(a=='d')a='s';
    else if(a=='e')a='o';
    else if(a=='f')a='c';
    else if(a=='g')a='v';
    else if(a=='h')a='x';
    else if(a=='i')a='d';
    else if(a=='j')a='u';
    else if(a=='k')a='i';
    else if(a=='l')a='g';
    else if(a=='m')a='l';
    else if(a=='n')a='b';
    else if(a=='o')a='k';
    else if(a=='p')a='r';
    else if(a=='q')a='z';
    else if(a=='r')a='t';
    else if(a=='s')a='n';
    else if(a=='t')a='w';
    else if(a=='u')a='j';
    else if(a=='v')a='p';
    else if(a=='w')a='f';
    else if(a=='x')a='m';
    else if(a=='y')a='a';
    else if(a=='z')a='q';
     fo<<a;i++;}
      fo<<'\n';
      if(num!=0)
      fo<<"Case #"<<j<<": ";
      j++;
     num--;
                   }
    system("pause");
}
