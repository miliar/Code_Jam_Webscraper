#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cstring>
#include <map>
#include <cctype>

#define rep(i,n) for(int i=0;i<n;i++)
#define rp(i,n) for(i=0;i<n;i++)
#define pr(i) cout<<i<<endl

using namespace std;

int n;
char a,b;
map<char,char> mp;

int main(){

  FILE *fp=fopen("t.in","r");

  rep(i,26){
    fscanf(fp,"%c %c\n",&a,&b);
    mp[a]=b;
  }


  cin>>n;getchar();
  string input;

  rep(i,n){
    getline(cin,input);
    cout<<"Case #"<<i+1<<": ";
    rep(j,input.size()){
      if(isalpha(input[j]))cout<<mp[input[j]];
      else cout<<input[j];
    }
    cout<<endl;
  }



}
