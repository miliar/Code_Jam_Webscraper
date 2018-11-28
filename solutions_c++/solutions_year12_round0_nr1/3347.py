#include <iostream>
#include <string>
#include <iomanip>
using namespace std;
int main(){
  //init mapping array. q<->z is not for sure.
  char aMap[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
  int nCase;
  cin >> nCase;
  cin.ignore();
//  cin >> noskipws;
  for (int i = 1; i <= nCase; i++){
    string str;
//    cin >> str;
    getline(cin,str);
    string sOut;
    for ( string::iterator it = str.begin() ; it < str.end(); it++ ){
      if (*it == ' ')
        sOut += ' ';
      else
        sOut += aMap[*it-'a'];
    }
    cout << "Case #";
    cout << i << ": " <<sOut<<endl;
  }
//y,h,e,s,o,c,v,x,d,u,i,g,l,b,k,r,z,t,u,w,j,p,f,m,a,q
//  for (int i = 0; i< 26; i++){
//    cout << aMap[i] << "";
//  }
//  cout << endl;
  return 0;
}
