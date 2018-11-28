#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int main(){
  int t;
  cin >> t;
  int tcNum = 1;
  while(t--){
    vector<string> combine;
    vector<string> combineForm;
    vector<string> opposed;
    vector<int> alpNum(26,0);
    int c,d,n;
    cin >> c;
    for(int i=0; i<c; i++){
      string str; cin >> str;
      string com = str.substr(0,2);
      string comF = str.substr(2,1);

      combine.push_back(com);
      reverse(com.begin(),com.end());
      combine.push_back(com);
      combineForm.push_back(comF);
      combineForm.push_back(comF);
    }
    cin >> d;
    for(int i=0; i<d; i++){
      string str; cin >> str;
      opposed.push_back(str);
    }
    cin >> n;
    string str; cin >> str;
    string ans = "";
    ans += str[0];
    alpNum[str[0] - 'A']++;
    for(int i=1; i<n; i++){
      ans += str[i];
      alpNum[str[i] - 'A']++;
      for(int j=0; j<combine.size(); j++){
	unsigned int loc = ans.find(combine[j]);
	if(string::npos == loc)continue;
	if(loc != ans.size()-2)cout << "error" << endl;
	ans.erase(loc,2); 
	alpNum[combine[j][0]-'A']--;
	alpNum[combine[j][1]-'A']--;
	ans += combineForm[j];
	//	cout << "add :-- " << ans << endl;
	break;
      }
      for(int j=0; j<d; j++){
	int idx1 = opposed[j][0] - 'A';
	int idx2 = opposed[j][1] - 'A';
	if(idx1 == idx2){
	  if(alpNum[idx1] >= 2){
	    ans = ""; 
	    alpNum = vector<int>(26,0);
	  }
	}
	else {
	  if(alpNum[idx1] >= 1 && alpNum[idx2] >= 1){
	    ans = ""; 
	    alpNum = vector<int>(26,0);
	  }
	}
      }
      //      cout << ans << endl;
    }
    printf("Case #%d: [",tcNum++);
    for(int i=0; i<ans.size(); i++){
      if(i!=0)printf(", ");
      printf("%c",ans[i]);
    }
    printf("]\n");
    //    cout << "final --- " << ans << endl;
  }
  return 0;
}
