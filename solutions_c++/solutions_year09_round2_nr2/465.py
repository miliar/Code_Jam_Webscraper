#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<queue>
#include<map>
#include<set>
#include<cmath>

using namespace std;

#define PB push_back

int main()
{
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    string str;
    cin>>str;

    if( !next_permutation(str.begin(),str.end())) {
      string str0="";
      string stra="";
      for( int i=0;i<str.size();i++){
	if( str[i] == '0')str0+='0';
	else stra+=str[i];
      }
      sort(stra.begin(),stra.end());
  
      reverse(stra.begin(),stra.end());
      char a = stra[stra.size()-1];
      stra[stra.size()-1]='0';
      stra+=str0;
      stra+=a;
      str=stra;
      reverse(str.begin(),str.end());
  
    }
    cout<<"Case #"<<i<<": "<<str<<endl;
  }
  return 0;
}
