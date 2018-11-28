#include <iostream>
using namespace std;

string T = "yhesocvxduiglbkrztnwjpfmaq";

int
main()
{
  char buf[128];

  int n; cin>>n;
  cin.getline(buf, sizeof(buf));
  for(int i = 0; i < n; i++){

    cin.getline(buf, sizeof(buf));

    string s = buf;
    for(int j = 0; j < s.size(); j++){
      if(s[j] == ' ') continue;
      s[j] = T[s[j]-'a'];
    }

    cout<<"Case #"<<i+1<<": "<<s<<endl;
  }

}
