#include <cstring>
#include <string>
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cassert>

using namespace std;

string st;
char mapping[] = "yhesocvxduiglbkrztnwjpfmaq";

int main(){
   int tcase; cin>>tcase; getline(cin,st);  
   for(int tc=1; tc<=tcase; ++tc){
      getline(cin,st); printf("Case #%d: ",tc);
      for(int j=0; j<st.length(); ++j){
           if(st[j]==' ') putchar(' ');
           else putchar(mapping[st[j]-'a']);
      }
      putchar('\n'); 
   }
   return 0;
}
