#include <iostream>
#include <string.h>
using namespace std;

char map[] = { 'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(){
  int N;
  cin>>N;
  char in[1000], out[1000];
  for(int k = 0; k < N; k++){
    cin.getline(in,1000);
    while(strlen(in) == 0)
	cin.getline(in,1000); 
    cout << "Case #"<<k+1<<": ";
    for(int i = 0; in[i]!='\0'; i++){
      if( in[i] >= 'a' && in[i] <= 'z'){
	cout << map[in[i]-'a'];
      }
      else{
	cout << in[i];
      }
    }
    cout<<"\n";
  }
  return 0;
}
      
  
