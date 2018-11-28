#include<iostream>
#include<string>
using namespace std;

char solve(char a);

int main(){
  int cnt;
  scanf("%d ",&cnt);
  for(int i=0;i<cnt;i++){
    string s;
    getline(cin,s);
    cout<<"Case #"<<i+1<<": ";
    for(int j=0;j<s.size();j++){
      cout<<solve(s[j]);
    }
    cout<<endl;
  }
  return 0;
}

char solve(char a){
  if(a==' ')return ' ';
  else if(a=='a')return 'y';
  else if(a=='b')return 'h';
  else if(a=='c')return 'e';
  else if(a=='d')return 's';
  else if(a=='e')return 'o';
  else if(a=='f')return 'c';
  else if(a=='g')return 'v';
  else if(a=='h')return 'x';
  else if(a=='i')return 'd';
  else if(a=='j')return 'u';
  else if(a=='k')return 'i';
  else if(a=='l')return 'g';
  else if(a=='m')return 'l';
  else if(a=='n')return 'b';
  else if(a=='o')return 'k';
  else if(a=='p')return 'r';
  else if(a=='q')return 'z';
  else if(a=='r')return 't';
  else if(a=='s')return 'n';
  else if(a=='t')return 'w';
  else if(a=='u')return 'j';
  else if(a=='v')return 'p';
  else if(a=='w')return 'f';
  else if(a=='x')return 'm';
  else if(a=='y')return 'a';
  else if(a=='z')return 'q';
}
