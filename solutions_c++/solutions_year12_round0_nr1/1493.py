#include <iostream>
#include <string>
#include <cassert>
using namespace std;


string from=" qzejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv#";
string to=  " zqourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
string map="abcdefghijklmnopqrstuvwxyz";

//yhesocvxduiglbkrtnwjpfmaq

void translate(string &line) {
  for (int i=0; i<line.size(); ++i) {
    int j;
    for (j=0; from[j] != line[i] && from[j]!='#'; j++);
    if (from[j] == '#')
      cout<<"UGH: "<<line[i]<<endl;
    assert(from[j]!='#');
    line[i]=to[j];
    //    line[i] = map[line[i]-'a'];
  }
}

int main() {
  int T;
  string line;
  cin >> T;
  getline(cin,line);
  for (int X=1; X<= T; X++) {
    getline(cin,line);
    translate(line);
    cout << "Case #" << X << ": " << line << endl;
  }
  return 0;
}
