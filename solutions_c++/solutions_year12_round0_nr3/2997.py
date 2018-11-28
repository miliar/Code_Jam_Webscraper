#include <iostream>

#include <vector>
#include <cstdio> 

using namespace std; 

#define REP(i, to) for(int i=0; i<to; i++)
typedef long long int LLI;

vector<int> de(int x){
  vector<int> result;
  while(x>0){
    result.push_back(x%10); 
    x /= 10; 
  }
  return result; 
}

int co(vector<int> v){
  int result = 0;
  int ten=1;
  REP(i, v.size()) {
    result += v[i] * ten;
    ten *= 10;
  }
  return result; 
}

vector<int> shift(vector<int> v, int by){
  vector<int> result; 
  REP(i, v.size()) result.push_back(v[(i+v.size()-by)%v.size()]);
  return result; 
}

int main()
{
  int T, A, B;
  cin >> T;
  for(int c=1; c<=T; c++){
    int result = 0;
    cin >> A >> B;
    for(int a=A; a<=B; a++){
      vector<int> v = de(a);
      REP(i, v.size()-1) {
        vector<int> s = shift(v,i+1); 
        int x = co(s); 
        if(a < x && A <= x && x <= B)  {
          result++; 
          //cout << a << ":" << x << endl;
        }
      }
    }
    cout << "Case #"<<c << ": " << result << endl;
  }
  
	return 0;
}
