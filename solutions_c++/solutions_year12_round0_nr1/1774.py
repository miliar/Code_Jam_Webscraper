#include<iostream>
#include<string>
using namespace std;

main() {
  char x[30] = "yhesocvxduiglbkrztnwjpfmaq";
  int n;
  cin>>n;
  string str;
  getline(cin, str); //input empty line
  for (int i = 0; i < n; i++) {
    getline(cin, str);
    for (int j = 0; j < str.length(); j++) {
      if (isalpha(str[j])) {
	str[j] = x[str[j] - 'a'];
      }
    }
    cout<<"Case #"<<i+1<<": "<<str<<endl;
  }
}       
