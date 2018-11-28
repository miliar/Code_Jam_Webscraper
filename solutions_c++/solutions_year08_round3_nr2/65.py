#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
#include<cmath>

using namespace std;

long long tab[15][15];

int main(){
  int Q;
  ios::sync_with_stdio(false);
  cin >> Q;
  for(int q=1;q<=Q;q++){
    string s;
    cin >> s;
    for(int i=0;i<s.size();i++){
      long long val=s[i]-'0';
      tab[i][i]=val;
      for(int j=i+1;j<s.size();j++){
	val*=10;
	val+=s[j]-'0';
	tab[i][j]=val;
      }
    }
    int cnt = 0;
    int maxi = (int)pow(3.0,(double)s.size()-1);
    for(int i=0; i<maxi;i++){
      int sind = 0;
      int t=i;
      long long num=0;
      int cind = 0;
      bool plus = true;
      while(t>0){
	int k = t%3;
	t/=3;
	if(k==0)cind++;
	else {
	  if(plus)num+=tab[sind][cind];
	  else num-=tab[sind][cind];
	  sind = cind+1;
	  cind++;
	  if(k==1)plus=true;
	  else plus=false;
	}
      }
      if(plus)num+=tab[sind][s.size()-1];
      else num-=tab[sind][s.size()-1];
      if(!(num%2 && num%3 && num%5 && num%7)){
	cnt++;
      }
    }
    cout<<"Case #"<<q<<": "<<cnt<<endl;
  }
  return 0;
}
