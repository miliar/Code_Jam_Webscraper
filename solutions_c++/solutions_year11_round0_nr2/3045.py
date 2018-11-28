#include <iostream>
#include <vector>
using namespace std;

int totalTime = 0;

void increaseTime(string color){
  totalTime++;
  //cout << "increase " << color << endl;
}

string runTestCase(int numCo, string co[], int numOp, string op[], int numEle, string ele){
  string result;
  result += ele[0];
  bool f[numOp];
  bool r[numOp];
  for(int i=1; i<numEle; i++){
    bool found = false;
    for(int j=0; j<numCo; j++){
      int size = result.size();
      if((result[size-1]==co[j][0] && ele[i]==co[j][1]) || (result[size-1]==co[j][1] && ele[i]==co[j][0])){
        result = result.substr(0, size-1);
        result += co[j][2];
        found = true;
        break;
      }
    }
    if(found) continue;
    for(int j=0; j<numOp; j++){
      if(ele[i]==op[j][0]){
        for(int k=0; k<result.size(); k++){
          if(result[k]==op[j][1]){
            result.clear();
            found = true;
            break;
          }
        }
      }
      if(ele[i]==op[j][1]){
        for(int k=0; k<result.size(); k++){
          if(result[k]==op[j][0]){
            result.clear();
            found = true;
            break;
          }
        }
      }
    }
    if(found) continue;
    result += ele[i];
  }
  return result;
}

int main(int argc, char *argv[]){
	int numTests;
  cin >> numTests;
  for(int i=1; i<=numTests; i++){
    int combineNum;
    int opposeNum;    
    string combined[100];
    string opposed[100];
    
    cin >> combineNum;
    for(int j=0; j < combineNum; j++){
      cin >> combined[j];
    }
    cin >> opposeNum;
    for(int j=0; j < opposeNum; j++){
      cin >> opposed[j];
    }
    
    int numElements;
    cin >> numElements;
    
    string elements;
    cin >> elements;
    
    string result = runTestCase(combineNum, combined, opposeNum, opposed, numElements, elements);
    cout << "Case #" << i << ": [";
    for(int j=0; j<result.size(); j++){
      if(j!=0) cout << ", ";
      cout << result[j];
    }  
    cout << "]" << endl;
  }
  
  return 0;
}