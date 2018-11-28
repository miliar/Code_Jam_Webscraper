#include<iostream>
#include<vector>
using namespace std;

int main(){
  int t,c,d,n;
  int i,j,k;
  string tmp;
  vector<char> com1,com2,com3;
  vector<char> op1,op2;
  vector<char> ans;
  int flag;
  int cases;

  cin >> t;
  cases = t;
  while(t){
    t--;
    com1.clear();
    com2.clear();
    com3.clear();
    op1.clear();
    op2.clear();
    ans.clear();
    cin >> c;
    while(c){
      c--;
      cin >> tmp;
      com1.push_back(tmp[0]);
      com2.push_back(tmp[1]);
      com3.push_back(tmp[2]);
    }
    cin >> d;
    while(d){
      d--;
      cin >> tmp;
      op1.push_back(tmp[0]);
      op2.push_back(tmp[1]);
    }
    cin >> n;
    cin >> tmp;

    ans.push_back(tmp[0]);
    for(i=1;i<n;i++){
      flag = 0;
      for(j=0;j<com1.size();j++){
	if(tmp[i] == com1[j] && ans[ans.size()-1] == com2[j]){
	  ans.pop_back();
	  ans.push_back(com3[j]);
	  flag = 1;
	  break;
	}else if(tmp[i] == com2[j] && ans[ans.size()-1] == com1[j]){
	  ans.pop_back();
	  ans.push_back(com3[j]);
	  flag = 1;
	  break;
	}
      }
      if(!flag){
	for(j=0;j<ans.size();j++){
	   for(k=0;k<op1.size();k++){
	     if(tmp[i] == op1[k] && ans[j] == op2[k]){
	       ans.clear();
	       flag = 1;
	       break;
	     }else if(tmp[i] == op2[k] && ans[j] == op1[k]){
	       ans.clear();
	       flag = 1;
	       break;
	     }
	   }
	   if(flag)break;
	}
      }
      if(!flag)ans.push_back(tmp[i]);
    }
    cout << "Case #" << cases - t << ": [";
    if(ans.size()>0){
      for(i=0;i<ans.size()-1;i++)cout << ans[i] << ", ";
      cout << ans[ans.size()-1] << "]" << endl;
    }else{
      cout << "]" << endl;
    }
  }
}
