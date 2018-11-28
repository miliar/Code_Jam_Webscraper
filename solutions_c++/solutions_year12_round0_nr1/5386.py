//---------------------------------------------------------------------------
#include<iostream>
#include<fstream>

#pragma hdrstop

using namespace std;
//---------------------------------------------------------------------------

#pragma argsused
int main(int argc, char* argv[])
{
int n, i=0;
string *str;
char *array = new char[256];
//ifstream fin("input.txt");
array['a'] = 'y';array['b'] = 'h';
array['c'] = 'e';array['d'] = 's';
array['e'] = 'o';array['f'] = 'c';
array['g'] = 'v';array['h'] = 'x';
array['i'] = 'd';array['j'] = 'u';
array['k'] = 'i';array['l'] = 'g';
array['m'] = 'l';array['n'] = 'b';
array['o'] = 'k';array['p'] = 'r';
array['q'] = 'z';array['r'] = 't';
array['s'] = 'n';array['t'] = 'w';
array['u'] = 'j';array['v'] = 'p';
array['w'] = 'f';array['x'] = 'm';
array['y'] = 'a';array['z'] = 'q';
array[' '] = ' ';

cin>>n;
string s;
//getline(fin, s, '\n');
//n = atoi(s.c_str());
str = new string[n];
getline(cin,str[0]);
getline(cin,str[0]);
for(i=1; i<n; ++i){
  getline(cin, str[i]);
 // getline(fin, str[i], '\n');
  //fscanf (f1,"%c",&str[i]);
}
for(i = 0; i<n; i++){
   cout<<"Case #"<<i+1<<": ";
  for(int j=0; j<str[i].length(); j++){
  string s (str[i]);
     cout<<array[s[j]];
  }
  cout<<endl;
}
  system("PAUSE");
  return 0;
}
//---------------------------------------------------------------------------

