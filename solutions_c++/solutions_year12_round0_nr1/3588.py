#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
void map_f(char& a) {
  if(a!=' ')
    a = map[a-'a'];
}
main() {
  int n;
  cin>>n;
  for(int i(0);i!=n;++i) {
    string temp;
    while(temp.empty())
      getline(cin,temp);
    for_each(temp.begin(),temp.end(),map_f);
    cout<<"Case #"<<i+1<<": "<<temp<<endl;
  }
}
