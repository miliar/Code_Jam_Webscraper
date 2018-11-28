#include <iostream>
#include <list>
#include <string>
using namespace std;

void solve(int);

int main(){
  int T;
  cin >> T;
  for(int i=1; i<=T; ++i){
    solve(i);
  }
  return 0;
}

void solve(int caseNum){
  int C, D, N;
  string elemList, temp, temp1, answer;
  list<string> combine, oppose;
  // get input
  cin >> C;
  for(int i=0; i<C; ++i){
    cin >> temp;    // ex:- QFT
    // ex:- QFT -> QTF
    temp1 = temp; temp1[0] = temp[1]; temp1[1] = temp[0];
    combine.push_back(temp);
    combine.push_back(temp1);
  }
  cin >> D;
  for(int i=0; i<D; ++i){
    cin >> temp;  // ex:- QE
    // ex:- QE -> EQ
    temp1 = temp; temp1[0] = temp[1]; temp1[1] = temp[0];
    oppose.push_back(temp);
    oppose.push_back(temp1);
  }
  cin >> N;
  cin >> elemList;
  
  // process
  int len;
  for(int i=0; i<N; ++i){
    answer += elemList[i];
    len = answer.length();
    if(len < 2)
      continue;
    // combine if u can
    for(list<string>::iterator it = combine.begin(); it != combine.end(); ++it){
      if(answer[len-2] == (*it)[0] && answer[len-1] == (*it)[1]){
        answer[len-2] = (*it)[2];
        answer.erase(len-1, 1);
        break;
      }
    }
    // oppose if u can
    len = answer.length();
    if(len < 2)
      continue;
    bool done = false;
    for(list<string>::iterator it = oppose.begin(); it != oppose.end(); ++it){
      if(answer[len-1] == (*it)[1]){
        int j = len-2;
        while(j >= 0){
          if(answer[j] == (*it)[0]){
            // erase all answer
            answer.erase(0);
            done = true;
            break;
          }
          --j;
        }
        if(done){
          break;
        }
      }
    }
  }
  // print answer
  len = answer.length();
  cout << "Case #" << caseNum << ": " << "[";
  for(int i=0; i<len; ++i){
    cout << answer[i];
    if(i != (len-1))
      cout << ", ";
  }
  cout << "]" << endl;
}
