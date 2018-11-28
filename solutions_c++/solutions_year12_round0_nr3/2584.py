#include<iostream>
#include<sstream>
#include<map>
using namespace std;
#define N 2000000

int cnt[N+1];
string com[N+1];
int n,m,t;

string shift(string str){
  int l = str.size();
  return str.substr(l-1,1)+str.substr(0,l-1);
}

int init(){
  for(int i=0 ; i<10 ; i++)
    cnt[i] = 0;
  // cout << "0 init" << endl;
  for(int i=10 ; i<N+1 ; i++){
    int d_cnt = 0,temp = i;
    string str1,str2;
    stringstream ss; 
    //cout << "test" << endl;
    //cout << i << ":";
    //cout << "outputed" << endl; 
    ss << i;
    ss >> str1;
    com[i] = str1;
    //cout << "str1:" << str1 << " str2:" << str2 <<endl;
    str2 = shift(str1); 
    //cout << "str1:" << str1 << " str2:" << str2 <<endl;
    while(str1!=str2){
      // cout << str1 << ' ' << str2 << endl;
      if(str2[0]!='0' && str1>str2){
	d_cnt++;
	if(com[i]>str2)com[i] = str2;
      }
      str2=shift(str2);
    }
    cnt[i] = d_cnt;
    //cout << cnt[i] << endl;
  }
  return 0;
}

int solve(){
  int ret = 0;
  cin >> m >> n;
  map<string,int> mp;
  for(int i=m ; i<n+1 ; i++){
    string c = com[i];
    map<string,int>::iterator it = mp.find(c);
    if(it!=mp.end()){
      //cout << i << endl;
      int s = (*it).second;
      ret += cnt[i]-s;
    }
    else mp.insert(make_pair(com[i],cnt[i]));
  }
  return ret;
}

int main(){
  //cout << "before init" << endl;
  init();
  //cout << "after init" << endl;
  cin >> t;
  for(int i=0 ; i<t ; i++)
    cout << "Case #" << i+1 << ": " << solve() <<  endl;
  return 0;
}
