#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {
  int numCases, count=1;
  string lineIn;
  cin >> numCases;
  //Used to clear the rest of the line after the int has been read
  getline(cin, lineIn);
  //Loop used to deal with each test case in the input file
  while(count<=numCases) {
    cout << "Case #" << count << ": ";
    //Implement algorithm to solve problem here (or call method if complex)
    int numCombine, numRepel, invokeLength;
    int combineCount=0, repelCount=0, invokeCount=0;
    cin >> numCombine;
    string combine [numCombine];
    while(combineCount<numCombine) cin >> combine[combineCount++];
    cin >> numRepel;
    string repel [numRepel];
    while(repelCount<numRepel) cin >> repel[repelCount++];
    cin >> invokeLength;
    string invoke;
    cin >> invoke;
    
    string output = "[";
    char prevElement = ' ';
    bool possCombo = false, combo = false, possRepel = false, repelFound = false;
    vector<char> repelList;
    for(int i=0; i<invokeLength; i++) {
      char currElement = invoke[i];
      if(combineCount==0 && repelCount==0) {
        output += currElement;
        if(i<invokeLength-1) output += ", ";
      } else {
        if(possCombo) {
          for(int j=0; j<numCombine; j++) {
            if(currElement==combine[j][0]) {
              if(prevElement==combine[j][1]) {
                combo = true;
                output += combine[j][2];
              } else {
                if(prevElement != ' ') {
                  output += prevElement;
                  if(i<invokeLength) output += ", ";
                }
              }
            } else if(currElement==combine[j][1]) {
              if(prevElement==combine[j][0]) {
                combo = true;
                output += combine[j][2];
              } else {
                if(prevElement != ' ') {
                  output += prevElement;
                  if(i<invokeLength) output += ", ";
                }
              }
            } else {
              possCombo = false;
              if(prevElement != ' ') {
                output += prevElement;
                output += ", ";
              }
            }
          }
          if(combo) {
            possCombo = false;
            int pos = -1;
            //if combo formed then make sure prevElement not still in repelList
            for(int k=0; k<repelList.size(); k++) {
              if(prevElement==repelList[k]) {
                pos = k;
                break;
              }
            }
            if(pos>=0) repelList.erase(repelList.begin()+pos);
            prevElement = ' ';
            if(i<invokeLength-1) output += ", ";
          }
        } else {
          for(int j=0; j<numCombine; j++) {
            if(currElement==combine[j][0] || currElement==combine[j][1]) {
              possCombo=true;
              prevElement = currElement;
            }
          }
        }
        if(!combo) {
          for(int j=0; j<numRepel; j++) {
            int repelPos = -1;
            for(int k=0; k<repelList.size(); k++) {
              if(repelList[k]==repel[j][0]) {
                if(currElement==repel[j][1]) {
                  repelFound = true;
                  repelPos = k;
                }
              } else if(repelList[k]==repel[j][1]) {
                if(currElement==repel[j][0]) {
                  repelFound =true;
                  repelPos = k;
                }
              }
            }
            if(repelFound) {
              repelList.clear();
              possCombo = false;
              prevElement = ' ';
              output = "[";
            } else {
              if(currElement==repel[j][0] || currElement==repel[j][1])
                repelList.push_back(currElement);
            }
          }
        }
        if(!possCombo && !repelFound && !combo) {
          output += currElement;
          if(i<invokeLength-1) output += ", ";
          prevElement = currElement;
        }
        if(combo) combo = false;
        if(repelFound) repelFound = false;
      }
    }
    if(possCombo) output += prevElement;
    output += "]";
    
    //Ensure correct output has been printed for this case by here
    cout << output << endl;
    count++;
  }
  return 0;
}
