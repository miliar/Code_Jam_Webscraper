#include<fstream>
#include<iostream>
#include <cstdlib>
using namespace std;
main()
{
int tc,j,i;
char ch[105];
char c;
ifstream f;ofstream f2;
f.open("C:/Turboc3/input.txt");
f2.open("C:/Turboc3/o.txt");
f >> tc;f.getline(ch,2);
for(int i=0;i<tc;i++) {
    //ch= NULL;
    f.getline(ch,102);
    cout << ch << "\n";
    for(j=0;j<strlen(ch);j++) {
        if(ch[j]=='a') ch[j]='y';
        else if(ch[j]=='b') ch[j]='h';
        else if(ch[j]=='c') ch[j]='e';
        else if(ch[j]=='d') ch[j]='s';
        else if(ch[j]=='e') ch[j]='o';
        else if(ch[j]=='f') ch[j]='c';
        else if(ch[j]=='g') ch[j]='v';
        else if(ch[j]=='h') ch[j]='x';
        else if(ch[j]=='i') ch[j]='d';
        else if(ch[j]=='j') ch[j]='u';
        else if(ch[j]=='k') ch[j]='i';
        else if(ch[j]=='l') ch[j]='g';
        else if(ch[j]=='m') ch[j]='l';
        else if(ch[j]=='n') ch[j]='b';
        else if(ch[j]=='o') ch[j]='k';
        else if(ch[j]=='p') ch[j]='r';
        else if(ch[j]=='q') ch[j]='z';
        else if(ch[j]=='r') ch[j]='t';
        else if(ch[j]=='s') ch[j]='n';
        else if(ch[j]=='t') ch[j]='w';
        else if(ch[j]=='u') ch[j]='j';
        else if(ch[j]=='v') ch[j]='p';
        else if(ch[j]=='w') ch[j]='f';
        else if(ch[j]=='x') ch[j]='m';
        else if(ch[j]=='y') ch[j]='a';
        else if(ch[j]=='z') ch[j]='q';
        
    }
    f2 << "Case #"<<i+1<<": "<<ch<<"\n";
}
f.close();
f2.close();
return 0;
}
