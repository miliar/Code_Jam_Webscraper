#include <iostream>
using namespace std;

int main()
{
  int i, j, t, l;
  char str[31][101];
  //           = "abcdefghijklmnopqrstuvwxyz"
  char map[27] = "yhesocvxduiglbkrztnwjpfmaq";
  cin>>t;

  for(i=0; i<t+1; i++)
  {
    cin.getline(str[i], 101); 
    //cout<<str[];
    l = strlen(str[i]);
    for(j=0; j<l; j++)
    {
      if(str[i][j]!=' ')
        str[i][j] = map[(int)(str[i][j]-'a')];
    }
  }

  for(i=1; i<=t; i++)
    printf("Case #%d: %s\n", i, str[i]);

  return 0;
}
