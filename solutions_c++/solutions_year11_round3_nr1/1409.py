#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <list>
#include <cmath>
#include <deque>
#include <numeric>
#include <algorithm>

using namespace std;

int main(void){
  int T_NumberOfCases,NowCaseNumber;
  cin>>T_NumberOfCases;
  for(NowCaseNumber=1;NowCaseNumber<=T_NumberOfCases;NowCaseNumber++){
    cout<<"Case #"<<NowCaseNumber<<":\n";
    int R,C;
    cin>>R;
    cin>>C;
    vector<string> data(R);
    for(int i=0;i<R;i++)cin>>data[i];
    int dx[3]={1,0,1};
    int dy[3]={0,1,1};
    string moji("\\\\/");
    for(int i=0;i<R;i++){
      for(int j=0;j<C;j++){
	if(data[i][j]=='#'){
	  data[i][j]='/';
	  if(i+1==R || j+1==C){
	    cout<<"Impossible\n";
	    goto skip;
	  }
	  for(int k=0;k<3;k++){
	    if(data[i+dx[k]][j+dy[k]]!='#'){
	      cout<<"Impossible\n";
	      goto skip;
	    }else{
	      data[i+dx[k]][j+dy[k]]=moji[k];
	    }
	  }
	}
      }
    }
    for(int i=0;i<R;i++){
      cout<<data[i]<<"\n";
    }
  skip:
    continue;
  }
  return 0;
}


