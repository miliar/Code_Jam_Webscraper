#include <fstream>

main()

{
      using namespace std;
long a,b=1; char x[1000];
ifstream I("input.txt");
ofstream O("output.txt");
I>>a;
I.getline (x,sizeof(x));
for(int i=0;i<a;i++){
        I.getline (x,sizeof(x));
        
         for(int j=0;j<sizeof(x);j++){
                 if(x[j]=='a') x[j]='y';
                else if(x[j]=='b') x[j]='h';
                else if(x[j]=='c') x[j]='e';
                else if(x[j]=='d') x[j]='s';
                else if(x[j]=='e') x[j]='o';
                else if(x[j]=='f') x[j]='c';
                else if(x[j]=='g') x[j]='v';
                else if(x[j]=='h') x[j]='x';//А может и нет
                else if(x[j]=='i') x[j]='d';
                else if(x[j]=='j') x[j]='u';
                else if(x[j]=='k') x[j]='i';
                else if(x[j]=='l') x[j]='g';
                else if(x[j]=='m') x[j]='l';
                else if(x[j]=='n') x[j]='b';
                else if(x[j]=='o') x[j]='k';
                else if(x[j]=='p') x[j]='r';
                else if(x[j]=='q') x[j]='z';//Возможно
                else if(x[j]=='r') x[j]='t';
                else if(x[j]=='s') x[j]='n';
                else if(x[j]=='t') x[j]='w';
                else if(x[j]=='u') x[j]='j';
                else if(x[j]=='v') x[j]='p';
                else if(x[j]=='w') x[j]='f';
                else if(x[j]=='x') x[j]='m';
                else if(x[j]=='y') x[j]='a';
                else if(x[j]=='z') x[j]='q';//Скорее всего     
                }           
                
        O<<"Case #"<<b<<':'<<' '<<x<<endl;b++;}
        }
