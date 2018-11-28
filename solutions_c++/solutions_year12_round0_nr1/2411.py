#include <iostream>
//#include <cstdio>
#include<string>
#include <map>

using namespace std;

char m[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(){
  int c;
  cin>>c;
  int n=c;
  cin.ignore();
  while(c--){
	string t;
	getline(cin, t);
	cout<<"Case #"<<n-c<<": ";
	for(int i=0; i<t.length(); i++){
	  if(t[i] != 32)
		t[i] = m[(int)t[i]-(int)'a'];
	  cout<<t[i];
	}
	cout<<endl;
  }
  return 0;
}