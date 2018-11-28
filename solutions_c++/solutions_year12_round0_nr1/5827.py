#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>

#define ll long long
using namespace std;

char trans[] = "yhesocvxduiglbkrztnwjpfmaq";
////////////////abcdefghijklmnopqrstuvwxyz
                             // ?
int main(void)
{
  freopen("g:\\input.txt", "rt", stdin);
  freopen("g:\\output.txt", "wt", stdout);


  int c;
  scanf("%d ", &c);

  string str;
  
  for(int i=0; i<c; i++)
  {
    // bool test = false;

    cout<<"Case #"<<i+1<<": ";
    
    getline(cin, str);

    for(int j=0; j<str.length(); j++)
    {
      if(str[j] == ' ') {
        cout<<' ';
        continue;
      }
      if(str[j] == '\n') {
        break;
      }

      cout<<trans[str[j]-'a'];
    }

    cout<<endl;
  }

  return 0;
}