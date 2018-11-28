#include<iostream>  
#include<string>
using namespace std;
int main(){   
   freopen("A-small-attempt4.in","r",stdin);
   freopen("a.out","w",stdout);
   int n,i,j;
   cin>>n;
   cin.get();
   string cad;
   for(j=0;j<n;j++){
      getline(cin,cad);
      for(i=0;i<cad.length();i++){
         if(cad[i]=='a'){cad[i]='y';continue;}
         if(cad[i]=='b'){cad[i]='h';continue;}
         if(cad[i]=='c'){cad[i]='e';continue;}
         if(cad[i]=='d'){cad[i]='s';continue;}
         if(cad[i]=='e'){cad[i]='o';continue;}
         if(cad[i]=='f'){cad[i]='c';continue;}
         if(cad[i]=='g'){cad[i]='v';continue;}
         if(cad[i]=='h'){cad[i]='x';continue;}
         if(cad[i]=='i'){cad[i]='d';continue;}
         if(cad[i]=='j'){cad[i]='u';continue;}
         if(cad[i]=='k'){cad[i]='i';continue;}
         if(cad[i]=='l'){cad[i]='g';continue;}
         if(cad[i]=='m'){cad[i]='l';continue;}
         if(cad[i]=='n'){cad[i]='b';continue;}
         if(cad[i]=='o'){cad[i]='k';continue;}
         if(cad[i]=='p'){cad[i]='r';continue;}
         if(cad[i]=='q'){cad[i]='z';continue;}
         if(cad[i]=='r'){cad[i]='t';continue;}
         if(cad[i]=='s'){cad[i]='n';continue;}
         if(cad[i]=='t'){cad[i]='w';continue;}
         if(cad[i]=='u'){cad[i]='j';continue;}
         if(cad[i]=='v'){cad[i]='p';continue;}
         if(cad[i]=='w'){cad[i]='f';continue;}
         if(cad[i]=='x'){cad[i]='m';continue;}
         if(cad[i]=='y'){cad[i]='a';continue;}
         if(cad[i]=='z'){cad[i]='q';continue;}
      }
      cout<<"Case #"<<j+1<<": "<<cad<<endl;
   }
}
