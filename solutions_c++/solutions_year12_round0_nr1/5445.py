#include<iostream>
#include<string>
using namespace std;
int main(){
   char map[27];
   map[1]='y';
   map[2]='h';
   map[3]='e';
   map[4]='s';
   map[5]='o';
   map[6]='c';
   map[7]='v';
   map[8]='x';
   map[9]='d';
   map[10]='u';
   map[11]='i';
   map[12]='g';
   map[13]='l';
   map[14]='b';
   map[15]='k';
   map[16]='r';
   map[17]='z';
   map[18]='t';
   map[19]='n';
   map[20]='w';
   map[21]='j';
   map[22]='p';
   map[23]='f';
   map[24]='m';
   map[25]='a';
   map[26]='q';

   int times;
   string input;
   cin>>times;
   getchar();
   for(int i=0;i<times;i++){
     cout<<"Case #"<<i+1<<": ";
     getline(cin,input);
     for(int j=0;j<input.size();j++)
     {
       if(input[j]==' ')
          cout<<' ';
       else
        cout<<map[ input[j]-'a'+1];
     }
     cout<<endl;
   }
   return 0;

}
