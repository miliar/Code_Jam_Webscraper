#include<iostream>
#include<string>
using namespace std;
int main(){
char getChar(char);
int t;
string given;
cin>>t;
getline(cin,given);
for(int i=0;i<t;++i){
        
        string ret="";
        getline(cin,given);
        //cout<<given<<endl;
        for(int j=0;j<given.length();++j){
                ret+=getChar(given[j]);
        }
        
        cout<<"Case #"<<i+1<<": "<<ret<<endl;
}
}
char getChar(char c){
     char sp;
     switch(c){
               case 'a':
                    sp='y';
                    break;
               case 'b':
                    sp='h';
                    break;
               case 'c':
                    sp='e';
                    break;
               case 'd':
                    sp='s';
                    break;
               case 'e':
                    sp='o';
                    break;
               case 'f':
                    sp='c';
                    break;
               case 'g':
                    sp='v';
                    break;
               case 'h':
                    sp='x';
                    break;
               case 'i':
                    sp='d';
                    break;
               case 'j':
                    sp='u';
                    break;
               case 'k':
                    sp='i';
                    break;
               case 'l':
                    sp='g';
                    break;
               case 'm':
                    sp='l';
                    break;
               case 'n':
                    sp='b';
                    break;
               case 'o':
                    sp='k';
                    break;
               case 'p':
                    sp='r';
                    break;
               case 'q':
                    sp='z';
                    break;
               case 'r':
                    sp='t';
                    break;
               case 's':
                    sp='n';
                    break;
               case 't':
                    sp='w';
                    break;
               case 'u':
                    sp='j';
                    break;
               case 'v':
                    sp='p';
                    break;
               case 'w':
                    sp='f';
                    break;
               case 'x':
                    sp='m';
                    break;
               case 'y':
                    sp='a';
                    break;
               case 'z':
                    sp='q';
                    break;
               case ' ':
                    sp=' ';
                    break;
               
     };     
     return sp;
}
