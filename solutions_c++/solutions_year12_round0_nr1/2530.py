#include <iostream>
#include <string>
#include <cstdlib>
#include<cstdio>

using namespace std;

int main(){
int b;
scanf("%d",&b);
string aaa;
for(int j=0;j<b+1;j++){
getline(cin,aaa);
char a;
for(int i=0;i<aaa.length();i++){
a=aaa[i];
if(a=='a'){aaa[i]='y';
}else if(a=='b'){aaa[i]='h';
}else if(a=='c'){aaa[i]='e';
}else if(a=='d'){aaa[i]='s';
}else if(a=='e'){aaa[i]='o';
}else if(a=='f'){aaa[i]='c';
}else if(a=='g'){aaa[i]='v';
}else if(a=='h'){aaa[i]='x';
}else if(a=='i'){aaa[i]='d';
}else if(a=='j'){aaa[i]='u';
}else if(a=='k'){aaa[i]='i';
}else if(a=='l'){aaa[i]='g';
}else if(a=='m'){aaa[i]='l';
}else if(a=='n'){aaa[i]='b';
}else if(a=='o'){aaa[i]='k';
}else if(a=='p'){aaa[i]='r';
}else if(a=='q'){aaa[i]='z';
}else if(a=='r'){aaa[i]='t';
}else if(a=='s'){aaa[i]='n';
}else if(a=='t'){aaa[i]='w';
}else if(a=='u'){aaa[i]='j';
}else if(a=='v'){aaa[i]='p';
}else if(a=='w'){aaa[i]='f';
}else if(a=='x'){aaa[i]='m';
}else if(a=='y'){aaa[i]='a';
}else if(a=='z'){aaa[i]='q';
}
}
if(j!=0)
cout<<"Case #"<<j<<": "<<aaa;
if(j!=0 && j!=30)
cout<<endl;
}
return 0;
}
