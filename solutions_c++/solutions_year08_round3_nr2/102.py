#include <iostream>
#include <vector>
#include <numeric>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#define REP(i,e) for(int i=0;i<(int)(e);i++)

using namespace std;

char inter[14];
string s;

long long construct(){
  long long n=0,temp=0;
  int sign=1;
  REP(i,s.length()){    
    temp*=10;temp+=(s[i]-'0');

    if (i+1==s.length()) break;
    if (inter[i]=='+') n+=temp*sign, temp=0, sign=1;
    if (inter[i]=='-') n+=temp*sign, temp=0, sign=-1;
  }
  //cout << n+temp*sign << endl;
  return n+temp*sign;
  /*
  string str;
  REP(i,s.length()-1)
    str=str+s[i]+inter[i];
  str=str+s[s.length()-1];

  stringstream sin(str);
  long long n,num;
  char sign;
  sin >> n;
  while(sin >> sign >> num){
    if (sign=='-') n-=num;
    else if (sign=='+') n+=num;
    else cout << "ASSERT!" << endl;
  }
  return n;
  */
}

long long check(){
  long long num=construct();
  return num%2==0 ||num%3==0 ||num%5==0 ||num%7==0;
}
void BruteForce(long long &result,long long depth){
  const static char mid[]={'+','-','#'};
  if (depth==s.length()-1){
    if (check()) result++;
    return ;
  }
  REP(i,3) {
    inter[depth]=mid[i];
    BruteForce(result,depth+1);
  }
}

main(){
  long long CT;
  cin >> CT;
  REP(C,CT){
    cout << "Case #" << C+1 << ": ";
    cin >> s;
    long long result=0;
    BruteForce(result,0);
    cout << result << endl;
  }
}
