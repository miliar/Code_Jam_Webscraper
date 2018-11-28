#include <iostream>
#include <map>
#include <string.h>
using namespace std;

map<char,char> translate;

int main()
{
  char a[1000];
  char b[1000];
  translate['q'] = 'z';
  translate['z'] = 'q';
  for(int k=0;k<3;k++)
  {
    cin.getline(a,1000);
    cin.getline(b,1000);
    for(int i=0;i<strlen(a);i++)
      translate[a[i]] = b[i];
  }
  int n;
  cin >> n;
  cin.getline(a,10);
  for(int i=0;i<n;i++)
  {
    cout << "Case #" << i+1 << ": ";
    cin.getline(a,1000);
    for(int j=0;j<strlen(a);j++)
      cout << translate[a[j]];
    cout << endl;
  }
}

