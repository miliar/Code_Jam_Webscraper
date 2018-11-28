#include <iostream>
#include <iomanip>
#include <string>
using namespace std;
long long a[504][24];
int main(){
  int n;
  cin >> n;
  string s;
  const string cj="welcome to code jam";
  getline(cin,s);
  int cas = 0;
  while (n--){
    ++cas; 
    getline(cin,s);
    memset(a,0,sizeof a);
    for (int i = 0; i < s.length(); ++i){
      if (s[i]==cj[0])
	a[i][0]=1;
      for (int j = 1; j < cj.length(); ++j)	
	if (s[i]==cj[j]){
	  for (int k = 0; k < i; ++k)
	    a[i][j] += a[k][j-1];
	  if (a[i][j]>=10000)
	    a[i][j] = a[i][j]%10000;
	}
    }
    /*    for (int i = 0; i < s.length(); ++i){
      
      for (int j = 0; j < cj.length(); ++j)
	cout << a[i][j] << " ";
      cout << endl;
      
      }*/
    
    long long ans = 0;
    for (int i = 0; i < s.length(); ++i)
      ans+=a[i][cj.length()-1];
    ans = ans%10000;
    cout << "Case #"<<cas << ": "<< setfill('0')<<setw(4)<<ans <<endl;    
    
  }
  
}

