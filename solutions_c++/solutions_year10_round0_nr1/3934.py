#include <fstream>
#include <iostream>
#include <string>
using namespace std;

string solve(int N, int K){
    unsigned int smapperState = 0;

    unsigned int lightOn = 0xFFFFFFFF >> (sizeof(int)*8 - N);
    string result;
    if (K <= lightOn)
        smapperState = K;
    else{
        smapperState = K&lightOn;
    }
    if (smapperState == lightOn)
       result = "ON";
    else
        result = "OFF";
    return result;
}
int main(int argc, char** argv){
  ifstream in("in.txt");
  ofstream out("out.txt");
  int casesNum;
  in >> casesNum;
  int N, K;
  for (int i=0;i < casesNum;i++){
    in >> N;
    in >> K;
    out << "Case #" << i+1 << ": " << solve(N, K) << endl;
  }
}
