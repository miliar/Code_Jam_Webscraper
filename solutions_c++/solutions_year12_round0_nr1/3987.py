#include <iostream>
#include <algorithm>
#include <string.h>


using namespace std;

int main()
{
  int nTestCases=0;
  char arr[256];
  char *mapping = "yhesocvxduiglbkrztnwjpfmaq";

  cin>>nTestCases;
  cin.getline(arr, 256);
  for (int i=1; i<=nTestCases; ++i)
  {
    memset(arr, 0, 256);
    cin.getline(arr, 256);

    for(int j=0; j<strlen(arr); ++j)
    {
      if (arr[j] >= 'a' && arr[j]<='z')
        arr[j] = mapping[arr[j]-'a'];
    }

    cout<<"Case #"<<i<<": "<<arr<<"\n";
  }
}

