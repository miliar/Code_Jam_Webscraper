#include<iostream>
using namespace std;
#include <string.h>

int main(int argc, char* argv[])
{
  int num;
  string str;
  string str1 = "yhesocvxduiglbkrztnwjpfmaq";
  cin>>num;
  // ifstream ifs(argv[1]);
   getline(cin, str);
  for( int i=0; i<num; i++ ){
     getline(cin, str);
    int j =0;
    char x=str[j];
      cout<<"Case #"<<i+1<<": ";
    while(str[j]!='\0'){
      if( x>='a' && x<='z' )
	cout<<str1[x-'a'];
      else cout<<x; 
      j++;
      x= str[j];
    }
    cout<<endl;
  }
}
