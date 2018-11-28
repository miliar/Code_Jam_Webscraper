#include <vector>
#include <string>
#include <iostream>

using namespace std;
const string convert_table = "yhesocvxduiglbkrztnwjpfmaq";

int main(){
  std::ios_base::sync_with_stdio(false);
  int T;
  string dummy;
  cin >> T;
  getline(cin,dummy);
  cin.clear();
  for(int t=1;t<=T;t++){
    cout << "Case #" << t << ": ";
    string text;
    getline(cin,text);
    string result(100,' ');
    for(int i=0;i<text.size();i++){
      if(text[i] != ' '){
	result[i]=convert_table[text[i]-'a'];
      }
      cout << result[i];
      }
    cout << endl;
  }

  return 0;
}
