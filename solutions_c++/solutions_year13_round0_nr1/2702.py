/*
  with the help of god
*/
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <stack>

using namespace std;

int main(){
  int t;
  cin>>t;
  int k=1;
  while(t--){
    string s;
    int a[4][4];
    memset(a,0,sizeof(a));
    int isdot=0;
    for(int i=0;i<4;i++){ 
      cin>>s; 
      for(int j=0;j<4;j++){
	if(s[j]=='.'){ a[i][j]=0; isdot=1;}
	else if(s[j]=='X') a[i][j]=1;
	else if(s[j]=='O') a[i][j]=-1;
	else if(s[j]=='T') a[i][j]=100;
      }
    }
    int rowsum[4];
    int colsum[4];
    int digsum[2];
    memset(rowsum,0,sizeof(rowsum));
    memset(colsum,0,sizeof(colsum));
    memset(digsum,0,sizeof(digsum));
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
	rowsum[i]+=a[i][j];
      }
    }
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
	colsum[j]+=a[i][j];
      }
    }
    for(int i=0;i<4;i++) digsum[0]+=a[i][i];
    for(int i=0;i<4;i++) digsum[1]+=a[i][3-i];
    int flag=0;
    for(int i=0;i<4;i++){
      if(colsum[i]==4||colsum[i]==103||rowsum[i]==4||rowsum[i]==103) flag=1; 
    }
    if(digsum[0]==4||digsum[0]==103||digsum[1]==4||digsum[1]==103) flag=1;
    for(int i=0;i<4;i++){
      if(colsum[i]==-4||colsum[i]==97||rowsum[i]==-4||rowsum[i]==97) flag=2; 
    }
    if(digsum[0]==-4||digsum[0]==97||digsum[1]==-4||digsum[1]==97) flag=2;
    if(flag==0&&isdot==1){
      cout<<"Case #"<<k<<":"<<" "<<"Game has not completed"<<endl;
    }
    else if(flag==0&&isdot==0){
      cout<<"Case #"<<k<<":"<<" "<<"Draw"<<endl;
    }
    else if(flag==1){
      cout<<"Case #"<<k<<":"<<" "<<"X won"<<endl;
    }
    else
      cout<<"Case #"<<k<<":"<<" "<<"O won"<<endl;
    k++;
  }
  return 0;
}

