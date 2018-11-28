#include<iostream>
using namespace std;

string base,replace;
int alph[26];
string setA[3]={
  "ejp mysljylc kd kxveddknmc re jsicpdrysi",
  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
  "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
string setB[3]={
  "our language is impossible to understand",
  "there are twenty six factorial possibilities",
  "so it is okay if you want to just give up"};


int init(){
  alph['z' - 'a']='q'-'a';
  alph['q' - 'a']='z'-'a';
  for(int i=0 ; i<3 ; i++)
    for(int j=0 ; j<setA[i].size() ; j++)
      if(setA[i][j]!=' ')alph[(int)(setA[i][j]-'a')] = (int)(setB[i][j]-'a');
  return 0;
}

int solve(int x){
  cout << "Case #" << x+1 << ": ";
  for(int i=0 ; i<base.size() ; i++)
    if(base[i]==' ')cout << ' ';
    else{
      int a = base[i]-'a';
      cout << (char)('a' + alph[a]);
    }
  cout << endl;
  return 0;
}

int main(){
  init();
  int n;
  cin >> n;
  getline(cin,base);
  for(int i=0 ; i<n ; i++){
    getline(cin,base);
    solve(i);
  }
  return 0;
}
