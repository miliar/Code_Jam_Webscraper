#include<iostream>
#include<string>
#include<sstream>
#include<cstdlib>
#include<cstring>
using namespace std;

string itos_convert(int num){
   stringstream ss;
   ss << num;
   return ss.str();
}

int stoi_convert(string s){
   stringstream ss(s);
   int res;
   ss >> res;
   return res;
}

int main(){
   int T;
   cin >> T;
   for(int k = 1 ; k <= T ; k++){
      int a,b;
      cin >> a >> b;
      
      bool used[b+1][b+1];
      memset(used,false,sizeof(used));

      int ans = 0;
      for(int i = a ; i <= b ; i++){
	 string s = itos_convert(i);

	 for(int j = 0 ; j < s.size() - 1; j++){
	    s = s.substr(1) + s[0];
	    if(s[0]=='0')continue;
	    
	    int res = stoi_convert(s);
	    if(a<= res && res <= b && i < res)ans++;
	 }
      }
      
      cout << "Case #" << k << ": " << ans << endl;
   }
   return 0;
}

