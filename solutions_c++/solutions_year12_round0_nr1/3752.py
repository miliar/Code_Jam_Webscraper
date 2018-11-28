#include<iostream>
#include<string>
#include<algorithm>
#include<cstdio>
using namespace std;

int main()
{
  int n;
string str;
  cin >> n;
  
  getchar();
  for(int i=0;i<n;i++){
    getline(cin,str);
    for(int j=0;j<str.length();j++){
      switch(str[j]){

   case 'e' : str[j]='o';
              break;
              
   case 'j' : str[j]='u';
              break;
              
case 'p' : str[j]='r';
break;

case 'm' : str[j]='l';
break;
case 'y' : str[j]='a';
break;
case 's' : str[j]='n';
break;
case 'l' : str[j]='g';
break;
case 'c' : str[j]='e';
break;
case 'k' : str[j]='i';
break;
case 'd' : str[j]='s';
break;
case 'x' : str[j]='m';
break;
case 'v' : str[j]='p';
break;
case 'r' : str[j]='t';
break;
case 'z' : str[j]='q';
break;
case 'b' : str[j]='h';
break;
case 'n' : str[j]='b';
break;
case 'w' : str[j]='f';
break;
case 'a'  : str[j]='y';
break;
case 't'  : str[j]='w';
break;
case 'g' : str[j]='v';
break;
case 'o' : str[j]='k';
break;
case 'i' : str[j]='d';
break;
case 'u' : str[j]='j';
break;
case 'q' : str[j]='z';
break;
case 'f' : str[j]='c';
break;
case 'h' : str[j]='x';
break;

      }
    }
cout <<"Case #"<<i+1<<": "<<str<<endl;
}
return 0;
}
