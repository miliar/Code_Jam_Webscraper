#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>

using namespace std;

int main(){
  int T;
  char abc[200], str[200];
  const char *conv = "yhesocvxduiglbkrztnwjpfmaq";
  gets(abc);
  T = atoi(abc);
  for(int i = 1; i <= T; i++){
    gets(str);
    int len = strlen(str);
    for(int j = 0; j < len; j++) if(str[j] >= 'a') str[j] = conv[str[j]-'a'];
    cout << "Case #" << i << ": " << str << endl;
  }
  return 0;
}
