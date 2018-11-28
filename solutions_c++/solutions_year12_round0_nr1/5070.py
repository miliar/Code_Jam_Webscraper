#include <cstdio>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

char f[30];

int set(string a,string b){
  for(int i=0;i<a.size();i++){
    if(a[i] == ' ') continue;
    f[a[i]-'a'] = b[i];
  }
}

string get(string a){
  for(int i=0;i<a.size();i++){
    if(a[i] == ' ') continue;
    a[i] = f[a[i]-'a'];
  }
  return a;
}

int main(){
  
  set("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand");
  set("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
  set("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
  f['z'-'a'] = 'q';
  f['q'-'a'] = 'z';
  
//  for(int i=0;i<30;i++){
//    char c = i+'a';
//    cout << c << ": " << f[i] << endl;
//  }
//  getchar();
  freopen("A2.in","r",stdin);
  freopen("A2.out","w",stdout);

  int n;
  string line;
  getline(cin,line);
  stringstream ss(line);
  ss >> n;

  for(int ncase=1;ncase<=n;ncase++){
    string line;
    getline(cin,line);
    string out = get(line);
    cout << "Case #" << ncase << ": " << out << endl;
  }
  
  return 0;
}
