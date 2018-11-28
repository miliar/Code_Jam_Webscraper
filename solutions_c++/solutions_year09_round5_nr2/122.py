#include <iostream>
#include <string>
using namespace std;
string a[20];
int b[200][150];
string s;
long long ans[15];
int c[150];
int n,k;
void test(int i){
  if (i==k)
    return;
  
  for (int j = 0; j < n; ++j){
    for (int k ='a'; k<='z'; ++k){
      c[k]+=b[j][k];
    }

    test(i+1);
    long long temp = 0,temp2=1;
    for (int k = 0; k < s.length(); ++k)
      if (s[k]=='+'){
	temp += temp2;
	temp2 = 1;
      } else {
	temp2*=c[s[k]];
      }
    temp+=temp2;
    ans[i]=(ans[i]+temp)%10009;
    for (int k ='a'; k<='z'; ++k){
      c[k]-=b[j][k];
    }
  }
}

int main(){
  int t;
  cin >> t;
  int cas = 0;
  while (t--){
    cout << "Case #"<<++cas<<":";
    cin >> s;
    cin >> k >> n;
    for (int i = 0; i < n; ++i)
      cin >> a[i];
    memset(b,0,sizeof b);
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < a[i].length(); ++j)
	++b[i][(int)a[i][j]];
    /*    for (int i = 0; i < n; ++i){
      for (int k ='a'; k<='z'; ++k)
	cout << b[i][k]<<" ";
      cout <<endl;
      }*/
    
    memset(ans,0,sizeof ans);
    memset(c,0,sizeof c);
    test(0);    
    for (int i = 0; i < k; ++i)
      cout << " " << ans[i];
    cout <<endl;
  }
}
