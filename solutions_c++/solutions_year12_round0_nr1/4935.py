#include<iostream>
#include<vector>
#include<string>
#include<cstdio>
#include<cstring>
using namespace std;

int main(){
  int n,i,len;
  string str,new_str;
  freopen("A-small-attempt0.in","r",stdin);
  freopen("A-small-attempt0.out","w",stdout);
  vector<string> res;
  char change[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
  cin>>n;
  getline(cin,str);
  while(n--){
    getline(cin,str);
    //cout<<str<<endl;
    new_str.clear();
    len = str.length();
    for(i=0;i<len;i++){
      if(!isspace(str[i]))
      new_str += change[str[i]-'a'];
      else
      new_str += str[i];
    }
    res.push_back(new_str);
  }
  for(i=1;i<=res.size();i++){
    cout<<"Case #"<<i<<": "<<res[i-1]<<endl;
  }
  fclose(stdin);
  fclose(stdout);

  return 0;
}
