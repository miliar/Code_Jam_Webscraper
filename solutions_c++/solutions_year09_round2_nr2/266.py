#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main(){
  int t,cas=0;
  cin >> t;

  while (t--){
    cout <<"Case #"<<++cas<<": ";
    string s;
    cin >> s;
    //    cout <<s <<endl;
    bool k= next_permutation(s.begin(),s.end());
    //    cout << s <<" "<<k<<endl;    
    if (!k){
      //      cout << s <<endl;
      
      s.insert(1,1,'0');
      //      cout << s <<endl;

    }
    if (s[0]=='0'){
      for (int i = 1; i < s.length(); ++i)
	if (s[i]!='0'){
	  s[0] = s[i];
	  
	  s[i] = '0';
	  break;
	}
    }
    cout << s <<endl;
    
  }
}

